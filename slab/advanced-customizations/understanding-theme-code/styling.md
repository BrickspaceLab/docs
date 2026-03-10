# Styling

Slab uses Tailwind CSS v4. Most styling is done with utility classes directly in Liquid files. This document covers all the ways CSS is applied, when to use each approach, the custom utility classes available in `src/css/`, and the full color system.



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

1. **Does an existing `src/css/utilities/` class cover it?** Use that class. These are theme-aware and pull from CSS custom properties, so they automatically adapt to merchant settings. See Custom utility classes below.
2. **Does Tailwind cover it?** Use a Tailwind utility class. Applies to layout, spacing, flexbox, grid, sizing, and most visual properties not tied to theme settings.
3. **Is this style scoped to a single section, block, or snippet and can't be expressed as a utility class?** Add it in a `{% stylesheet %}` tag inside that file. See `.cursor/rules/css.mdc`.
4. **Is this a component style shared across many files that cannot be a single utility class?** Add it to `src/css/components/`.
5. **Are you resetting or styling a bare HTML element globally?** Add it to `src/css/base/`. Do not add component styles here.
6. **Do you need to register a new CSS custom property or author a new reusable `@utility` rule?** Add it to `src/css/utilities/`.



## Custom utility classes

The `src/css/utilities/` directory contains theme-aware utility classes that must be used in place of hardcoded values for typography and color. These classes read CSS custom properties set from merchant theme settings, so they adapt automatically to color schemes and font selections.

#### Typography — `src/css/utilities/typography.css`

Use these instead of hardcoding font families, weights, or sizes:

| Class                                                                         | Purpose                                          |
| ----------------------------------------------------------------------------- | ------------------------------------------------ |
| `type__body`                                                                  | Body font family, weight, style, and line-height |
| `type__heading`                                                               | Default heading font family, weight, and style   |
| `type__subheading`                                                            | Subheading font family, weight, and style        |
| `type__accent`                                                                | Accent font family, weight, and style            |
| `type__button-style`                                                          | Button font family, weight, and capitalization   |
| `type__button-size`                                                           | Button line-height and letter-spacing            |
| `type__heading-1-style` / `type__heading-1-size`                              | H1 font + size (repeat for 2–6)                  |
| `type--smaller` / `type--small` / `type--base` / `type--big` / `type--bigger` | Theme-relative font sizes                        |

#### Color — `src/css/utilities/colors.css`

Use these instead of hardcoding hex values or raw `color` / `background-color` declarations:

| Prefix       | Example                                         | Purpose                                               |
| ------------ | ----------------------------------------------- | ----------------------------------------------------- |
| `color-bg__` | `color-bg__body-bg`, `color-bg__scheme-bg`      | Background colors                                     |
| `color-tx__` | `color-tx__text-default`, `color-tx__scheme-fg` | Text colors                                           |
| `color-br__` | `color-br__divider-1`, `color-br__scheme-br`    | Border colors                                         |
| `color-ol__` | `color-ol__selected-1`                          | Outline colors                                        |
| `color-bt__` | `color-bt__main`, `color-bt__scheme`            | Button background + text + border (with hover states) |

Scheme-aware variants (`color-bg__scheme-bg`, `color-tx__scheme-fg`, etc.) automatically reflect the color scheme set on the nearest parent section or block — prefer these over body-level utilities inside themed sections.

See Color utility class reference for the full list.

## Color system

Colors are never written as raw hex values. Everything flows through CSS custom properties so that merchant-configurable theme settings propagate automatically to every component.

#### How it works

There are two layers:

1. **Global CSS variables** — set on `:root` in `snippets/theme__styles.liquid`. These cover the body background, body foreground, auto-calculated shades, overlays, dividers, and input states.
2. **Color scheme classes** — merchant-defined palettes (e.g. `color__primary`, `color__secondary`). Applying one to a container exposes a set of `--scheme__*` variables that any descendant can use.

