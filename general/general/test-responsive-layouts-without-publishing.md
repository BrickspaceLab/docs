# Test responsive layouts without publishing the theme

You can review how your Brickspace theme looks on phones and tablets before you publish changes to your live storefront.

## Use the theme preview on a real device

1. In the Shopify admin, go to **Online Store** > **Themes**.
2. On the theme you are editing (often a duplicate while you work), click the **…** menu, then **Preview**.
3. Shopify opens a preview URL. Copy that URL from the browser address bar.
4. Send the link to your phone (AirDrop, email, Slack, QR code generator, and similar methods all work), then open it on the device.

The preview URL reflects your unpublished theme editor changes, so you see the same layout your team sees in **Customize** without affecting customers on the live theme.

## Use responsive mode in your desktop browser

1. Open the same preview URL in Chrome, Edge, or Firefox.
2. Open developer tools (for example **View** > **Developer** > **Developer tools** in Chrome).
3. Toggle the device toolbar and pick a phone or tablet profile.

This is fast for layout checks. It does not replace testing on a real phone when you care about touch gestures, safe areas, or mobile performance.

## Run a local preview with Shopify CLI (advanced)

If you use [Shopify CLI](https://shopify.dev/docs/themes/tools/cli) for theme development, you can run `shopify theme dev` to serve your theme with live reload. Open the tunnel or localhost URL on a phone on the same network (or use the CLI’s share options when available) to test responsive behavior against your local files.

## Adjust sections per device in the theme editor

Brickspace themes support **device-specific visibility** on many sections so you can show, hide, or tune content separately for mobile and desktop. That is useful when you want a simpler mobile layout while keeping a richer desktop block.

For theme-specific steps, open your product’s documentation hub and search for **device-specific visibility** (for example Keystone: [Device specific visibility](../../keystone/guides/sitewide/device-specific-visibility.md)).

## Related reading

* [Recover from third-party theme code changes](recover-from-third-party-theme-code.md) — if mobile layout breaks after custom edits.
* [Get help with Brickspace themes](contact-support/get-help-with-brickspace-themes.md) — when you need support after your own tests.
