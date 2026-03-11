# Changelog

{% updates format="full" %}
{% update date="2026-02-27" tags="2.2.2" %}
## 2.2.2 Product gallery and sticky content improvements

**Fixes**

* Fixed product gallery image switching when thumbnail images are clicked
* Improved gallery logic to consistently target the visible gallery instance (desktop or mobile)
* Added sticky product right-column behavior with dynamic top offset for sticky headers
* Fixed cart note toggle behavior by clearing note content when the option is turned off
{% endupdate %}

{% update date="2025-12-12" tags="2.2.1" %}
## 2.2.1 Swatch counts, product template, and currency fixes

**Fixes**

* **Improved product template block positioning**\
  We reworked how blocks are positioned in the product template to ensure more consistent layout behavior and better control across mobile and desktop.
* **Accurate swatch counts on product cards**\
  Fixed an issue where product cards displayed an incorrect number of swatches. Swatch counts now reflect the actual variant options.
* **Correct swatch display with dropdown selectors**\
  Resolved a bug where swatches wouldn't appear correctly when the product used dropdown-style variant selectors.
* **Updated currency meta tag for multi-market setups**\
  Updated the currency meta tag to behave correctly across multi-market stores, improving compatibility with region-specific pricing and SEO expectations.
* **Restored missing blog thumbnails**\
  Fixed an issue where blog post thumbnails failed to display.
* **Header menu alignment fix**\
  Corrected a layout issue that caused the header menu to misalign in certain configurations.
{% endupdate %}

{% update date="2025-10-16" tags="2.2.0" %}
## 2.2.0 High-variant product support and swatch display settings

Big update here to improve how our theme works with high variant products. We had to do a big rework with how a lot of features work.

**Added**

* Added new setting to display swatches with buttons or drop-down independently of other options

**Fixes**

* Updated and improved support for high-variant products
* Fixed combined listing in quick add breaking pagination
* Fixed combined listing selection being unselected
* Fixed broken mobile filter button
* Fixed pagination after using collection filters
* Fixed pickup availability block not appearing when refreshing
* Fixed missing linked products block on featured product section
* Fixed missing title in upsell block
{% endupdate %}

{% update date="2025-09-05" tags="2.1.3" %}
## 2.1.3 Template installation fixes

**Fixes**

* Fixed broken default settings preventing all section files from importing on installation
{% endupdate %}

{% update date="2025-06-23" tags="2.1.2" %}
## 2.1.2 Install experience and store locator fixes

**Fixes**

* Fixed listing directory with better defaults for an improved install experience
  * Removed image setting so theme is installed without images
  * Removed internal Intercom widget used on theme store
* Fixed store locator not appearing on mobile
{% endupdate %}

{% update date="2025-05-12" tags="2.1.0" %}
## 2.1.0 Quick bug fixes

Quick update to fix a number of smaller bugs that have popped up recently.

**Fixes**

* Fixed missing quick add button on mobile when using overlay setting
* Fixed button alignment in text highlight section
* Fixed missing width classes with text highlight section
* Fixed missing translations in tooltip section
* Fixed focus state from being shown on mobile
* Fixed sticky layout when using split view
* Fixed pickup block in featured product section
* Fixed broken link for border support
{% endupdate %}

{% update date="2025-02-11" tags="2.0.0" %}
## 2.0.0 High-variant support, swatch settings, and major improvements

Big, huge, massive update. We're adding support for the upcoming variant limit increase — which means Space will support up to 2,000 variants per product when Shopify releases this update. We've also went through and dialed in a number of settings and features. For example, you now have much more control over how to display color swatches by changing size and styles.

You should always review your theme settings and adjust your theme as needed when updating. This update introduces a number of new or changed settings that should be reviewed:

* Theme settings > Product options — review settings to adjust color swatch display
* Theme settings > Quick add — review new settings to control how quick add buttons are displayed
* Slider sections — review slider sections that include new settings to control arrow, scrollbar, and dot-indicator display

**Added**

* Added support for high-variant products
* Added improvements to swatch rendering — you can now change the size of color swatches, disable color labels, and change the grid layout
* Added new setting to control product gallery sizing on both desktop and mobile
* Added new setting to "Show image" on navigation slider
* Added setting to "Show close buttons on mobile"
* Added support to show menu items when using "Center" layout
* Added better hover states across different sections
* Added better alt text display on product pages
* Added color option to collection template filter
* Added option to show or hide variant option labels
* Added improved sliders with more settings to control display of arrows, indicators, and scrollbars
* Added option to set font family on price block
* Added option to use a custom font size for banner headings
* Added better mobile support for hotspot section
* Added improved pagination when returning to an infinite-scrolled page
* Added alt text to fullscreen image product gallery
* Added setting to toggle chevron icons in menu drawer
* Added better control when displaying sale prices
* Added option to set quick-add button position and color
* Added setting to change how cart upsells are displayed

**Changed**

* Changed desktop dropdown menu to use same font family
* Changed padding around "Taxes included" message
* Changed and updated typography inconsistencies in drawer content

**Fixes**