```
Theme Settings
    └─ snippets/theme__styles.liquid
        ├─ :root { --color__* }          ← global variables
        └─ .color__[id] { --scheme__* }  ← per-scheme variables
                └─ color-bg__*, color-tx__*, color-br__*, color-ol__*, color-bt__*
                        └─ HTML elements
```

**Key files:**

* `snippets/theme__styles.liquid` — all CSS variable definitions
* `src/css/utilities/colors.css` — all utility class definitions
* `config/settings_schema.json` — color scheme configuration

#### Global CSS variables

These are always available on `:root` regardless of scheme context.

**Body colors:**

| Variable                   | Description             |
| -------------------------- | ----------------------- |
| `--color__background-body` | Page background         |
| `--color__foreground-body` | Default text            |
| `--color__text-default`    | Same as foreground-body |
| `--color__text-link`       | Link color              |

**Auto-calculated colors** — derived from body background brightness, adapts on light and dark backgrounds:

| Group    | Variables                           | Use                                                |
| -------- | ----------------------------------- | -------------------------------------------------- |
| Overlays | `--color__background-overlay-1/2/3` | Semi-transparent backgrounds, lightest → darkest   |
| Shades   | `--color__background-shade-1/2/3`   | Darken on light, lighten on dark — subtle → strong |
| Unshades | `--color__background-unshade-1/2/3` | Inverse of shades — subtle → strong                |
| Borders  | `--color__border-divider-1/2/3`     | Divider lines, increasing opacity                  |
| Selected | `--color__border-selected-1/2`      | Selected / active states                           |

**Input states:**

| Variable                                                  | Use           |
| --------------------------------------------------------- | ------------- |
| `--input__default-background` / `--input__default-border` | Default state |
| `--input__hover-background` / `--input__hover-border`     | Hover state   |
| `--input__focus-background` / `--input__focus-border`     | Focus state   |

#### Color schemes

Merchants configure color schemes in the theme editor. Each scheme exposes six variables when its class is applied to a container:

| Variable                     | Description       |
| ---------------------------- | ----------------- |
| `--scheme__background`       | Scheme background |
| `--scheme__foreground`       | Scheme text       |
| `--scheme__border`           | Scheme border     |
| `--scheme__background-hover` | Hover background  |
| `--scheme__foreground-hover` | Hover text        |
| `--scheme__border-hover`     | Hover border      |

**Applying a scheme:**

Add the scheme class to a container. All `color-bg__scheme-*`, `color-tx__scheme-*`, and `color-br__scheme-*` utilities inside will then resolve correctly.

```html
<div class="color__primary">
  <div class="color-bg__scheme-bg color-tx__scheme-fg color-br__scheme-br border">
    Styled with the primary scheme
  </div>
</div>
```

> Do not use `color-bg__scheme-bg` on an element without a parent scheme class — `--scheme__background` will be undefined and the background will be transparent.

**Applying from section settings:**

```liquid
<section class="color__{{ section.settings.color_scheme }} color-bg__scheme-bg color-tx__scheme-fg">
  ...
</section>
```

**Partial overrides** — mix scheme variables by applying modifier classes alongside a base scheme:

```html
<!-- Use primary's foreground/border but secondary's background -->
<div class="color__primary color__secondary--background">
  ...
</div>
```

Available modifiers: `--background`, `--foreground`, `--border`, `--background-hover`, `--foreground-hover`, `--border-hover`.

***

### Color utility class reference

All classes follow this pattern:

```
color-[property]__[source]-[aspect]
```

| Segment    | Values                                                                                          |
| ---------- | ----------------------------------------------------------------------------------------------- |
| `property` | `bg` background · `tx` text · `br` border · `ol` outline · `bt` button                          |
| `source`   | `body` · `scheme` · `shade` · `unshade` · `overlay` · `divider` · `selected` · `input` · `text` |
| `aspect`   | `bg` · `fg` · `br` · `1` / `2` / `3`                                                            |

#### Background — `color-bg__*`

