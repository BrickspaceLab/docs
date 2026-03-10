# Styling

Slab uses Tailwind CSS v4. Most styling is done with utility classes directly in Liquid files. This document covers all the ways CSS is applied and when to use each approach.



## How CSS is applied

There are five places styling can live:

| **Tailwind utility classes** | Inline in `.liquid` files                          | Layout, spacing, sizing, and anything Tailwind covers natively                                       |
| ---------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **`src/css/utilities/`**     | Inline in `.liquid` files                          | Theme-aware typography, colors, animations, and other utilities that pull from CSS custom properties |
| **`src/css/components/`**    | Imported globally via `src/entrypoints/styles.css` | Cross-cutting styles reused across many files that cannot be a single utility class                  |
| **`src/css/base/`**          | Imported globally via `src/entrypoints/styles.css` | Opinionated resets and defaults for bare HTML elements                                               |
| **`{% stylesheet %}` tag**   | Inside a section, block, or snippet file           | Scoped styles tied to a single component where no utility class exists                               |



#### When to use each

Use this as a decision guide — work through it top to bottom:

1. **Does an existing `src/css/utilities/` class cover it?** Use that class. These are theme-aware and pull from CSS custom properties, so they automatically adapt to merchant settings. See [Utility classes](utility-classes/README.md).
2. **Does Tailwind cover it?** Use a Tailwind utility class. Applies to layout, spacing, flexbox, grid, sizing, and most visual properties not tied to theme settings.
3. **Is this style scoped to a single section, block, or snippet and can't be expressed as a utility class?** Add it in a `{% stylesheet %}` tag inside that file. See `.cursor/rules/css.mdc`.
4. **Is this a component style shared across many files that cannot be a single utility class?** Add it to `src/css/components/`.
5. **Are you resetting or styling a bare HTML element globally?** Add it to `src/css/base/`. Do not add component styles here.
6. **Do you need to register a new CSS custom property or author a new reusable `@utility` rule?** Add it to `src/css/utilities/`.



{% content-ref url="utility-classes/" %}
[utility-classes/](utility-classes/)
{% endcontent-ref %}