* Improved product cards so titles are clickable
* Fixed error where items get added above their quantity
* Fixed add to cart breaking when "Enable default variant" unchecked
* Fixed age verification displaying when adding a product to cart
* Fixed price updating incorrectly on cart page
* Fixed quick add label when item sold out
* Fixed missing product option labels
* Fixed label in edit drawer
* Fixed overlap when using tall images in block reveal section
* Fixed checkboxes appearing incorrectly when using bottom border
* Fixed spacing in navigation slider when layout gap size set to 1
* Fixed line breaks not working in product descriptions
* Fixed header overlap on split banner
* Fixed collection blocks breaking grid layout
* Fixed Safari double border radius issue
* Fixed product overlap with image hotspot
* Fixed weird layout in collection list grid
* Fixed overlap on input increments
* Fixed horizontal margin in pickup block
* Fixed video section play button
* Fixed video interaction causing page refresh
* Fixed video not playing when "Enable video autoplay" is unchecked
* Fixed collection blocks not appearing on additional pages
* Fixed all search results being shown
* Fixed search input not using correct border
* Fixed broken hover on search drawer
* Fixed "Hover to open" from breaking navigation for mobile
* Fixed inputs not inheriting parent color
* Fixed missing border in recent and recommended sliders
* Fixed content shift when using open accordions
{% endupdate %}

{% update date="2025-01-29" tags="1.2.1" %}
## 1.2.1 Deprecated font replacements

**Changed**

* Changed default fonts for presets, replacing deprecated fonts with recommended replacements
{% endupdate %}

{% update date="2024-10-16" tags="1.2.0" %}
## 1.2.0 Safari fixes, improved colors, and swatch support

Lots of improvements here. This update has a lot of small visual improvements and bug fixes specifically for Safari display issues.

**Added**

* Added sticky position for content in banner when set to top alignment
* Added new "Show location" setting to header bar
* Added previous and next buttons to blog article as a block
* Added new hover styling for menu drawer
* Added improved CSS for accelerated checkout and buy-it-now buttons
* Added performance improvements for liquid rendering

**Changed**

* Updated how colors are rendered — accent and shade colors will now lighten or darken based on the body background, working much better with dark body backgrounds
* Revised 3D model viewer shown on product pages — horizontal scrolling will no longer be interrupted when hovering over a model
* Revised and implemented improved animations
* Changed default image color so transparent PNGs appear as expected
* Used liquid default from Dawn theme for structured data

**Fixes**

* Fixed mobile gallery on product pages from not sliding to the selected featured variant image
* Fixed placeholder text not appearing in gift card form
* Fixed a variety of Safari image and grid display issues
* Fixed vertical alignment setting for blocks in Collage section
* Fixed broken video sections when using multiple video sections on the same template
* Fixed promo block overlap in menu drawer
* Fixed subscription products not adding correctly when using third-party widgets
* Fixed address popup not loading correct region selector
{% endupdate %}

{% update date="2024-09-03" tags="1.1.0" %}
## 1.1.0 Sign in with Shop, combined listing support, and bug fixes

Welcome to our first big patch since our release! Detailed below we have a list of new features, bug fixes, and general improvements we've made over the past two months.

**Added**

* Added new rating component for easy customizations
* Added Sign in with Shop button and a setting allowing to enable/disable the button
* Added ability to force different layout on mobile product page
* Added setting allowing to set section heading layout to split
* Added support for videos being used in first media position in product cards
* Added setting to set product/collection slider size
* Added text-position setting to content-item component
* Added support for Shopify combined listing app
* Added new global setting for app blocks position on product page

**Changed**

* Updated store locator section to use Mapbox
* Updated stock indicators
* Updated collection grid and slider to use "collection\_list" setting
* Updated Twitter icon to x.com icon
* Revised settings for background media on card blocks
* Hidden focus border on mobile devices

**Fixes**

* Increased size of spots in hotspot with "plus" icon
* Fixed swatches displaying incorrectly
* Fixed when variant selection options include space
* Fixed special characters breaking option selection
* Fixed quantity increment disabled incorrectly
* Fixed quick search from not using correct fetch URL
* Fixed app blocks appearing in wrong order on product page
* Fixed horizontal layout setting in icon grid
* Fixed product descriptions from stripping paragraph spacing
* Fixed search drawer on mobile
* Fixed video not working in article cart block
* Fixed weird layout shift in sub footer
* Fixed zoom gallery issues on mobile
* Fixed image gallery display when only one image is shown
* Fixed input padding with no border
* Fixed so videos can be used in split banner with no buttons
* Updated swatches to support new Shopify metafield setup
{% endupdate %}

{% update date="2024-07-08" tags="1.0.1" %}
## 1.0.1 Preset style name changes

**Changed**

* Changed names of style presets
{% endupdate %}

{% update date="2024-07-04" tags="1.0.0" %}
## 1.0.0 Space goes live

Space comes out! This is our initial release. We'll be following up this release with a number of smaller fixes and design tweaks to continue to elevate this theme.
{% endupdate %}
{% endupdates %}