| Class                     | Sets background to                                 |
| ------------------------- | -------------------------------------------------- |
| `color-bg__body-bg`       | Body background                                    |
| `color-bg__body-fg`       | Body foreground (inverted panel)                   |
| `color-bg__text-default`  | Default text color                                 |
| `color-bg__scheme-bg`     | Scheme background _(requires parent scheme class)_ |
| `color-bg__scheme-fg`     | Scheme foreground _(requires parent scheme class)_ |
| `color-bg__overlay-1/2/3` | Semi-transparent overlays                          |
| `color-bg__shade-1/2/3`   | Shade tints                                        |
| `color-bg__unshade-1/2/3` | Unshade tints                                      |
| `color-bg__blur-1/2/3`    | Shade tint + `backdrop-blur-sm`                    |
| `color-bg__unblur-1/2/3`  | Unshade tint + `backdrop-blur-sm`                  |
| `color-bg__error`         | Error state                                        |
| `color-bg__success`       | Success state                                      |
| `color-bg__input`         | Input default background                           |
| `color-bg__input--hover`  | Input hover background                             |
| `color-bg__input--focus`  | Input focus background                             |

```html
<!-- Standard content area -->
<div class="color-bg__body-bg color-tx__text-default">...</div>

<!-- Subtle card tint -->
<div class="color-bg__shade-1">...</div>

<!-- Frosted glass panel -->
<div class="color-bg__blur-2">...</div>

<!-- Scheme-colored banner -->
<div class="color__accent color-bg__scheme-bg color-tx__scheme-fg">...</div>
```

#### Text — `color-tx__*`

| Class                    | Sets text color to                                        |
| ------------------------ | --------------------------------------------------------- |
| `color-tx__text-default` | Default text (also styles `::placeholder` at 75% opacity) |
| `color-tx__text-link`    | Link color                                                |
| `color-tx__body-bg`      | Body background (text on dark surfaces)                   |
| `color-tx__body-fg`      | Body foreground                                           |
| `color-tx__scheme-bg`    | Scheme background _(requires parent scheme class)_        |
| `color-tx__scheme-fg`    | Scheme foreground _(requires parent scheme class)_        |
| `color-tx__shade-1/2/3`  | Shade colors (muted text)                                 |
| `color-tx__error`        | Error text                                                |
| `color-tx__success`      | Success text                                              |

> `color-tx__scheme-fg` and `color-tx__scheme-bg` also set `border-color` on child `input[type="checkbox"]` and `input[type="radio"]` elements.

```html
<!-- Muted caption -->
<p class="color-tx__shade-2 text-sm">Optional description</p>

<!-- Error message -->
<span class="color-tx__error">This field is required</span>
```

#### Border — `color-br__*`

| Class                     | Sets border color to                                     |
| ------------------------- | -------------------------------------------------------- |
| `color-br__body-bg`       | Body background                                          |
| `color-br__body-fg`       | Body foreground                                          |
| `color-br__text-default`  | Default text color                                       |
| `color-br__divider-1/2/3` | Divider lines                                            |
| `color-br__selected-1/2`  | Selected / active state                                  |
| `color-br__scheme-bg`     | Scheme background _(requires parent scheme class)_       |
| `color-br__scheme-fg`     | Scheme foreground _(requires parent scheme class)_       |
| `color-br__scheme-br`     | Scheme border _(requires parent scheme class)_           |
| `color-br__scheme-bghv`   | Scheme background hover _(requires parent scheme class)_ |
| `color-br__scheme-fghv`   | Scheme foreground hover _(requires parent scheme class)_ |
| `color-br__scheme-brhv`   | Scheme border hover _(requires parent scheme class)_     |
| `color-br__input`         | Input default border                                     |
| `color-br__input--hover`  | Input hover border                                       |
| `color-br__input--focus`  | Input focus border                                       |

```html
<!-- Subtle divider line -->
<hr class="border-t color-br__divider-1">

<!-- Selected state ring -->
<div class="border-2 color-br__selected-1">...</div>
```

#### Outline — `color-ol__*`

