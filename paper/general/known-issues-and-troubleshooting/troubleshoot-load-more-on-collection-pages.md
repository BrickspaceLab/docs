# Troubleshoot Load More on collection pages

Paper collection pages can paginate with **Load more on click** or **Load more on scroll** instead of numbered pages. If the **Load more** button appears but nothing loads—or the page count never increases—use this guide to isolate JavaScript conflicts, settings, and custom code issues.

## Confirm pagination settings

1. Open **Customize** > **Theme settings**.
2. Open **Pagination** (or **Navigation** > **Pagination**, depending on your theme version).
3. Confirm **Type** is set to **Load more on click** or **Load more on scroll**—not **Next/back buttons**.

| Pagination type | Customer experience |
| --------------- | ------------------- |
| Load more on click | Button at bottom of grid; click loads next page via AJAX |
| Load more on scroll | Automatically loads when customer scrolls near the bottom |
| Next/back buttons | Standard page links; no Load more button |

4. Save and retest on a collection with **more products than the collection section’s products-per-page limit**.

The Load more UI renders from `component__pagination.liquid` and calls `fetchAndRenderPage()` in the theme’s JavaScript bundle (Alpine.js).

## Quick diagnostic steps

{% stepper %}
{% step %}
**Test in a private window**

Rule out browser extensions blocking scripts. Open the collection URL logged out in incognito mode.
{% endstep %}

{% step %}
**Check the browser console**

1. Open the collection page on your storefront.
2. Open developer tools (**View** > **Developer** > **JavaScript Console** in Safari, or **F12** > **Console** in Chrome).
3. Click **Load more**.
4. Look for red errors—especially `fetchAndRenderPage is not defined`, Alpine errors, or failed network requests to the collection URL.

If no network request fires on click, a JavaScript error or script conflict likely stopped the handler.
{% endstep %}

{% step %}
**Disable app embeds temporarily**

In **Customize**, open **Theme settings** > **App embeds** and disable nonessential apps one at a time. Retest after each disable. Apps that inject global scripts often break AJAX pagination.
{% endstep %}

{% step %}
**Compare to an unmodified theme copy**

Duplicate your theme or add a fresh Paper install. Enable the same pagination type without custom code. If Load more works on the clean copy, the issue is custom or app code—not a core Paper defect.
{% endstep %}
{% endstepper %}

## Common causes

| Cause | What to look for |
| ----- | ---------------- |
| **JavaScript conflict** | Console errors when clicking Load more; handler never runs |
| **Custom code in `theme.liquid` or assets** | Modified theme files; support may be limited—see [modified-code policy](../../../general/general/support-policy-for-modified-theme-code.md) |
| **App script overrides `$fetch` or Alpine** | Issue starts after installing an app; fixed when embed disabled |
| **Too few products** | Collection has fewer items than **Products per page**—no second page to load |
| **Filtered collection URL** | Some filter combinations reload the page instead of AJAX; test the base collection URL first |
| **Pagination set to pages** | **Load more** UI hidden or non-functional when type is **Next/back buttons** |

## What Paper’s Load more expects

* Alpine.js must initialize on the collection template (`pagination_type` is not `pages`).
* `fetchAndRenderPage('next')` fetches the next page HTML and appends product cards to `#js-results`.
* A loading state disables the button briefly (`button_loading`) to prevent double clicks.

If your store uses aggressive performance apps that defer all JavaScript, ensure theme scripts still execute on collection pages.

## When to contact support

Include in your message:

* Collection URL and theme version
* Pagination type from **Theme settings**
* Console errors (screenshot)
* Whether Load more works on an unmodified duplicate theme
* Recent app installs or **Edit code** changes

Brickspace support can confirm bugs in **unmodified** Paper themes. Custom script debugging requires a developer or app vendor.

## Related reading

* [Use and install apps](../basics/use-and-install-apps.md)
* [How third-party apps affect theme styles](../../../general/general/how-third-party-apps-affect-theme-styles.md)
* [Support policy for modified theme code](../../../general/general/support-policy-for-modified-theme-code.md)
