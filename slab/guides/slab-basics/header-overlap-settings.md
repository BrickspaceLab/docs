# Header overlap

Header overlap settings in Slab let merchants place top-of-page content under the header for a layered storefront look. Use **Theme settings > Header** to turn overlap on globally, then fine-tune desktop and mobile overlap spacing.

For position-focused guidance, see [Set header position](header-position-settings.md).

## How to set up header overlap

Use this order so overlap spacing stays predictable:

1. Open **Theme settings > Header**.
2. Turn on **Enable header overlap**.
3. Set **Desktop overlap** based on your desktop header height.
4. Set **Mobile overlap** based on your mobile header height.
5. Open each section where you want overlap and enable that section's **Enable header overlap** setting.
6. Preview collection, product, and any custom top sections on desktop and mobile before publishing.

If either the theme-level or section-level overlap setting is off, the section will render in normal flow without overlap.

## Suggested setup defaults for most stores

- Keep **Enable header overlap** off unless your top sections are designed for text contrast over media.
- Start with the default overlap values, then adjust in 5 px steps to match your live header height.
- Keep desktop and mobile overlap values separate so each viewport aligns cleanly.
- Enable overlap only on sections where the top spacing and contrast still read clearly.

## What each header overlap setting controls

### Header

| Setting | What it controls | Range or options | Default |
| --- | --- | --- | --- |
| Enable header overlap | Master switch for header overlap behavior across supported sections. | Enabled, Disabled | Disabled |
| Desktop overlap | Overlap offset applied on desktop when header overlap is enabled. | 5 to 200 px (step 5) | 90 px |
| Mobile overlap | Overlap offset applied on mobile when header overlap is enabled. | 5 to 200 px (step 5) | 80 px |
