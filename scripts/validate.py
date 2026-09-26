#!/usr/bin/env python3

from pathlib import Path
from datetime import date, timedelta
import argparse
import json
import subprocess
import sys
import urllib.request

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]

SCHEMAS = {
    p.name: json.loads(p.read_text())
    for p in (ROOT / "schemas").glob("*.json")
}


def load(directory):
    records = {}

    for path in sorted(directory.rglob("*.yml")):
        data = yaml.safe_load(path.read_text())

        if not isinstance(data, dict) or "id" not in data:
            raise AssertionError(f"Invalid record: {path}")

        record_id = data["id"]

        if record_id in records:
            raise AssertionError(f"Duplicate id: {record_id}")

        records[record_id] = (path, data)

    return records


def load_resources():
    path = ROOT / "resources" / "catalog.yml"
    data = yaml.safe_load(path.read_text())

    if not isinstance(data, list):
        raise AssertionError(f"{path} must contain a YAML list")

    resources = {}
    validator = Draft202012Validator(
        SCHEMAS["resource.schema.json"],
        format_checker=FormatChecker(),
    )

    for resource in data:
        if not isinstance(resource, dict) or "id" not in resource:
            raise AssertionError(f"Invalid resource in {path}")

        resource_id = resource["id"]

        if resource_id in resources:
            raise AssertionError(
                f"Duplicate resource id: {resource_id}"
            )

        errors = sorted(
            validator.iter_errors(resource),
            key=lambda error: list(error.path),
        )

        if errors:
            raise AssertionError(
                f"resource {resource_id}: {errors[0].message}"
            )

        resources[resource_id] = resource

    return resources


def validate_schema(records, schema_name):
    validator = Draft202012Validator(
        SCHEMAS[schema_name],
        format_checker=FormatChecker(),
    )

    for path, data in records.values():
        errors = sorted(
            validator.iter_errors(data),
            key=lambda error: list(error.path),
        )

        if errors:
            raise AssertionError(
                f"{schema_name}: {path}: {errors[0].message}"
            )


def check_references(records, field, targets, label):
    for record_id, (_, data) in records.items():
        for value in data.get(field, []):
            if value not in targets:
                raise AssertionError(
                    f"Missing {label} {value} from {record_id}"
                )


def check_active_resources(records, resources):
    for record_id, (_, data) in records.items():
        for field in ("resources", "datasets"):
            for resource_id in data.get(field, []):
                resource = resources[resource_id]
                if resource["status"] != "active":
                    raise AssertionError(
                        f"{record_id} references non-active resource "
                        f"{resource_id} (status: {resource['status']})"
                    )


def check_resource_provenance(resources, strict):
    today = date.today()
    stale = []

    for resource_id, resource in resources.items():
        provenance = resource.get("provenance")
        if not provenance:
            if resource["status"] == "active":
                raise AssertionError(
                    f"Active resource without provenance: {resource_id}"
                )
            continue

        verified_on = date.fromisoformat(provenance["last_verified"])
        review_after = verified_on + timedelta(
            days=provenance["review_interval_days"]
        )

        if review_after < today:
            stale.append(
                f"{resource_id} (review due {review_after.isoformat()})"
            )

    if stale:
        message = "Stale resource provenance: " + "; ".join(stale)
        if strict:
            raise AssertionError(message)
        print(f"VALIDATION WARNING: {message}")


def check_paper_relations(papers):
    for paper_id, (_, paper) in papers.items():
        for related_id in paper.get("related_papers", []):
            if related_id not in papers:
                raise AssertionError(
                    f"Missing related paper {related_id} from {paper_id}"
                )


