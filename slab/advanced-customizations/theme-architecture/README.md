# Theme architecture

Slab follows [standard Shopify theme architecture](https://shopify.dev/docs/storefronts/themes/architecture) with one addition: a `src/` folder that holds source files compiled into the theme at build time.

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



{% content-ref url="styling.md" %}
[styling.md](styling.md)
{% endcontent-ref %}

{% content-ref url="javascript.md" %}
[javascript.md](javascript.md)
{% endcontent-ref %}

{% content-ref url="naming-conventions.md" %}
[naming-conventions.md](naming-conventions.md)
{% endcontent-ref %}
