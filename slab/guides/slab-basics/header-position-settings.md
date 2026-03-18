# Set header position

Header position settings in Slab let merchants control how the header behaves while customers scroll the storefront. Use **Theme settings > Header** to choose whether the header stays fixed, scrolls with the page, or hides while scrolling.

## How to set up header position

Use this order to keep header behavior changes predictable:

1. Open **Theme settings > Header**.
2. In **Position**, choose **Sticky**, **Standard**, or **Dynamic**.
3. If you want sections to appear under the header, enable **Enable header overlap**.
4. Set **Desktop overlap** and **Mobile overlap** to match your header height and content spacing.
5. Open each section where you want overlap and enable that section's **Enable header overlap** setting.
6. Preview desktop and mobile scroll behavior before publishing.

## When to use each position mode

- **Sticky** keeps the header visible at the top of the storefront while customers scroll.
- **Standard** places the header in normal page flow, so it scrolls away with page content.
- **Dynamic** keeps the header at the top but hides it after scrolling starts and shows it again when customers return to the top.

## Suggested setup defaults for most stores

- Start with **Sticky** when quick access to navigation and cart is important.
- Use **Standard** for content-first landing pages where a fixed header feels too heavy.
- Use **Dynamic** when you want more vertical space while customers browse.
- Keep **Enable header overlap** off unless your top sections are designed for text contrast under the header.
- Start overlap near default values, then adjust by 5 to 10 px increments while previewing desktop and mobile.

## What each header setting controls

| Setting | What it controls | Options or range | Default |
| --- | --- | --- | --- |
| Position | Controls how the header behaves during page scroll. | Sticky, Standard, Dynamic | Standard |
| Enable header overlap | Allows sections to render under the header bar when those sections also enable overlap. | Enabled, Disabled | Disabled |
| Desktop overlap | Sets the desktop overlap offset used when header overlap is enabled. | 5 to 200 px | 90 px |
| Mobile overlap | Sets the mobile overlap offset used when header overlap is enabled. | 5 to 200 px | 80 px |