def check_roadmap_sections(roadmaps):
    for roadmap_id, (_, roadmap) in roadmaps.items():
        for field in ("prerequisites", "core_path", "optional_branches"):
            values = roadmap.get(field, [])
            if len(values) != len(set(values)):
                raise AssertionError(
                    f"Roadmap {roadmap_id} contains a duplicate node "
                    f"inside {field}"
                )

        core = set(roadmap.get("core_path", []))
        optional = set(roadmap.get("optional_branches", []))
        overlap = sorted(core & optional)

        if overlap:
            raise AssertionError(
                f"Roadmap {roadmap_id} repeats node(s) "
                f"between core_path and optional_branches: {overlap}"
            )

def check_prerequisites(nodes):
    graph = {
        node_id: set(data["prerequisites"])
        for node_id, (_, data) in nodes.items()
    }

    for node_id, (_, node) in nodes.items():
        prerequisites = graph[node_id]

        if (
            not prerequisites
            and node.get("level") != "foundation"
        ):
            raise AssertionError(
                f"Non-foundation node without prerequisites: "
                f"{node_id}"
            )

        if node_id in prerequisites:
            raise AssertionError(
                f"Self prerequisite: {node_id}"
            )

    state = {}

    def visit(node_id, stack=()):
        if state.get(node_id) == 1:
            cycle = " -> ".join(
                (*stack, node_id)
            )
            raise AssertionError(
                f"Prerequisite cycle: {cycle}"
            )

        if state.get(node_id) == 2:
            return

        state[node_id] = 1

        for dependency in graph[node_id]:
            if dependency not in nodes:
                raise AssertionError(
                    f"Missing prerequisite "
                    f"{dependency} from {node_id}"
                )

            visit(
                dependency,
                (*stack, node_id),
            )

        state[node_id] = 2

    for node_id in graph:
        visit(node_id)

    return graph


def check_roadmap_order(roadmaps, nodes):
    for roadmap_id, (_, roadmap) in roadmaps.items():
        satisfied = set(
            roadmap["prerequisites"]
        )

        for node_id in roadmap["core_path"]:
            missing = (
                set(nodes[node_id][1]["prerequisites"])
                - satisfied
            )

            if missing:
                raise AssertionError(
                    f"Roadmap {roadmap_id} places "
                    f"{node_id} before prerequisites: "
                    f"{sorted(missing)}"
                )

            satisfied.add(node_id)

        for node_id in roadmap.get(
            "optional_branches", []
        ):
            missing = (
                set(nodes[node_id][1]["prerequisites"])
                - satisfied
            )

            if missing:
                raise AssertionError(
                    f"Roadmap {roadmap_id} branch "
                    f"{node_id} has undeclared "
                    f"prerequisites: {sorted(missing)}"
                )


def check_orphans(
    nodes,
    projects,
    roadmaps,
    papers,
    resources,
    graph,
):
    used_nodes = set()
    used_projects = set()
    used_papers = set()
    used_resources = set()

    for _, roadmap in roadmaps.values():
        used_nodes.update(
            roadmap["prerequisites"]
        )
        used_nodes.update(
            roadmap["core_path"]
        )
        used_nodes.update(
            roadmap.get("optional_branches", [])
        )

        used_projects.update(
            roadmap.get("projects", [])
        )
        used_papers.update(
            roadmap.get("papers", [])
        )
        used_resources.update(
            roadmap.get("resources", [])
        )
        used_resources.update(
            roadmap.get("datasets", [])
        )

    for _, project in projects.values():
        used_nodes.update(
            project["prerequisite_skills"]
        )

    for node_id, (_, node) in nodes.items():
        used_resources.update(
            node.get("resources", [])
        )
        used_papers.update(
            node.get("sources", [])
        )

        if any(
            node_id in dependencies
            for dependencies in graph.values()
        ):
            used_nodes.add(node_id)

    orphans = {
        "nodes": set(nodes) - used_nodes,
        "projects": set(projects) - used_projects,
        "papers": set(papers) - used_papers,
        "resources": set(resources) - used_resources,
    }

    for kind, ids in orphans.items():
        if ids:
            raise AssertionError(
                f"Orphan {kind}: "
                + ", ".join(sorted(ids))
            )


