# Use colors and schemes

Slab color styling starts in **Theme settings > Colors**. Merchants pick a small set of global colors, then Slab generates additional color tokens (such as accents, shades, neutral, and plain) that sections and blocks can use through color scheme settings.

## What each global color setting does

Use this section to understand what each setting group controls in **Theme settings > Colors**.

### Body

These settings define your store's base color system.

- **Background** (`color_body_background`): Main storefront background and the base color used to generate overlays, shades, and divider tokens.
- **Foreground** (`color_body_foreground`): Default text color and default border color.
- **Alternative foreground** (`color_body_foreground_alt`): Alternative text tone used by `--color__text-alt`.
- **Default Slab preset values:** Background `#ffffff`, Foreground `#000000`, Alternative foreground `#ffffff`.


### Primary

Primary colors are your main emphasis colors for surfaces and buttons.

- **Background** (`color_primary_background`): Primary surface color.
- **Foreground** (`color_primary_foreground`): Text and icon color on primary surfaces.
- **Border** (`color_primary_border`): Border color for primary elements.
- **Hover background** (`color_primary_background_hover`): Hover background for primary interactive elements.
- **Hover foreground** (`color_primary_foreground_hover`): Hover text/icon color.
- **Hover border** (`color_primary_border_hover`): Hover border color.
- **Default Slab preset values:** Background `#a61313`, Foreground `#ffffff`, Border `#a61313`, Hover background `#611414`, Hover foreground `#ffffff`, Hover border `#611414`.


### Secondary

Secondary colors provide a second branded contrast style.

- **Background** (`color_secondary_background`): Secondary surface color.
- **Foreground** (`color_secondary_foreground`): Text and icon color on secondary surfaces.
- **Border** (`color_secondary_border`): Border color for secondary elements.
- **Hover background** (`color_secondary_background_hover`): Hover background for secondary interactive elements.
- **Hover foreground** (`color_secondary_foreground_hover`): Hover text/icon color.
- **Hover border** (`color_secondary_border_hover`): Hover border color.
- **Default Slab preset values:** Background `#000000`, Foreground `#ffffff`, Border `#000000`, Hover background `#ffffff`, Hover foreground `#000000`, Hover border `#000000`.


### Tertiary

Tertiary colors are an additional brand surface style, often softer or more decorative.

- **Background** (`color_tertiary_background`): Tertiary surface color.
- **Foreground** (`color_tertiary_foreground`): Text and icon color on tertiary surfaces.
- **Border** (`color_tertiary_border`): Border color for tertiary elements.
- **Hover background** (`color_tertiary_background_hover`): Hover background for tertiary interactive elements.
- **Hover foreground** (`color_tertiary_foreground_hover`): Hover text/icon color.
- **Hover border** (`color_tertiary_border_hover`): Hover border color.
- **Default Slab preset values:** Background `#f6eadf`, Foreground `#000000`, Border `#f6eadf`, Hover background `#c9beb4`, Hover foreground `#000000`, Hover border `#c9beb4`.


### Additional colors and text links

These settings control utility and supporting colors.

- **Error** (`color_error`): Error surface and error text color token.
- **Success** (`color_success`): Success surface and success text color token.
- **Mobile bar color** (`color_mobile_bar`): Mobile browser theme color/meta color.
- **Background overlay** (`color_overlay_background`): Default overlay gradient/background.
- **Links** (`color_links`): Link text color token (`--color__text-link`).
- **Default Slab preset values:** Mobile bar `#a61313`, Links `var(--color__text-default)`, Background overlay `linear-gradient(0deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.2) 100%)`.


### Input state colors (global)

These settings are in **Theme settings > Inputs**, but they feed global color tokens used across the storefront.

- **Background (Default colors)** (`input_default_color_background`): Default input background token.
- **Border (Default colors)** (`input_default_color_border`): Default input border token.
- **Background (Hover colors)** (`input_hover_color_background`): Hover input background token.
- **Border (Hover colors)** (`input_hover_color_border`): Hover input border token.
- **Background (Focus colors)** (`input_focus_color_background`): Focus input background token.
- **Border (Focus colors)** (`input_focus_color_border`): Focus input border token.
- **Schema defaults:** Default background `var(--color__background-body)`, default border `transparent`, hover background `var(--color__background-body)`, hover border `transparent`, focus background `var(--color__background-body)`, focus border `var(--color__border-primary)`.



## How generated colors are created

Slab computes many color tokens in `theme__styles.liquid` from the global settings above.

### Accent, shade, neutral, plain, and related tokens

- **Accent 1/2/3** map to overlay background tokens (`--color__background-overlay-1/2/3`).
- **Shade 1/2/3** map to shade background tokens (`--color__background-shade-1/2/3`).
- **Main** maps to Slab's primary family (`--color__background-primary`, `--color__foreground-primary`, plus hover and border variants).
- **Plain** maps to `--color__background-plain` and `--color__background-plain-shade`.
- **Neutral** maps to `--color__background-neutral` and `--color__background-neutral-shade`.

### Generation logic

- **Overlays, shades, unshades, and divider/selected borders** are derived from the body background brightness:
  - If body is light, Slab darkens for overlays/shades and lightens for unshades.
  - If body is dark, Slab lightens for overlays/shades and darkens for unshades.
- **Neutral** is derived from body + primary mix and then receives a derived shade.
- **Plain** is a translucent version of the body background and gets a derived shade.
- **Primary, secondary, and tertiary shade tokens** are generated by darkening or lightening each background based on brightness.



## How to set up and use schemes

In most Slab workflows, you use schemes directly in the theme editor. You do not need to write code to switch between Body, Accent, Shade, Primary, Secondary, or Tertiary styles.

1. Open the section or block you are editing in the theme editor.
2. Find the **Scheme** setting (sometimes labeled as color scheme in certain blocks).
3. Select the style you want, such as **Body**, **Accent 1**, **Shade 2**, **Primary**, or **Transparent**.
4. If needed, set the matching **Border** style so the outline contrast fits the selected scheme.
5. Repeat for each section or block to build consistent visual hierarchy across the storefront.

### Suggested setup order

- Set your global colors first in **Theme settings > Colors**.
- Apply section-level schemes next for major background areas.
- Apply block-level schemes after that for cards, overlays, and calls to action.
- Use **Primary**, **Secondary**, and **Tertiary** for intentional emphasis.
- Use **Accent** and **Shade** options for softer contrast and layering.
- Use **Transparent** when you want the parent area to show through.

### For custom development

If you are building custom sections or blocks, follow the same pattern Slab uses in source: add a `color_scheme` select setting in schema, then apply `{{ section.settings.color_scheme }}` or `{{ block.settings.color_scheme }}` on the wrapper element.



## Common scheme and border options

These labels come from `en.default.schema.json`:

- **Scheme options:** Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Transparent.
- **Border options:** Body, Subtle, Strong, Primary, Secondary, Tertiary, None.

For border selectors, Slab commonly maps these options to utility classes:

- Body -> `color__border-light`
- Subtle -> `color__border-divider-1`
- Strong -> `color__border-selected-1`
- Primary -> `color__border-primary`
- Secondary -> `color__border-secondary`
- Tertiary -> `color__border-tertiary`
- None -> `border-0!`
