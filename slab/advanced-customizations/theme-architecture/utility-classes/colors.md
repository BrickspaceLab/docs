# Colors

`src/css/utilities/colors.css`

Use these instead of hardcoding hex values or raw `color` / `background-color` declarations:

| Prefix       | Example                                         | Purpose                                               |
| ------------ | ----------------------------------------------- | ----------------------------------------------------- |
| `color-bg__` | `color-bg__body-bg`, `color-bg__scheme-bg`      | Background colors                                     |
| `color-tx__` | `color-tx__text-default`, `color-tx__scheme-fg` | Text colors                                           |
| `color-br__` | `color-br__divider-1`, `color-br__scheme-br`    | Border colors                                         |
| `color-ol__` | `color-ol__selected-1`                          | Outline colors                                        |
| `color-bt__` | `color-bt__main`, `color-bt__scheme`            | Button background + text + border (with hover states) |

Scheme-aware variants (`color-bg__scheme-bg`, `color-tx__scheme-fg`, etc.) automatically reflect the color scheme set on the nearest parent section or block — prefer these over body-level utilities inside themed sections.



## How it works

Colors are never written as raw hex values. Everything flows through CSS custom properties so that merchant-configurable theme settings propagate automatically to every component.

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

## Global CSS variables

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

## Color schemes

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

## Color utility class reference

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

## Common patterns

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

## Do / Don't

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
