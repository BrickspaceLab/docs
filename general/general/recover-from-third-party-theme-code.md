---
hidden: true
---

# Recover from third-party theme code changes

If a freelancer, agency, or app changed your theme’s Liquid, CSS, or JavaScript, you might see broken layouts (for example desktop styling on mobile), console errors, or features that no longer match the original Brickspace behavior.

This guide helps merchants narrow down what happened and choose a safe path forward.

## Confirm whether code was customized

1. In the Shopify admin, go to **Online Store** > **Themes**.
2. On the affected theme, open the **…** menu and choose **Edit code** (or use **Actions** > **Edit code**, depending on your admin version).
3. Look at **Layout**, **Templates**, **Sections**, and **Snippets** for recent edits. Files with unfamiliar comments, disabled blocks, or large pasted scripts often point to contractor work.

If you only used the theme editor (**Customize**) and never opened **Edit code**, the issue is more likely a setting, an app embed, or a bad product image order than hand-written Liquid.

## Capture evidence before you change anything

* Note the exact page URL and whether the problem is mobile, desktop, or both.
* Take screenshots or a short screen recording.
* If you can, duplicate the theme (**…** > **Duplicate**) and work on the copy so you always have the modified original to compare.

## Compare against a clean install

1. Add a fresh copy of your Brickspace theme from your purchase source (for example the **Theme library** or **Add theme** flow).
2. Publish is not required: open **Customize** on the clean copy and navigate to the same template (for example **Default product**).
3. If the clean theme looks correct while the modified one does not, the difference is almost certainly custom code or an app, not a hidden Shopify outage.

## Roll back or isolate the change

* **Revert a single file:** In **Edit code**, open the file you suspect, use the file history feature when Shopify offers it, or paste back a known-good version from a duplicate you made before the edits.
* **Remove app blocks and app embeds:** In **Customize**, check the app embeds area and the template’s app blocks. Temporarily disable them one at a time to see if layout returns to normal.
* **Restore an older theme copy:** If you still have an older duplicate from before the contractor started, you can publish that duplicate or copy settings forward manually.

## When to contact the original developer

Theme code is interconnected. If you are not comfortable reading Liquid, ask the contractor for a written list of files changed and either a rollback or a patch that restores mobile breakpoints. Be explicit that the storefront must match the unmodified theme’s responsive behavior unless you signed off on a new design.

## Brickspace support and custom code

Brickspace support covers defects in **unmodified** theme files and questions about built-in settings. It does not include debugging arbitrary third-party edits. See [Contact support](contact-support/) and [Support policy for modified theme code](support-policy-for-modified-theme-code.md) for the full policy.

If you need hands-on help merging updates or cleaning custom work, consider hiring a Shopify Expert. The general hub lists [Hire a Shopify developer](../support/hire-a-shopify-developer.md).

## Related reading

* [Test responsive layouts without publishing the theme](test-responsive-layouts-without-publishing.md).
* [Get help with Brickspace themes](contact-support/get-help-with-brickspace-themes.md) — include your comparison results when you write in.
