# Troubleshoot favicon and SEO page title

Favicons and search-result titles can look “stuck” even after you change settings. This guide covers where each value is set, why caching delays updates, and how to verify the correct source is in control.

These steps apply to all Brickspace Lab themes (Paper, Space, Keystone, and Slab).

## Favicon not updating

### Where the favicon is set

Brickspace themes read the favicon from **Theme settings** > **Favicon** > **Favicon image** in the theme editor. Slab documents this under [Favicon settings](../../slab/getting-started/global-settings/favicon-settings.md); other themes use the same **Theme settings** path.

Shopify may also expose favicon controls in admin settings depending on your Shopify version. If both are set, confirm which theme is **published**—only the live theme’s favicon appears on the storefront.

### Steps to verify

{% stepper %}
{% step %}
**Confirm the live theme**

In **Online Store** > **Themes**, check which theme is published. Open **Customize** on that theme—not a duplicate or backup.
{% endstep %}

{% step %}
**Upload and save**

Under **Theme settings** > **Favicon**, upload a square image (about 400×400 px works well). Click **Save**.
{% endstep %}

{% step %}
**Hard refresh or use a private window**

Browsers cache favicons aggressively. Open the storefront in an incognito/private window or hard refresh. Tab icons can take several minutes to update.
{% endstep %}

{% step %}
**Check for duplicate favicon tags (custom code)**

If you or an app edited `theme.liquid` or layout files, a second `<link rel="icon">` tag may override theme settings. Search **Edit code** for `rel="icon"` or `favicon`. Remove duplicate tags or ask your developer to reconcile them.
{% endstep %}
{% endstepper %}

## SEO page title or meta description not showing

### Two places control search snippets

| Source | Controls |
| ------ | -------- |
| **Shopify admin** — product, collection, or page **Search engine listing** | Title and meta description for that resource |
| **Theme defaults** | Fallback title patterns when a resource has no custom SEO fields |

Themes output meta tags based on Shopify’s SEO fields. Changing only the visible page heading in a section block does **not** automatically change the `<title>` tag or meta description.

### Steps to verify

1. In Shopify admin, open the product, collection, page, or blog post.
2. Scroll to **Search engine listing** (or **Edit website SEO**).
3. Set **Page title** and **Meta description** explicitly. Save.
4. View page source on the storefront and search for `<title>` and `meta name="description"`.
5. Allow time for Google to recrawl—Search Console updates are not instant.

For broader SEO context, see [SEO for Shopify](../../paper/guides/basics/seo-for-shopify.md).

## Still not working?

Include the following when you [contact support](contact-support.md):

* Store URL and whether the issue is favicon, title, or meta description
* Published theme name and version
* Whether **Edit code** or apps were used on layout files
* A screenshot of the relevant **Theme settings** or **Search engine listing** panel
* Whether the problem appears in a private browser window

If custom layout code is involved, see [Support policy for modified theme code](support-policy-for-modified-theme-code.md).

## Related reading

* [Get help with Brickspace themes](get-help-with-brickspace-themes.md)
* [SEO for Shopify](../../paper/guides/basics/seo-for-shopify.md)
