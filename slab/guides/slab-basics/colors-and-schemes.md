# Use colors and schemes

Slab color styling starts in **Theme settings > Colors**. Merchants pick a small set of global colors, then Slab generates additional color tokens (such as accents, shades, neutral, and plain) that sections and blocks can use through color scheme settings.

## What each global color setting does

Use this section to understand what each setting group controls in **Theme settings > Colors**.

### Base

These settings define your store's base color system.

| Setting | What it controls |
| --- | --- |
| Background | Main storefront background and the base used for generated shade/overlay tones. |
| Foreground | Default text color and default border contrast for base surfaces. |


### Schemes

Schemes replace the old primary/secondary/tertiary model.

In **Theme settings > Colors > Schemes**, you can edit **Scheme 1**, **Scheme 2**, and add as many additional schemes as needed.

Each scheme has the same six color fields:

| Setting | How it is applied |
| --- | --- |
| Background | Main background color for any section or block using that scheme. |
| Foreground | Text/icon color used on top of that scheme background. |
| Border | Default border color for elements using that scheme. |
| Hover background | Hover background for buttons and interactive elements in that scheme. |
| Hover foreground | Hover text/icon color for interactive elements in that scheme. |
| Hover border | Hover border color for interactive elements in that scheme. |

Important: editing a scheme updates every section and block that uses that scheme.


### Utility

These settings control utility and supporting colors.

| Setting | What it controls |
| --- | --- |
| Error | Error surfaces and error feedback color. |
| Success | Success surfaces and success feedback color. |
| Mobile bar | Browser UI color on supported mobile browsers. |
| Overlay background | Background shown behind overlays and popups. |


### Input state colors (global)

These settings are in **Theme settings > Inputs**, but they feed global color tokens used across the storefront.

| Setting | What it controls |
| --- | --- |
| Background (Default colors) | Default input background color. |
| Border (Default colors) | Default input border color. |
| Background (Hover colors) | Input background color on hover. |
| Border (Hover colors) | Input border color on hover. |
| Background (Focus colors) | Input background color on focus. |
| Border (Focus colors) | Input border color on focus. |



## How Slab creates color variations

After you choose your global colors, Slab automatically creates extra color variations so sections and blocks stay visually consistent.

### What these generated styles mean

- **Accent 1/2/3:** Layered overlay tones used for depth and emphasis.
- **Shade 1/2/3:** Lighter or darker background steps for subtle contrast.
- **Main:** The main emphasis style for a component, based on the selected scheme's core colors.
- **Plain:** A softer, low-emphasis surface based on the body background.
- **Neutral:** A balanced surface tone that sits between body and brand colors.

### What to expect in your storefront

- If your body background is light, Slab creates darker overlays and shade tones.
- If your body background is dark, Slab creates lighter overlays and shade tones.
- Neutral and plain are auto-generated from your chosen body and brand colors.
- Any section or block using a scheme will inherit that scheme's background, text, border, and hover behavior.

Developer note: these generated values are calculated in `theme__styles.liquid` and exposed as `--color__*` variables used by color utility classes.



## How to set up and use schemes

In most Slab workflows, you use schemes directly in the theme editor. You do not need to write code to switch scheme colors.

1. Open **Theme settings > Colors**.
2. Under **Schemes**, edit **Scheme 1** and **Scheme 2** first.
3. Click **Add Scheme** if you need more brand variations.
4. For each scheme, set all six fields: background, foreground, border, hover background, hover foreground, and hover border.
5. Open the section or block you are editing.
6. Select that scheme in the **Scheme** setting.
7. If available, set a matching **Border** style for better contrast.

### Suggested setup order

- Set your global colors first in **Theme settings > Colors**.
- Set up your core schemes (for example, light, dark, and accent variants).
- Apply section-level schemes next for major background areas.
- Apply block-level schemes after that for cards, overlays, and calls to action.
- Use a small set of schemes repeatedly so the storefront feels consistent.
- Use **Accent** and **Shade** options for softer contrast and layering.
- Use **Transparent** when you want the parent area to show through.

### For custom development (optional)

If you are building custom sections or blocks, follow the same pattern Slab uses in source: add a `color_scheme` select setting in schema, then apply `{{ section.settings.color_scheme }}` or `{{ block.settings.color_scheme }}` on the wrapper element.



## Common scheme and border options

These are the options merchants usually see:

- **Scheme options:** Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Transparent, and your saved schemes (Scheme 1, Scheme 2, and any additional schemes you create).
- **Border options:** Body, Subtle, Strong, scheme-based border options, and None.

Developer note: border options commonly map to these utility classes in Slab source.

- Body -> `color__border-light`
- Subtle -> `color__border-divider-1`
- Strong -> `color__border-selected-1`
- Scheme-based border options -> scheme-specific border utility classes
- None -> `border-0!`
