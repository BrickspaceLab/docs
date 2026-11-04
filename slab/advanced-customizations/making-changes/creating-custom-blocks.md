# Create custom blocks

## What is a block?

A block is a configurable, reusable content unit that merchants can add, remove, and reorder inside sections from the theme editor. Blocks have a `{% schema %}` that defines their settings — things like text fields, image pickers, color selectors, and toggles — which appear in the editor's sidebar whenever a block is selected.

Slab includes 60+ built-in blocks covering most common use cases. Custom blocks let you extend this library with components tailored to your store.



## Block vs custom liquid

|                          | Custom block                        | Custom liquid            |
| ------------------------ | ----------------------------------- | ------------------------ |
| Editable in theme editor | Yes                                 | No                       |
| Reusable across sections | Yes                                 | No                       |
| Merchant-facing settings | Yes                                 | No                       |
| Best for                 | Repeatable, configurable components | One-off dynamic snippets |

If the content only needs to appear in one place and does not need merchant-facing controls, [custom liquid](using-custom-liquid.md) is simpler. Use a custom block when you need the content to be editable, have configuration options, or be reusable across multiple sections.



## How blocks are structured

A block file lives in the `blocks/` folder and follows this pattern:

* `{% doc %}` — LiquidDoc header describing the block's purpose
* HTML markup using `block.settings.*` for dynamic values
* `{{ block.shopify_attributes }}` on the root element (required for the theme editor to work)
* Optional `{% stylesheet %}` for scoped styles
* `{% schema %}` — JSON defining the block's name, settings, and presets



## Generating a custom block with AI

The Slab repo includes the `shopify-liquid-themes` agent skill, which knows the full block structure, all Shopify schema setting types, and Slab's naming conventions. Open your coding agent (e.g. Cursor) in the Slab repo and prompt:

{% code overflow="wrap" %}
```
Using the shopify-liquid-themes skill, create a new block called [your block name]. It should [describe what the block displays and any settings it needs, e.g. "display a testimonial quote with a name, title, and star rating that merchants can configure"].
```
{% endcode %}

The agent will generate a complete block file with correct schema JSON, `{% doc %}` header, translation keys, and Tailwind utility classes.

**Example — a notice block with an icon and a message:**

{% code overflow="wrap" %}
```
Using the shopify-liquid-themes skill, create a new block called notice. It should display a short message alongside an icon. Include settings for the message text, an icon selector (choosing from the theme's built-in icon set), and a color scheme selector.
```
{% endcode %}

Once the file is generated, place it in the `blocks/` folder. The block will appear in the theme editor's block picker for any section that accepts `@theme` blocks.
