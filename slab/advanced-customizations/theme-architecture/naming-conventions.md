# Naming conventions

Files follow a prefix system across all three component layers:



## Snippets&#x20;

| Prefix       | Purpose                                           |
| ------------ | ------------------------------------------------- |
| `c__`        | Reusable UI component rendered via `{% render %}` |
| `g__`        | Generative/grouped component                      |
| `theme__`    | Core theme infrastructure (scripts, styles, meta) |
| `template__` | Snippets tied to a specific template context      |



## Blocks

| Prefix      | Purpose                                                                |
| ----------- | ---------------------------------------------------------------------- |
| `g__`       | Grouped block — accepts nested blocks via `{% content_for 'blocks' %}` |
| `_`         | Private block — only valid inside a specific parent                    |
| `layout__`  | Structural layout container                                            |
| `overlay__` | Overlay block (drawer, popup, sidebar)                                 |



## Sections

| Prefix    | Purpose                                                              |
| --------- | -------------------------------------------------------------------- |
| `main__`  | Template-specific main content (e.g., `main__collection.liquid`)     |
| `theme__` | Global sections used across all pages (e.g., `theme__header.liquid`) |
