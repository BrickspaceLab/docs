# Installing apps

Third-party apps often inject forms, popups, or widgets into your storefront. When an app embed looks unstyled, broken, or “wrong” compared to its marketing site, merchants sometimes assume the theme is at fault. In most cases, normal **CSS cascade** behavior is involved—and fixing the app’s appearance is the app developer’s responsibility, not the theme author’s.

**How app embeds inherit theme styles**

Brickspace Lab themes ship global base styles: typography, button resets, form field styling, link colors, and spacing utilities. Any HTML the app injects into your page sits inside the same document as your theme.Browsers apply CSS from the outside in:

1. **Theme global styles** set defaults for elements like `button`, `input`, `h1`, and `a`.
2. **App stylesheets** load afterward and try to style the app’s own markup.
3. When selectors overlap, **specificity and load order** decide what wins.

If the theme’s global rules are broad (for example `button { font-family: … }`), app buttons can inherit theme fonts, padding, or borders even when the app author expected their stylesheet to control everything. That is expected browser behavior—not a theme bug.

**Why themes do not exclude vendor-specific app CSS**

There are thousands of Shopify apps, each with different HTML structures and class names. Brickspace Lab themes cannot maintain a blocklist of vendor-specific CSS overrides in core stylesheets because:

* App markup changes between app versions without notice.
* Overrides for one app often break another app on the same store.
* Scoped fixes belong in the app’s integration layer or in **store-specific custom CSS**, not in the base theme.

We design themes for storefront consistency. App vendors are responsible for styles that survive inside customer themes.

**Our policy on third-party app support**

Brickspace Lab **does not provide support for third-party app integrations**. That includes:

* Styling or layout of app popups, forms, or widgets
* Conflicts between app JavaScript and theme JavaScript
* App features that stop working after a theme update
* Code an app left in theme files after uninstall

For app issues, **contact the app developer first**. They control the embed, its CSS, and its scripts.For our full support scope, see [Contact support](https://app.gitbook.com/o/IxMO7qKqucxvsAjnGtFw/s/TnJCyRVLdtKs6ZCDLXr1/general/contact-support) and [Support policy for modified theme code](https://app.gitbook.com/o/IxMO7qKqucxvsAjnGtFw/s/TnJCyRVLdtKs6ZCDLXr1/general/support-policy-for-modified-theme-code).

**What merchants can do**

**1. Confirm the app is the source**

1. In **Customize**, open **Theme settings** > **App embeds** (or the template’s app blocks).
2. Disable the app embed temporarily.
3. Reload the page. If the styling issue disappears, the app—not the theme—is involved.

**2. Ask the app developer for scoped CSS**Request CSS that targets **only their embed’s root container** (for example a wrapper class the app documents). Good app CSS avoids resetting global `button` or `input` rules on the entire page.**3. Add store-specific overrides (optional)**&#x49;f the app vendor provides fix CSS, add it through:

* **Theme settings** > **Custom CSS** (all Brickspace themes), or
* A **Custom liquid** section for isolated markup

Keep overrides narrow. Avoid editing core theme files unless you accept [modified-code support limits](https://app.gitbook.com/o/IxMO7qKqucxvsAjnGtFw/s/TnJCyRVLdtKs6ZCDLXr1/general/support-policy-for-modified-theme-code).**4. Prefer supported install methods**Use [app blocks and app embeds](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/apps) rather than manual script tags pasted into `theme.liquid`. See [Use and install apps](../../../paper/guides/basics/use-and-install-apps.md) for general guidance.

**Common symptoms and likely causes**

| Symptom                                     | Likely cause                               |
| ------------------------------------------- | ------------------------------------------ |
| App popup uses theme fonts or button styles | Global CSS inheritance (cascade)           |
| App form fields match theme inputs          | Theme form resets applied to injected HTML |
| App worked on a previous theme              | Different global CSS on the new theme      |
| App broke after uninstall                   |                                            |