def check_internal_links():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue

        text = path.read_text()

        for chunk in text.split("](")[1:]:
            target = (
                chunk
                .split(")", 1)[0]
                .split("#", 1)[0]
            )

            if target.startswith(
                ("http://", "https://", "mailto:")
            ):
                continue

            if target and not (
                path.parent / target
            ).resolve().exists():
                raise AssertionError(
                    f"Broken internal link in "
                    f"{path}: {target}"
                )


def check_generated_markdown():
    result = subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "scripts"
                / "generate_roadmaps.py"
            ),
            "--check",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode:
        raise AssertionError(
            result.stdout.strip()
            or result.stderr.strip()
        )


def check_urls(resources):
    warnings = 0

    for resource_id, resource in resources.items():
        try:
            request = urllib.request.Request(
                resource["url"],
                headers={
                    "User-Agent":
                    "neurotech-roadmaps-link-check"
                },
            )

            with urllib.request.urlopen(
                request,
                timeout=12,
            ) as response:
                if response.status >= 400:
                    print(
                        f"URL WARNING: "
                        f"{resource_id}: "
                        f"HTTP {response.status}"
                    )
                    warnings += 1

        except Exception as error:
            print(
                f"URL WARNING: "
                f"{resource_id}: {error}"
            )
            warnings += 1

    print(
        f"External URL checks completed "
        f"with {warnings} warning(s)."
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--urls",
        action="store_true",
        help="also check external resource URLs",
    )
    parser.add_argument(
        "--strict-provenance",
        action="store_true",
        help="fail when active resources are past their review date",
    )
    args = parser.parse_args()

    nodes = load(ROOT / "nodes")
    projects = load(ROOT / "projects")
    roadmaps = load(ROOT / "roadmaps")
    papers = load(
        ROOT / "papers" / "paper-guides"
    )
    resources = load_resources()

    validate_schema(
        nodes,
        "node.schema.json",
    )
    validate_schema(
        projects,
        "project.schema.json",
    )
    validate_schema(
        roadmaps,
        "roadmap.schema.json",
    )
    validate_schema(
        papers,
        "paper.schema.json",
    )

    check_references(
        nodes,
        "resources",
        resources,
        "resource",
    )
    check_references(
        nodes,
        "sources",
        papers,
        "paper",
    )
    check_references(
        projects,
        "prerequisite_skills",
        nodes,
        "node",
    )

    for field in (
        "prerequisites",
        "core_path",
        "optional_branches",
    ):
        check_references(
            roadmaps,
            field,
            nodes,
            "node",
        )

    check_references(
        roadmaps,
        "projects",
        projects,
        "project",
    )
    check_references(
        roadmaps,
        "papers",
        papers,
        "paper",
    )
    check_references(
        roadmaps,
        "resources",
        resources,
        "resource",
    )
    check_references(
        roadmaps,
        "datasets",
        resources,
        "resource",
    )

    check_active_resources(nodes, resources)
    check_active_resources(roadmaps, resources)
    check_paper_relations(papers)
    check_roadmap_sections(roadmaps)

    graph = check_prerequisites(nodes)

    check_roadmap_order(
        roadmaps,
        nodes,
    )

    check_resource_provenance(
        resources,
        strict=args.strict_provenance,
    )

    check_orphans(
        nodes,
        projects,
        roadmaps,
        papers,
        resources,
        graph,
    )

    check_internal_links()
    check_generated_markdown()

    if args.urls:
        check_urls(resources)

    print(
        f"Validation passed: "
        f"{len(nodes)} nodes, "
        f"{len(roadmaps)} roadmaps, "
        f"{len(projects)} projects, "
        f"{len(resources)} resources, "
        f"{len(papers)} paper guides."
    )


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(
            f"VALIDATION FAILED: {error}"
        )
        raise SystemExit(1)
