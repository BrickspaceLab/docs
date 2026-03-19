# Header

Header settings in Slab control how the header behaves while customers scroll the storefront and whether top sections can overlap under it. Use **Theme settings > Header**.

## Set up header settings

Use this order to keep header behavior predictable.

{% stepper %}
{% step %}
### Choose a header position

1. Open **Theme settings > Header**.
2. In **Position**, choose **Sticky**, **Standard**, or **Dynamic**.
3. Preview desktop and mobile behavior before changing overlap settings.
{% endstep %}

{% step %}
### Enable overlap only when needed

1. Turn on **Enable header overlap** only if your top sections are designed for text contrast over media.
2. Set **Desktop overlap**.
3. Set **Mobile overlap**.

Desktop and mobile overlap values only appear when **Enable header overlap** is on.
{% endstep %}

{% step %}
### Enable overlap on the sections that need it

1. Open each top section where you want overlap.
2. Enable that section's **Enable header overlap** setting.
3. Preview key templates like home, collection, and product before publishing.

If either the theme-level or section-level overlap setting is off, the section renders in normal flow.
{% endstep %}
{% endstepper %}

## Suggested defaults for most stores

- Start with **Sticky** when navigation and cart should stay accessible.
- Use **Standard** for content-first pages where a fixed header feels too heavy.
- Use **Dynamic** when you want more vertical browsing space while keeping the header available.
- Keep **Enable header overlap** off unless top sections are intentionally designed for overlap.
- Adjust overlap in 5 px increments until spacing matches your live header height.

## Header settings reference

| Setting | What it controls | Range or options | Default |
| --- | --- | --- | --- |
| Position | Controls how the header behaves during page scroll. | Sticky, Standard, Dynamic | Standard |
| Enable header overlap | Allows supported sections to render under the header bar. | Enabled, Disabled | Disabled |
| Desktop overlap | Overlap offset for desktop when header overlap is enabled. | 5 to 200 px (step 5) | 90 px |
| Mobile overlap | Overlap offset for mobile when header overlap is enabled. | 5 to 200 px (step 5) | 80 px |
