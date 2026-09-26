# Contributing

This project values accurate, teachable content over repository size. A contribution should make the learning system more useful, more verifiable or easier to maintain.

## Where changes belong

- **Node:** a reusable capability that can serve more than one learning goal.
- **Roadmap:** a change to sequencing, scope, destination or branching. Edit the YAML; generated Markdown is not hand-maintained.
- **Project:** an evidence-producing activity with a concrete input and evaluation criteria.
- **Resource:** a small, high-value source with a clear learner-facing rationale and provenance.
- **Paper guide:** a paper whose methods or evidence can support a specific learning goal.

## Quality rules

1. Write measurable learning objectives.
2. Put only true blockers in `prerequisites`.
3. Omit fields that do not add information. Do not use `null`, `None` or empty arrays as fillers.
4. Avoid duplicating the same claim or relationship across files.
5. Verify URLs and bibliographic metadata against stable sources.
6. Distinguish established evidence from study-specific results and emerging claims.
7. Keep safety notes specific to the actual risk.
8. Use realistic ranges instead of false precision.
9. New resources intended for current roadmaps must have complete `provenance` metadata. `last_verified` records the latest catalog review, while `review_interval_days` controls when another review becomes due.
10. Do not reference resources whose status is `needs-review`, `deprecated`, `broken-link` or `archived` from an active roadmap or node.

## Review

Run:

```bash
python scripts/generate_roadmaps.py --check
python scripts/validate.py --strict-provenance
python -m unittest discover -s tests -v
```

Use `python scripts/validate.py --urls` when reviewing external links.

A content PR should say what changed pedagogically and what source evidence supports any scientific correction. Prerequisite changes deserve explicit explanation because they change the learning graph.

For resource changes, explain whether the URL, source identity, scope, licensing, scientific relevance or maintenance state changed. A stale resource should move to `needs-review` until the review is complete; do not keep it `active` merely to preserve a roadmap link.
