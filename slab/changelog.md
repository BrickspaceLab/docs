# Changelog

{% updates format="full" %}
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
