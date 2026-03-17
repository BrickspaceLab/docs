# Use colors and schemes

Slab color styling starts in **Theme settings > Colors**. Merchants pick a small set of global colors, then Slab generates additional color tokens (such as accents, shades, neutral, and plain) that sections and blocks can use through color scheme settings.

This guide is based on Slab source code in:

- `.temp/slab/config/settings_schema.json`
- `.temp/slab/config/settings_data.json`
- `.temp/slab/locales/en.default.schema.json`
- `.temp/slab/snippets/theme__styles.liquid`
- `.temp/slab/sections/main__collection.liquid`



## What each global color setting does

These are the global color settings in **Theme settings > Colors**.

### Body

| Editor label | Setting ID | What it controls | Default preset value |
| --- | --- | --- | --- |
| Background | `color_body_background` | Main storefront background and base for generated overlays/shades/borders. | `#ffffff` |
| Foreground | `color_body_foreground` | Default text and default border color. | `#000000` |
| Alternative foreground | `color_body_foreground_alt` | Alternative text tone (`--color__text-alt`). | `#ffffff` |



### Primary

| Editor label | Setting ID | What it controls | Default preset value |
| --- | --- | --- | --- |
| Background | `color_primary_background` | Primary surface color. | `#a61313` |
| Foreground | `color_primary_foreground` | Text/icon color on primary surfaces. | `#ffffff` |
| Border | `color_primary_border` | Border color for primary surfaces. | `#a61313` |
| Hover background | `color_primary_background_hover` | Hover background for primary buttons/surfaces. | `#611414` |
| Hover foreground | `color_primary_foreground_hover` | Hover text/icon color on primary surfaces. | `#ffffff` |
| Hover border | `color_primary_border_hover` | Hover border color on primary surfaces. | `#611414` |



### Secondary

| Editor label | Setting ID | What it controls | Default preset value |
| --- | --- | --- | --- |
| Background | `color_secondary_background` | Secondary surface color. | `#000000` |
| Foreground | `color_secondary_foreground` | Text/icon color on secondary surfaces. | `#ffffff` |
| Border | `color_secondary_border` | Border color for secondary surfaces. | `#000000` |
| Hover background | `color_secondary_background_hover` | Hover background for secondary buttons/surfaces. | `#ffffff` |
| Hover foreground | `color_secondary_foreground_hover` | Hover text/icon color on secondary surfaces. | `#000000` |
| Hover border | `color_secondary_border_hover` | Hover border color on secondary surfaces. | `#000000` |



### Tertiary

| Editor label | Setting ID | What it controls | Default preset value |
| --- | --- | --- | --- |
| Background | `color_tertiary_background` | Tertiary surface color. | `#f6eadf` |
| Foreground | `color_tertiary_foreground` | Text/icon color on tertiary surfaces. | `#000000` |
| Border | `color_tertiary_border` | Border color for tertiary surfaces. | `#f6eadf` |
| Hover background | `color_tertiary_background_hover` | Hover background for tertiary buttons/surfaces. | `#c9beb4` |
| Hover foreground | `color_tertiary_foreground_hover` | Hover text/icon color on tertiary surfaces. | `#000000` |
| Hover border | `color_tertiary_border_hover` | Hover border color on tertiary surfaces. | `#c9beb4` |



### Additional colors and text links

| Editor label | Setting ID | What it controls | Default preset value |
| --- | --- | --- | --- |
| Error | `color_error` | Error surfaces and text utility color. | Theme default (no explicit schema default) |
| Success | `color_success` | Success surfaces and text utility color. | Theme default (no explicit schema default) |
| Mobile bar color | `color_mobile_bar` | Mobile browser theme color/meta color. | `#a61313` |
| Background overlay | `color_overlay_background` | Overlay gradient/background setting used by overlay UI. | `linear-gradient(0deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.2) 100%)` |
| Links | `color_links` | Link text color token (`--color__text-link`). | `var(--color__text-default)` |



### Input state colors (global)

These settings are in **Theme settings > Inputs**, but they are global color tokens and feed directly into `--input__*` variables used across the storefront.

