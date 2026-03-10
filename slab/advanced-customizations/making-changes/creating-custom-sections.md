# Creating custom sections

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../support/hire-a-shopify-developer.md).
{% endhint %}

### What is a section?

A section is a full-width content area that merchants can add to any page template from the theme editor. Sections act as containers — they hold blocks, control the overall layout, and expose their own settings for things like spacing, background color, and visibility.

Every page in a Slab-powered store is built from sections stacked vertically. The built-in `Section` type covers most layouts, but custom sections let you build entirely new content areas with their own block types and configuration options.

### When to create a custom section

Sections are the right choice when you need:

- A standalone content area with a distinct layout not covered by the built-in `Section` type.
- A set of blocks that only make sense within a specific container (e.g. a pricing table where each column is a block with a price, feature list, and call-to-action).
- Section-level settings that control the container as a whole (background media, column count, spacing).

If you only need a small piece of dynamic or interactive content within an existing section, [custom liquid](using-custom-liquid.md) or a [custom block](creating-custom-blocks.md) is simpler.

### How sections are structured

A section file lives in the `sections/` folder (compiled from `src/sections/` if you are using the development toolkit) and follows this pattern:

- Liquid markup with `{{ section.shopify_attributes }}` on the root element (required for the theme editor)
- Blocks rendered via `{% content_for 'blocks' %}` inside the layout
- `{% schema %}` — JSON defining the section's name, accepted block types, settings, and presets

Accepted block types are declared in the schema's `"blocks"` array. Use `{ "type": "@theme" }` to accept all theme blocks, `{ "type": "@app" }` for app blocks, or list specific block types to restrict what merchants can add.

### Generating a custom section with AI

The Slab repo includes the `shopify-liquid-themes` agent skill, which knows the full section structure, schema conventions, and Slab's Tailwind and Alpine.js patterns. Open your coding agent (e.g. Cursor) in the Slab repo and prompt:

> Using the `shopify-liquid-themes` skill, create a new section called `[your section name]`. It should \[describe the layout and what it contains, e.g. "display a two-column layout with a heading and body text on the left and an image on the right, with settings for spacing and background color"].

The agent will generate a complete section file with correct schema JSON, Tailwind utility classes, and `{% content_for 'blocks' %}` for the dynamic block area.

**Example — a testimonials section with configurable quote blocks:**

> Using the `shopify-liquid-themes` skill, create a new section called `testimonials`. It should display a heading above a grid of quote blocks. Include a setting for the number of columns (2, 3, or 4). Accept only a custom `testimonial` block type that has settings for the quote text, author name, and author title.

Once the file is generated, place it in the `sections/` folder. The section will appear in the theme editor's **Add section** picker under its preset category.
