# Neurotech Atlas

Neurotech Atlas is the presentation layer for the public `neurotech-roadmaps` knowledge base.

## Product intent

The repository remains the source of truth. The app does not copy or redefine scientific content; it exposes the existing model as a navigable interface:

- **Overview** — orientation, counts and destination discovery.
- **Roadmaps** — goal-driven learning paths.
- **Capability graph** — reusable capability families and prerequisite-oriented navigation.
- **Projects** — evidence-producing work grouped by depth.
- **Papers** — structured paper-reading guides.
- **Library** — direct access to nodes, roadmaps, projects, resources and methodological/safety documents.

## Design constraints

The MVP follows the repository's existing principles: capability-first rather than link-first; YAML remains canonical where the repository says it is canonical; generated Markdown remains source-owned; scientific claims are not invented by the UI; safety boundaries remain visible; public-source links open canonical GitHub content; and no clinical, invasive or stimulation procedure is introduced by the app.

## Run locally

This MVP is dependency-free and static. Serve the repository root with any static HTTP server and open `app/index.html`.

For example:

    python -m http.server 8000

Then open `http://localhost:8000/app/`.

The app uses browser APIs and localStorage for future client-side progress state, plus links to the public GitHub repository.