# Colors

`src/css/utilities/colors.css`

Use color utility classes instead of hardcoding hex values or raw `color` / `background-color` declarations.

Scheme-aware variants (`color-bg__scheme-bg`, `color-tx__scheme-fg`, etc.) automatically reflect the color scheme set on the nearest parent section or block — prefer these over body-level utilities inside themed sections.



## How it works

Colors are never written as raw hex values. Everything flows through CSS custom properties so that merchant-configurable theme settings propagate automatically to every component.

There are two layers:

1. **Global CSS variables** — set on `:root` in `snippets/theme__styles.liquid`. These cover the body background, body foreground, auto-calculated shades, overlays, dividers, and input states.
2. **Color scheme classes** — merchant-defined palettes (e.g. `color__primary`, `color__secondary`). Applying one to a container exposes a set of `--scheme__*` variables that any descendant can use.

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

Color schemes can be applied with section or block settings letting merchants select any color scheme to be used.

```liquid
<section class="color__{{ section.settings.color_scheme }} color-bg__scheme-bg color-tx__scheme-fg">
  ...
</section>
```



## Color utility class reference

All classes follow this pattern:

```
color-[property]__[source]-[aspect]
```



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



#### Outline — `color-ol__*`

Primarily used for focus rings.

| Class                   | Sets outline color to    |
| ----------------------- | ------------------------ |
| `color-ol__divider-1`   | Divider color            |
| `color-ol__selected-1`  | Selected state           |
| `color-ol__transparent` | Transparent (hides ring) |
| `color-ol__input`       | Input border color       |



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

