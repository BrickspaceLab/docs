# Understanding theme code

## Project structure

```
slab/
├── assets/           # Compiled JS/CSS output (do not edit directly)
├── blocks/           # Theme block files
├── config/           # Global theme settings schema
├── layout/           # theme.liquid and other layout files
├── locales/          # Translation files
├── sections/         # Compiled section files (do not edit directly)
├── snippets/         # Reusable Liquid snippets
├── src/
│   ├── scripts/      # Build scripts (section-builder, icon snippets)
│   ├── sections/     # Section source files and preset JSON
│   └── entrypoints/  # Vite JS/CSS entry points
└── templates/        # JSON templates
```

* `src/entrypoints/` — JavaScript and CSS entry points compiled by Vite. Add new global scripts or styles here.
* `src/sections/` — Section preset JSON source files. The section watcher compiles these into `sections/` automatically.



## Styling

Slab uses Tailwind CSS v4. Most styling is done with utility classes directly in Liquid files.

Colors use a CSS custom property system. See `.cursor/rules/colors.mdc` for the full color architecture.



## JavaScript

Interactivity is handled by Alpine.js. Components are defined inline in Liquid templates with `x-data`.

For shared logic or heavier components, add modules to `src/entrypoints/` and import them. See `.cursor/rules/alpine.mdc` and `.cursor/rules/javascript.mdc` for conventions.



## Naming conventions

Files follow a prefix system across all three component layers:

#### Snippets (`snippets/*.liquid`)

| Prefix       | Purpose                                           |
| ------------ | ------------------------------------------------- |
| `c__`        | Reusable UI component rendered via `{% render %}` |
| `g__`        | Generative/grouped component                      |
| `theme__`    | Core theme infrastructure (scripts, styles, meta) |
| `template__` | Snippets tied to a specific template context      |

#### Blocks (`blocks/*.liquid`)

| Prefix      | Purpose                                                                |
| ----------- | ---------------------------------------------------------------------- |
| `g__`       | Grouped block — accepts nested blocks via `{% content_for 'blocks' %}` |
| `_`         | Private block — only valid inside a specific parent                    |
| `layout__`  | Structural layout container                                            |
| `overlay__` | Overlay block (drawer, popup, sidebar)                                 |

#### Sections (`sections/*.liquid`)

| Prefix    | Purpose                                                              |
| --------- | -------------------------------------------------------------------- |
| `main__`  | Template-specific main content (e.g., `main__collection.liquid`)     |
| `theme__` | Global sections used across all pages (e.g., `theme__header.liquid`) |
