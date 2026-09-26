#!/usr/bin/env python3
"""Generate the human-readable Markdown pages for each roadmap."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]

ROADMAP_DIR = ROOT / "roadmaps"
NODE_DIR = ROOT / "nodes"
PROJECT_DIR = ROOT / "projects"
PAPER_DIR = ROOT / "papers" / "paper-guides"
RESOURCE_FILE = ROOT / "resources" / "catalog.yml"


def load_records(
    directory: Path,
) -> dict[str, tuple[Path, dict[str, Any]]]:
    """Load YAML records indexed by their stable ID."""
    records: dict[str, tuple[Path, dict[str, Any]]] = {}

    for path in sorted(directory.rglob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))

        if not isinstance(data, dict) or not isinstance(data.get("id"), str):
            raise ValueError(f"Invalid record in {path}")

        record_id = data["id"]

        if record_id in records:
            previous = records[record_id][0]
            raise ValueError(
                f"Duplicate id {record_id!r}: {previous} and {path}"
            )

        records[record_id] = (path, data)

    return records


def load_resources() -> dict[str, dict[str, Any]]:
    """Load the shared resource catalog."""
    data = yaml.safe_load(
        RESOURCE_FILE.read_text(encoding="utf-8")
    )

    if not isinstance(data, list):
        raise ValueError(
            f"{RESOURCE_FILE} must contain a YAML list"
        )

    resources: dict[str, dict[str, Any]] = {}

    for item in data:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError(
                f"Invalid resource record in {RESOURCE_FILE}"
            )

        resource_id = item["id"]

        if resource_id in resources:
            raise ValueError(
                f"Duplicate resource id {resource_id!r}"
            )

        resources[resource_id] = item

    return resources


def relative_link(path: Path) -> str:
    """Return a Markdown link from a generated roadmap page."""
    return "../" + path.relative_to(ROOT).as_posix()


def render_roadmap(
    roadmap: dict[str, Any],
    nodes: dict[str, tuple[Path, dict[str, Any]]],
    projects: dict[str, tuple[Path, dict[str, Any]]],
    papers: dict[str, tuple[Path, dict[str, Any]]],
    resources: dict[str, dict[str, Any]],
) -> str:
    """Render one roadmap YAML record as Markdown."""
    lines = [
        f"# {roadmap['title']}",
        "",
        roadmap["audience"],
        "",
    ]

    def heading(title: str) -> None:
        lines.extend([f"## {title}", ""])

    def bullets(items: list[str]) -> None:
        lines.extend(f"- {item}" for item in items)
        lines.append("")

    if roadmap.get("destination_outcomes"):
        heading("Destination")
        bullets(roadmap["destination_outcomes"])

    if roadmap.get("starting_assumptions"):
        heading("Starting assumptions")
        bullets(roadmap["starting_assumptions"])

    if roadmap.get("prerequisites"):
        heading("Entry prerequisites")

        for node_id in roadmap["prerequisites"]:
            path, node = nodes[node_id]
            lines.append(
                f"- [{node['title']}]({relative_link(path)})"
            )

        lines.append("")

    heading("Time budgets")

    for level, hours in roadmap["estimated_hours"].items():
        lines.append(f"- **{level.title()}:** {hours}")

    lines.append("")

    heading("Core path")

    for index, node_id in enumerate(roadmap["core_path"], start=1):
        path, node = nodes[node_id]
        lines.append(
            f"{index}. [{node['title']}]"
            f"({relative_link(path)}) — `{node_id}`"
        )

    lines.append("")

    if roadmap.get("optional_branches"):
        heading("Optional branches")

        for node_id in roadmap["optional_branches"]:
            path, node = nodes[node_id]
            lines.append(
                f"- [{node['title']}]({relative_link(path)})"
            )

        lines.append("")

    text_sections = (
        ("minimum_viable_path", "Minimum viable path"),
        ("deeper_path", "Deeper path"),
    )

    for field, title in text_sections:
        if roadmap.get(field):
            heading(title)
            lines.extend([roadmap[field], ""])

    if roadmap.get("projects"):
        heading("Projects")

        for project_id in roadmap["projects"]:
            path, project = projects[project_id]
            lines.append(
                f"- [{project['title']}]({relative_link(path)})"
            )

        lines.append("")

    if roadmap.get("papers"):
        heading("Paper sequence")

        for paper_id in roadmap["papers"]:
            path, paper = papers[paper_id]
            lines.append(
                f"- [{paper['title']}]({relative_link(path)})"
            )

        lines.append("")

    # Backward-compatible support for the current roadmap format.
    # New roadmaps can put datasets into "resources" with kind: dataset.
    resource_ids = list(roadmap.get("resources", []))
    resource_ids.extend(roadmap.get("datasets", []))

    if resource_ids:
        heading("Resources")

        seen: set[str] = set()

        for resource_id in resource_ids:
            if resource_id in seen:
                continue

            seen.add(resource_id)
            resource = resources[resource_id]

            lines.append(
                f"- **{resource['title']}** — {resource['url']}"
            )

        lines.append("")

    list_sections = (
        ("common_misconceptions", "Common misconceptions"),
        ("typical_failure_modes", "Typical failure modes"),
        ("research_directions", "Research directions"),
    )

    for field, title in list_sections:
        if roadmap.get(field):
            heading(title)
            bullets(roadmap[field])

    text_sections = (
        ("safety", "Safety"),
        ("ethics", "Ethics"),
        ("next_steps", "What to learn next"),
    )

    for field, title in text_sections:
        if roadmap.get(field):
            heading(title)
            lines.extend([roadmap[field], ""])

    return "\n".join(lines).rstrip() + "\n"


def render_all(check_only: bool) -> int:
    """Generate or validate all roadmap Markdown pages."""
    nodes = load_records(NODE_DIR)
    projects = load_records(PROJECT_DIR)
    papers = load_records(PAPER_DIR)
    resources = load_resources()

    expected: dict[Path, str] = {}

    for yaml_path in sorted(ROADMAP_DIR.glob("*.yml")):
        roadmap = yaml.safe_load(
            yaml_path.read_text(encoding="utf-8")
        )

        if not isinstance(roadmap, dict):
            raise ValueError(
                f"Invalid roadmap in {yaml_path}"
            )

        markdown_path = yaml_path.with_suffix(".md")

        expected[markdown_path] = render_roadmap(
            roadmap,
            nodes,
            projects,
            papers,
            resources,
        )

    changed: list[str] = []

    for markdown_path, content in expected.items():
        current = (
            markdown_path.read_text(encoding="utf-8")
            if markdown_path.exists()
            else None
        )

        if current != content:
            changed.append(markdown_path.name)

            if not check_only:
                markdown_path.write_text(
                    content,
                    encoding="utf-8",
                )

    # Generated files are never deleted automatically.
    # Stale pages are reported instead.
    generated_pages = {
        path
        for path in ROADMAP_DIR.glob("*.md")
        if path.name != "bci-12-week-plan.md"
    }

    stale = sorted(
        path.name
        for path in generated_pages - set(expected)
    )

    if check_only:
        problems = sorted(set(changed + stale))

        if problems:
            print(
                "Generated roadmap files out of date: "
                + ", ".join(problems)
            )
            return 1

        print(
            f"Roadmaps are up to date: {len(expected)}"
        )
        return 0

    print(f"Roadmaps rendered: {len(expected)}")

    if stale:
        print(
            "Stale generated pages were not removed automatically: "
            + ", ".join(stale)
        )

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate or check roadmap Markdown files."
    )

    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail when generated Markdown is out of date.",
    )

    args = parser.parse_args()

    return render_all(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
