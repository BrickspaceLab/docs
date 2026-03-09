# Styling

Slab uses Tailwind CSS v4. Most styling is done with utility classes directly in Liquid files.

## Custom CSS layers

Custom CSS lives in `src/css/` and is organized into three layers, each imported by `src/entrypoints/styles.css`:

| Layer         | Path                  | Purpose                                                                                                                                                            |
| ------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `utilities/`  | `src/css/utilities/`  | Custom Tailwind utility classes and CSS custom properties (colors, typography, animation, borders, spacing, scrollbar, Shopify-specific helpers, vendor overrides) |
| `base/`       | `src/css/base/`       | Opinionated element defaults (colors, typography, forms, tables, media). Injected into the `components` cascade layer so Tailwind utilities win.                   |
| `components/` | `src/css/components/` | Standalone component styles that Tailwind alone cannot express (buttons, containers, header, gallery)                                                              |

**When to use each:**

* **Tailwind utility classes** — reach for these first. Most layout, spacing, color, and typography needs can be covered with utilities in your Liquid.
* **`{% stylesheet %}` tag** — for scoped styles tied to a single section, block, or snippet where a utility class does not exist or a component selector is required. See `.cursor/rules/css.mdc`.
* **`src/css/components/`** — for cross-cutting component styles reused across many files that cannot be expressed as a single utility class.
* **`src/css/base/`** — only for resetting or styling bare HTML elements globally. Avoid adding component styles here.
* **`src/css/utilities/`** — for registering new CSS custom properties or authoring custom `@utility` rules that extend Tailwind's utility layer.
