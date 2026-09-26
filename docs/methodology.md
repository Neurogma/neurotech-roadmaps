# Methodology

## Source of truth

- `nodes/**/*.yml` are the canonical learning capabilities. `prerequisites` live only there.
- `roadmaps/*.yml` are the canonical roadmap structure; `scripts/generate_roadmaps.py` renders the GitHub-facing Markdown.
- `projects/**/*.yml` are project specifications.
- `resources/catalog.yml` is the only resource catalog.
- `papers/paper-guides/*.yml` are structured reading guides.

Do not add a second index, graph store or metadata copy. A derived view is acceptable only when generated from the canonical data.

## Prerequisite semantics

Use `prerequisites` only for material blockers or risks of serious misunderstanding. Topic similarity is not a prerequisite. Do not use `related` as a second dependency graph.

Roadmap order matters: a node should appear after the capabilities it genuinely needs, unless the roadmap explicitly treats a prerequisite as an external starting assumption. CI validates this for core paths and optional-branch order.

## Levels

- **foundation** — transferable prerequisite knowledge or field vocabulary.
- **intermediate** — multi-step analysis or implementation.
- **advanced** — integrated systems or specialized methods.
- **research** — primary literature, methodological limits, critical interpretation and open questions.

Projects use `beginner`, `intermediate`, `advanced` and `research` because project difficulty is not identical to conceptual-node level.

## Pedagogy

Good paths move from concepts → practice → evidence. Learning objectives should be observable. Projects must expose a concrete input, work product and evaluation criterion.

The repository deliberately avoids deep-learning-first paths, vague “understand X” objectives, arbitrary prerequisite chains and resource-count optimization.

## Scientific wording

Separate established knowledge, study-specific findings, engineering assumptions, hypotheses and open questions. Do not use sensational shorthand such as “reads thoughts” unless the task and inferential limits are explicitly defined.

## Resource curation

Fewer strong resources are preferred. A resource marked `active` is eligible to appear in current roadmaps and nodes.

Active resources must carry:

- `provenance.source_type` — the class of authority being relied on.
- `provenance.last_verified` — the date the catalog entry and linked source were reviewed.
- `provenance.review_interval_days` — the intended maintenance interval.

The review date is a maintenance record, not a claim that the underlying source cannot change. Review intervals should be shorter for fast-moving software, standards and policy than for stable textbooks or long-lived courses.

Resources in `needs-review`, `deprecated`, `broken-link` or `archived` status are intentionally unavailable to current roadmaps and nodes. This prevents a broken link from remaining pedagogically “live” just because a reference was not removed yet.

`community-submitted` is suitable for candidate material that has not yet been promoted into the curated active set.

## Validation

Run:

```bash
python scripts/generate_roadmaps.py --check
python scripts/validate.py --strict-provenance
python -m unittest discover -s tests -v
```

The validator checks:

- schema validity and duplicate IDs;
- internal references and related-paper references;
- dependency cycles and prerequisite order;
- roadmap section duplication;
- use of only active resources;
- orphan records;
- resource provenance freshness;
- internal Markdown links;
- generated Markdown drift.

Use `python scripts/validate.py --urls` for a best-effort external URL check. Scheduled CI runs strict provenance and external-link checks.

## Review principle

Prefer a smaller, well-maintained evidence base to a larger catalog whose freshness and scope cannot be defended. When in doubt, move a resource to `needs-review` rather than silently weakening the standard for `active`.
