# Changelog

{% updates format="full" %}
{% update date="2026-05-12" tags="0.4.0" %}
## Header transitions, schema cleanup, and storefront refinements

* Added **Header transition** options for **Fade**, **Slide up**, **Slide down**, and **Slide right** when page transitions are enabled.
* Added header overlay color and border controls so overlapped headers can keep contrast against either the bar or the page background.
* Added **Enable balanced wrapping** to the **Rich text** block for more balanced multiline text.
* Added inline filter horizontal alignment controls and mobile margin controls for the product section.



<details>

<summary>Upgrade notes</summary>

* Review blocks with custom color settings after updating. Slab 0.4.0 improves color inheritance for non-nestable blocks, which can change how inherited and custom schemes are applied in some layouts.
* If you use custom header overlap designs, review the header section's default and overlay color schemes after updating so the header remains readable over both the bar and the page background.

</details>

<details>

<summary>Improvements</summary>

* Improved the shared schema settings system and applied shared settings across blocks for more consistent editor controls.
* Improved flex layouts, flex item editor behavior, and gap spacing inside container blocks.
* Improved page transitions to avoid content scrolling during navigation.
* Improved marquee image rendering so images keep better proportions while scrolling.
* Improved product section layout control with a mobile margin setting.
* Added site credits to the developer console.
* Removed the deprecated `update-shopify-json` agent skill and added schema-setting rules for agents.

</details>

<details>

<summary>Fixes</summary>

* Fixed right-positioned alert overlays staying left aligned.
* Fixed custom liquid blocks so content can use the full available width.
* Fixed theme editor scrolling to the wrong block when selecting a flex item.
* Fixed broken button layout inside cards, trigger button hit areas, and standard button sizing in the account sheet block.
* Fixed header overlap, menu item overlap, and header bar loading z-index issues.
* Fixed background video in container blocks hiding inner content and mobile section backgrounds appearing skewed.
* Fixed checkbox border color, product quantity input height, share button icon backgrounds, and cart item alignment.
* Fixed product media hover images overlapping and gallery alt text layout in grid mode.
* Fixed tab block content vertical padding, newsletter inline layout, button block flex wrapping, and sibling product dropdown radius and width.
* Fixed filter dropdown shadows and incorrect color settings.

</details>

{% endupdate %}

{% update date="2026-03-26" tags="0.3.1" %}
## Developer workflow, CORS for local dev, and version alignment

* Bumped theme version to 0.3.1 and updated in-theme help links (design-mode menu, support tooling) so they reference this changelog entry. **No changes to storefront behavior, theme settings, blocks, or sections** compared with 0.3.0.



<details>

<summary>Improvements</summary>

* Added Cursor command **`pull-upstream-updates`** and expanded **[Pull upstream updates](advanced-customizations/getting-started/pulling-upstream-updates.md)** for fork owners merging releases from `upstream`.
* Improved local development by documenting optional **`CORS_ORIGINS`** in **[Install from GitHub](getting-started/installing-slab/installing-from-github.md)** for Vite when previewing on custom domains or tunnels.
* Updated theme-repo developer docs (`README`, `AGENTS.md`) for CORS and upstream workflows.

</details>

{% endupdate %}

{% update date="2026-03-25" tags="0.3.0" %}
## New blocks, richer visibility rules, and layout refinements

* Added **Progress bar** block for a simple 0–100 progress display.
* Added **Account sheet** block to display login with Shop in a simple popover.
* Added a **Main** color option across color schemes that uses the body foreground as a background.
* Added gradient support to all color schemes.
* Added load-in animation support to select blocks.
* Added session-based rules, URL path matching, viewport-linked visibility, and toggle animations to **Visibility**. This lets you create a sticky add to cart bar when the primary add to cart scrolls out of view.
* Added **Show advanced settings** to many blocks to maintain merchant usability.
* Added restriction bypass support for wholesale features.
* Added margin presets, custom widths, color inheritance, and device visibility to **Drawer** and **Popup** advanced settings.
* Added **Enable color difference** in **Theme settings > Header** so header content can invert over overlapping page content.
* Added image alt text support to grid **Product gallery** when enabled.
* Added a dedicated **Quick buy** product template for a minimal quick-buy layout. It remains configurable under **Theme settings > Quick actions**.



<details>

<summary>Upgrade notes</summary>

* **Flex item:** **Enable width fill** and **Enable default width** are replaced by **Width** (**Fit**, **Fill**, or **Custom** with mobile and desktop percentage sliders). Shopify does not map the old checkboxes to the new setting, so after upgrading you should open each **Flex item**, choose the correct **Width** mode, and confirm percentages. **Show advanced settings** now gates device **Visibility**, **Enable sticky layout** (and **Sticky position**), plus **Load animation** and **Scroll animation** (pick one or neither)—reapply those if you used them before.
* **Theme settings (link / input colors):** The dedicated **Accelerated checkout** custom color scheme block next to link colors was removed. If you relied on that picker, review dynamic and accelerated checkout buttons after the update.
* **Button blocks:** Editor labels **Transparent** and **Inverted transparent** are now **Text** and **Inverted text**; the underlying styles are the same—no layout change required unless you are following old documentation by name.

</details>

<details>

<summary>Improvements</summary>

* Improved header settings by removing redundant options.
* Improved product option labels by removing unnecessary punctuation.
* Improved the quick buy block editor by removing the warning.
* Improved product option and dropdown interaction details.

</details>

<details>

<summary>Fixes</summary>

* Fixed sidebar overlays cropping main content on smaller screens.
* Fixed hover image behavior for transparent images.
* Fixed block preview backgrounds.
* Fixed content shifting with the filter stack.
* Fixed dynamic map storefront behavior so added map keys appear correctly.
* Fixed strong border color alignment with design tokens for consistency.

</details>


{% endupdate %}

{% update date="2026-03-04" tags="0.2.0" %}
## Gallery zoom, high-variant support, and focus fixes

* Added zoom on hover to grid and slider gallery blocks with cursor-tracking transform origin.
* Added support for high-variant products (250+ variants) per Shopify guide.



<details>

<summary>Improvements</summary>

* Improved Stagehand and Cursor browser agent workflows for agent testing.
* Improved liquid-theme support to Cursor skills.

</details>

<details>

<summary>Fixes</summary>

* Fixed focus state on option swatches to prevent nested focus targets inside buttons.
* Fixed swatches not displaying correctly for unavailable options.

</details>


{% endupdate %}

{% update date="2026-02-19" tags="0.0.2" %}
## Initial early release

Prerelease version updated with fixed css and JavaScript assets. This is still a early preview so you will encounter setup issues using this version.

This version has missing json settings and translations for French, Spanish and Italian. You will likely have to update color settings and hit save.
{% endupdate %}
{% endupdates %}