| Editor label | Setting ID | What it controls | Schema default |
| --- | --- | --- | --- |
| Background (Default colors) | `input_default_color_background` | Input default background token. | `var(--color__background-body)` |
| Border (Default colors) | `input_default_color_border` | Input default border token. | `transparent` |
| Background (Hover colors) | `input_hover_color_background` | Input hover background token. | `var(--color__background-body)` |
| Border (Hover colors) | `input_hover_color_border` | Input hover border token. | `transparent` |
| Background (Focus colors) | `input_focus_color_background` | Input focus background token. | `var(--color__background-body)` |
| Border (Focus colors) | `input_focus_color_border` | Input focus border token. | `var(--color__border-primary)` |



## How generated colors are created

Slab computes many color tokens in `theme__styles.liquid` from the global settings above.

### Accent, shade, neutral, plain, and related tokens

- **Accent 1/2/3** in section and block scheme pickers map to overlay tokens: `--color__background-overlay-1/2/3`.
- **Shade 1/2/3** map to `--color__background-shade-1/2/3`.
- **Main** maps to the primary color family in Slab (`--color__background-primary`, `--color__foreground-primary`, and related hover/border tokens).
- **Plain** maps to `--color__background-plain` and `--color__background-plain-shade`.
- **Neutral** maps to `--color__background-neutral` and `--color__background-neutral-shade`.

### Generation logic

- **Overlays, shades, unshades, and divider/selected borders** are derived from the body background brightness:
  - If body is light, Slab darkens for overlays/shades and lightens for unshades.
  - If body is dark, Slab lightens for overlays/shades and darkens for unshades.
- **Neutral** is derived from body + primary mix and then receives a derived shade.
- **Plain** is a translucent version of the body background and gets a derived shade.
- **Primary, secondary, and tertiary shade tokens** are generated by darkening or lightening each background based on brightness.



## How to create and use schemes in section or block schemas

In Slab, schemes are created by adding a `select` setting (typically `color_scheme`) to a section or block schema. Each option returns utility classes that are applied directly to the rendered element.

Example from `main__collection.liquid` schema:

```json
{
  "type": "select",
  "id": "color_scheme",
  "label": "t:general.settings.color_scheme.label",
  "options": [
    { "value": "color__bg-body color__default", "label": "t:general.settings.color_scheme.body.label" },
    { "value": "color__bg-neutral color__default", "label": "t:general.settings.color_scheme.neutral.label" },
    { "value": "color__bg-overlay-1 color__default", "label": "t:general.settings.color_scheme.accent_1.label" },
    { "value": "color__bg-overlay-2 color__default", "label": "t:general.settings.color_scheme.accent_2.label" },
    { "value": "color__bg-overlay-3 color__default", "label": "t:general.settings.color_scheme.accent_3.label" },
    { "value": "color__bg-shade-1 color__default", "label": "t:general.settings.color_scheme.shade_1.label" },
    { "value": "color__bg-shade-2 color__default", "label": "t:general.settings.color_scheme.shade_2.label" },
    { "value": "color__bg-shade-3 color__default", "label": "t:general.settings.color_scheme.shade_3.label" },
    { "value": "color__bg-primary color__primary", "label": "t:general.settings.color_scheme.primary.label" },
    { "value": "color__bg-secondary color__secondary", "label": "t:general.settings.color_scheme.secondary.label" },
    { "value": "color__bg-tertiary color__tertiary", "label": "t:general.settings.color_scheme.tertiary.label" },
    { "value": "bg-transparent", "label": "t:general.settings.color_scheme.transparent.label" }
  ],
  "default": "color__bg-body color__default"
}
```

To apply the selected scheme:

```liquid
<section class="{{ section.settings.color_scheme }}">
  {% content_for 'blocks' %}
</section>
```

The same pattern applies to blocks:

- Define a block `select` setting (for example `id: "color_scheme"`).
- Add the selected classes to the block wrapper (for example `class="{{ block.settings.color_scheme }}"`).



## Common scheme and border options

These labels come from `en.default.schema.json`:

- **Scheme options:** Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Transparent.
- **Border options:** Body, Subtle, Strong, Primary, Secondary, Tertiary, None.

For border selectors, Slab commonly maps these to:

- Body -> `color__border-light`
- Subtle -> `color__border-divider-1`
- Strong -> `color__border-selected-1`
- Primary -> `color__border-primary`
- Secondary -> `color__border-secondary`
- Tertiary -> `color__border-tertiary`
- None -> `border-0!`