Primarily used for focus rings.

| Class                   | Sets outline color to    |
| ----------------------- | ------------------------ |
| `color-ol__divider-1`   | Divider color            |
| `color-ol__selected-1`  | Selected state           |
| `color-ol__transparent` | Transparent (hides ring) |
| `color-ol__input`       | Input border color       |

```html
<button class="focus:outline-2 focus:color-ol__selected-1">
  Accessible focus ring
</button>
```

#### Button — `color-bt__*`

Button utilities set background, border, and text color together with `:hover` states in a single class. They also cascade `color` to non-`.reset` children.

| Class                   | Style                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `color-bt__scheme`      | Scheme colors with hover states _(requires parent scheme class)_     |
| `color-bt__main`        | Body-foreground fill, body-background text — high contrast "primary" |
| `color-bt__plain`       | Neutral fill, body foreground text                                   |
| `color-bt__transparent` | Transparent fill, shade hover                                        |
| `color-bt__shade`       | Shade-2 fill, shade-3 hover                                          |
| `color-bt__unshade`     | Unshade-2 fill, unshade-3 hover                                      |

```html
<!-- High-contrast primary action -->
<button class="color-bt__main px-4 py-2 rounded">Buy now</button>

<!-- Scheme-colored CTA inside a themed section -->
<div class="color__secondary">
  <button class="color-bt__scheme px-4 py-2 rounded">Shop now</button>
</div>

<!-- Ghost button -->
<button class="color-bt__transparent px-4 py-2 rounded">Cancel</button>
```

***

### Common patterns

#### Plain content area

```html
<div class="color-bg__body-bg color-tx__text-default">
  Default page content
</div>
```

#### Themed section

```liquid
<section class="color__{{ section.settings.color_scheme }} color-bg__scheme-bg color-tx__scheme-fg">
  <div class="border-t color-br__scheme-br">...</div>
  <button class="color-bt__scheme">...</button>
</section>
```

#### Card with subtle tint

```html
<div class="color-bg__shade-1 color-tx__text-default rounded-lg p-4">
  Card content
</div>
```

#### Input field

```html
<input
  class="color-bg__input color-br__input border color-tx__text-default
         hover:color-bg__input--hover hover:color-br__input--hover
         focus:color-bg__input--focus focus:color-br__input--focus"
  type="text"
/>
```

#### Color type toggle in schema

A common pattern offers merchants a choice between body colors and a custom scheme:

```json
{
  "type": "select",
  "id": "color_type",
  "label": "Color",
  "options": [
    { "value": "body", "label": "Body" },
    { "value": "custom", "label": "Custom" }
  ]
}
```

```liquid
<div
  class="
    {% if block.settings.color_type == 'custom' %}
      color__{{ block.settings.color_scheme }} color-bg__scheme-bg color-tx__scheme-fg
    {% else %}
      color-bg__body-bg color-tx__text-default
    {% endif %}
  "
>
  {{ block.settings.content }}
</div>
```

***

### Do / Don't

**Do not hardcode hex values:**

```liquid
<!-- Bad -->
<div style="background: #ffffff; color: #000000;">

<!-- Good -->
<div class="color-bg__body-bg color-tx__text-default">
```

**Do not use scheme utilities without a parent scheme class:**

```liquid
<!-- Bad — --scheme__background is undefined -->
<div class="color-bg__scheme-bg">...</div>

<!-- Good -->
<div class="color__primary">
  <div class="color-bg__scheme-bg color-tx__scheme-fg">...</div>
</div>
```

**Do not reach for raw Tailwind color classes:**

```liquid
<!-- Bad — bypasses merchant theming -->
<div class="bg-gray-100 text-gray-900">

<!-- Good -->
<div class="color-bg__shade-1 color-tx__text-default">
```

**Do not add component styles to `src/css/base/`:**

```css
/* Bad — base is for bare element resets only */
.product-card { ... }

/* Good — put it in src/css/components/ or a {% stylesheet %} tag */
```

***

### Further reading
