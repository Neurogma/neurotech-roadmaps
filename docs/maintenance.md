# Maintenance

The repository is a curated learning system, so maintenance is partly an epistemic task: a URL can remain reachable while a resource becomes outdated, a standard changes, or a method's recommended practice shifts.

## Resource states

- `active` — eligible for current roadmaps and nodes.
- `needs-review` — temporarily excluded while its identity, scope, relevance or URL is checked.
- `community-submitted` — candidate material that has not yet been promoted into the active curated set.
- `deprecated` — superseded by a better or newer source.
- `broken-link` — the stored URL is no longer usable.
- `archived` — historically useful but no longer part of the current learning path.

Never leave a source marked `active` solely because a generated Markdown page still links to it. Update the canonical YAML and let CI expose the resulting drift.

## Provenance contract

Every `active` resource has:

```yaml
provenance:
  source_type: official-project
  last_verified: 2026-09-26
  review_interval_days: 180
```

`last_verified` is the last catalog review date. It does not mean “published on” or “guaranteed current until”.

Suggested defaults are:

| Resource type | Review interval |
|---|---:|
| Book / course | 365 days |
| Documentation / software / standard / dataset | 180 days |
| Policy / regulatory guidance | 90 days |

A maintainer can choose a different interval when the source has a clear reason to change faster or slower.

## Review workflow

1. Inspect the source at the stored URL and confirm that its identity and scope still match the catalog entry.
2. Check whether the source has a canonical replacement, current edition, current specification or maintained documentation page.
3. Reassess the learner-facing `why_useful` and `does_not_cover` fields.
4. Update `last_verified` and the review interval when the entry remains active.
5. Otherwise move it to `needs-review`, `deprecated`, `broken-link` or `archived` and remove it from current learning paths.
6. Run the full validation suite.

For scientific corrections, also verify the associated paper, standard or institutional source rather than editing a claim based only on a secondary summary.

## Automated gates

Pull requests and pushes run structural validation, strict provenance checks and repository tests.

The monthly scheduled job additionally runs the external URL checker. URL failures are reported as warnings because transient network failures are possible; the underlying resource should still be reviewed and its status updated when a link is genuinely broken.

## Why this is intentionally strict

The goal is not to create a large catalog. The goal is to keep the current catalog small enough that its pedagogical relevance, provenance and maintenance state can be defended.
