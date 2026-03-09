# Understanding theme code

### File structure

* **`src/entrypoints/`** — JavaScript and CSS entry points compiled by Vite. Add new global scripts or styles here.
* **`src/sections/`** — Section preset JSON source files. The section watcher compiles these into `sections/` automatically.
* **`snippets/`** — Liquid partials shared across sections and templates. Follow the naming conventions in `.cursor/rules/snippets.mdc`.

```
slab/
├── assets/           # Compiled JS/CSS output (do not edit directly)
├── config/           # Theme settings schema
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



### Styling

Slab uses Tailwind CSS v4. Most styling is done with utility classes directly in Liquid files.

For custom CSS that Tailwind cannot handle, use the `{% stylesheet %}` tag within a section or snippet file. See `.cursor/rules/css.mdc` for conventions.

Colors use a CSS custom property system. See `.cursor/rules/colors.mdc` for the full color architecture.



### JavaScript

Interactivity is handled by [Alpine.js](https://alpinejs.dev/). Components are defined inline in Liquid templates with `x-data`.

For shared logic or heavier components, add modules to `src/entrypoints/` and import them. See `.cursor/rules/alpine.mdc` and `.cursor/rules/javascript.mdc` for conventions.



### Naming conventions

| Prefix         | Usage                                                     |
| -------------- | --------------------------------------------------------- |
| `components__` | Reusable snippets used across multiple sections           |
| `theme__`      | Snippets used only in `theme.liquid` (global, every page) |
| `header__`     | Snippets scoped to the header                             |
| `product__`    | Snippets used only on product templates                   |
| `collection__` | Snippets used only on collection templates                |
| `article__`    | Snippets used only on article templates                   |

Section files follow the same prefix pattern. For example, `collection__banner.liquid` is only used in the collection template.
