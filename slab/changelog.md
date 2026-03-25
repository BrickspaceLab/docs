# Changelog

{% updates format="full" %}
{% update date="2026-03-25" tags="0.3.0" %}
## Progress bar, richer visibility rules, and layout refinements

#### Improvements

* Added **Progress bar** block for a simple 0–100 progress display (works well with metafields for dynamic values)
* Extended **Visibility** block with session-based rules, URL path matching (including wildcards), viewport-linked visibility tied to another element’s CSS class, and toggle animations when content is shown or hidden dynamically
* Added **Show advanced settings** on many blocks; **Drawer** and **Popup** overlays support margin presets, custom width (percentage), color inheritance, and device visibility behind advanced settings
* Updated documentation so block, section, and **Shop Pay installments** pages describe **Show advanced settings** and the settings it reveals, aligned with the theme editor
* Renamed button color styles **Transparent** and **Inverted transparent** to **Text** and **Inverted text**; added **Enable square** for icon-forward buttons
* Added **Enable color difference** in **Theme settings > Header** so header content can invert over overlapping page content
* Grid **Product gallery** can show image alt text under each image when enabled
* Added dedicated **Quick buy** product template for a minimal quick-buy layout (optional; still configurable under **Theme settings > Quick actions**)

#### Upgrade notes

* **Flex item:** **Enable width fill** and **Enable default width** are replaced by **Width** (**Fit**, **Fill**, or **Custom** with mobile and desktop percentage sliders). Shopify does not map the old checkboxes to the new setting, so after upgrading you should open each **Flex item**, choose the correct **Width** mode, and confirm percentages. **Show advanced settings** now gates device **Visibility**, **Enable sticky layout** (and **Sticky position**), plus **Load animation** and **Scroll animation** (pick one or neither)—reapply those if you used them before.
* **Theme settings (link / input colors):** The dedicated **Accelerated checkout** custom color scheme block next to link colors was removed. If you relied on that picker, review dynamic and accelerated checkout buttons after the update.
* **Button blocks:** Editor labels **Transparent** and **Inverted transparent** are now **Text** and **Inverted text**; the underlying styles are the same—no layout change required unless you are following old documentation by name.

#### Fixes

* Improved map rendering when a Mapbox API key is present
* HTML root uses the body background color to reduce loading flash
* Strong border color aligned with design tokens for consistency

{% endupdate %}

{% update date="2026-03-04" tags="0.2.0" %}
## Gallery zoom, high-variant support, and focus fixes

#### Improvements

* Added zoom on hover to grid and slider gallery blocks with cursor-tracking transform origin
* Added support for high-variant products (250+ variants) per Shopify guide
* Updated agent testing workflows with Stagehand and Cursor browser agent
* Updated Cursor skills with liquid-theme support

#### Fixes

* Fixed focus state on option swatches to prevent nested focus targets inside buttons
* Fixed swatches not displaying correctly for unavailable options


{% endupdate %}

{% update date="2026-02-19" tags="0.0.2" %}
## Initial early release

Prerelease version updated with fixed css and JavaScript assets. This is still a early preview so you will encounter setup issues using this version.

This version has missing json settings and translations for French, Spanish and Italian. You will likely have to update color settings and hit save.&#x20;
{% endupdate %}
{% endupdates %}
