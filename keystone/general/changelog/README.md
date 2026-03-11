# Changelog

{% updates format="full" %}
{% update date="2026-02-27" tags="2.1.1" %}
## 2.1.1 Account fixes, banner rendering, and cart note improvements

**Added**

* Added upsell style options in locale schema files
* Added better login/signup button controls and labels for account sections
* Added cart note HTML entity decoding for special characters

**Fixes**

* Fixed signup/login text issues, including legacy strings and missing Italian translations
* Fixed banner image/video behavior to improve rendering and fallback handling
* Fixed cart notes with special characters so they render correctly
* Fixed bundle help-link text and locale formatting
* Updated dev setup and dependencies for smoother local development
{% endupdate %}

{% update date="2025-12-12" tags="2.1.0" %}
## 2.1.0 Customer account visibility controls and improved login settings

**Improved customer account visibility controls**\
You can now more clearly control which content is shown or hidden based on a shopper's account status. This gives you finer control over gated content and member-only experiences. These new visibility controls are available on the Richtext, Collage, and Banner sections.

**Customizable login and signup button**\
A new setting lets you customize the signup button action, allowing you to point it to any URL you need. This makes it easy to route users to external signup flows or custom pages.

**Legacy form section compatibility**\
The legacy form section now displays a simple button that directs users to the new customer account signup form when enabled. This ensures that if a customer encounters a legacy form while using the new customer accounts, the experience still works and sends them to the correct page.

**Fixes**

* **Clearer login redirect behavior**\
  Theme settings have been updated to better explain the limitations around login redirects, reducing confusion when customizing customer account flows.
* **Correct account link routing**\
  Fixed an issue where some account links pointed to incorrect destinations. All account-related links now route properly.
* **Adjusted currency meta tag for multi-market setups**\
  Updated the currency meta tag to behave correctly across multi-market stores, improving compatibility with region-specific pricing and SEO expectations.
{% endupdate %}

{% update date="2025-11-05" tags="2.0.1" %}
## 2.0.1 Theme editor access during restrictions and variant table direct links

**Edit themes while restrictions are enabled**\
We added a new editor condition that allows you to make theme changes even when site restrictions are turned on (for example during password protection or maintenance mode). This removes unnecessary blockers and improves admin workflows.

**Direct links for variant tables**\
Variant table selections now deep-link directly to the preselected variant. Shoppers are taken straight to the exact variant they chose, reducing extra clicks and friction on the product page.

**Fixes**

* **Sticky buy button reliability**\
  Fixed an issue where the Sticky Buy Button could fail to add items to cart, ensuring consistent add-to-cart behavior.
* **Mobile sub-collection grid**\
  Resolved overflow issues on small viewports so grids now render cleanly across mobile devices.
* **Subtag menu highlighting**\
  Corrected a bug where multiple labels with matching prefixes could appear highlighted at the same time.
* **Featured product rendering**\
  Fixed layout and display issues affecting the Featured Product section so it now renders as intended across themes and breakpoints.
{% endupdate %}

{% update date="2025-10-16" tags="2.0.0" %}
## 2.0.0 Variant table pagination and high-variant product support

Lots of improvements here to really fine tune how Keystone handles high variant products. We've introduced new table pagination for variant rows and let you control how this is setup now.

**Added**

* Added new settings to change how variant tables are loaded — merchants now have the ability to load with no variant rows loaded, improving page performance when many variants are available
* Added new pagination to variant tables so merchants can load 50 variant rows at a time
* Added improved pagination when returning to an infinite-scrolled collection page — scrolling back now returns to the correct page instead of the first

**Fixes**

* Improved support for high-variant products
* Fixed pagination from breaking after using filters
* Fixed discounts breaking cart checkout with specific apps
* Fixed quantity selectors not respecting stock count
* Fixed pickup block not being shown when variant preselected
* Fixed combined listing selection being unselected
{% endupdate %}

{% update date="2025-08-05" tags="1.4.1" %}
## 1.4.1 Preset listing defaults fix

**Fixes**

* Fixed broken default settings preventing all section files from importing on installation
{% endupdate %}

{% update date="2025-07-14" tags="1.4.0" %}
## 1.4.0 Account icon header link and bug fixes

This update includes a batch of bug fixes and introduces a new setting to link the account icon in the header directly to the account page, bypassing the account drawer if desired.

**Added**

* Added ability to link account icon in header bar to account page

**Fixes**

* Fixed duplicating footer content
* Fixed price range slider not increasing from 0
* Fixed incorrect help text in theme settings
* Fixed broken pagination on blog post comments
* Fixed cart page incorrectly displaying cart quantity
* Fixed "Featured product" image not full screening
* Fixed cart grouping causing memory freezes
* Fixed "Show entire image" in slideshow
{% endupdate %}

{% update date="2025-06-09" tags="1.3.2" %}
## 1.3.2 Install experience improvements

**Fixes**

* Fixed listing directory with better defaults for an improved install experience
  * Removed image setting so theme is installed without images
  * Removed internal Intercom widget used on theme store
  * Added missing collection.json preset files
{% endupdate %}

{% update date="2025-06-09" tags="1.3.1" %}
## 1.3.1 Theme file restructure for theme store redesign

**Changed**

* Created subfolders for preset listings
* Changed preset names in the config file
* Added the .json files matching each preset's demo store/templates and /sections into their respective subfolders
{% endupdate %}

{% update date="2025-05-07" tags="1.3.0" %}
## 1.3.0 Cart, accounts, and product discovery improvements

This release significantly improves the customer journey with enhanced product discovery, streamlined cart functionality, and a more robust account system.

**Added**

* Added alt text to fullscreen product image gallery
* Added option to set play button text for video section
* Added setting to change how cart upsells are displayed
* Added check to hide cart upsells that are already in cart
* Added delete button for products in cart on mobile
* Added success and error messages after login or signup
* Added new badge setting to show sold out labels
* Added setting to redirect after login or signup
* Added ability to include up to 3 custom product and variant metafields to product tables
* Added new preset

**Changed**

* Changed name of signup form section to "Legacy signup"

**Fixes**

* Fixed price range slider displaying incorrectly for certain currencies without decimals
* Fixed vertical icon alignment
* Fixed spacing in navigation slider when gap set to 1
* Fixed video interaction causing page refresh
* Fixed checkboxes appearing incorrectly when using bottom border
* Fixed line breaks from not working in product descriptions
* Fixed width for featured upsell slider
* Fixed broken "Add address" button in account drawer
* Fixed required region field error for non-region countries
* Fixed missing password reset email
* Fixed price range thumb not matching input location
* Fixed sort dropdown missing padding
* Fixed banner search text not displaying on light backgrounds
* Fixed scroll reflow after using filters
* Fixed slider borders not wrapping entire content
* Fixed "Products per page" limit to include a max to avoid going above pagination limit
* Improved mobile support for hotspot section
* Improved login experience so unapproved logged-in users see a warning
* Improved collection view to maintain selected view — customers will not be switched back to grid view when filtering
* Updated "Skip to content" button so it is hidden even when scrolling up
* Updated product lists to hide "Default title"
{% endupdate %}

{% update date="2024-12-11" tags="1.2.0" %}
## 1.2.0 Price hiding for non-approved accounts and new product blocks

We've been getting lots of feedback on Keystone and want to prioritize pushing out updates since the theme is still relatively new. Which is why we've got a few exciting features in this update like the ability to hide product prices for non-approved customers.

**Added**

* Added ability to hide product prices unless logged into an approved account
* Added new "Request a quote" block on product template
* Added improvements to all sliders with more control over how to display scrollbars, arrows, and indicators
* Added ability to fold nested menu items within accordions
* Added minimal accordion style to product block "Collapsible content"

**Changed**

* Changed theme default settings to remove deprecated fonts

**Removed**

* Removed "Enable header overlap" setting as this was accidentally included

**Fixes**

* Fixed missing translations for "Product comparison" metafield
* Fixed missing CSS for outline button styles
{% endupdate %}

{% update date="2024-11-27" tags="1.1.0" %}
## 1.1.0 Product comparison section and metafield improvements

Smaller update here with some solid improvements to metafield support. The coolest thing launching here is the support to include custom product or variant metafield data inside your product tables. We're also including a new product comparison section.

**Added**

* Added new product comparison section
* Added support to include product and variant metafields inside product tables
* Added more support so product titles are linked correctly
* Added support to set which column app blocks are placed in for product pages
* Added previous/next buttons to blog articles

**Changed**

* Revised image component by removing unnecessary properties

**Fixes**

* Fixed age verification when adding a product
* Fixed many minor issues flagged by automatic theme check
{% endupdate %}

{% update date="2024-11-12" tags="1.0.1" %}
## 1.0.1 Post-launch bug fixes

First update for Keystone. We're fixing a number of small issues that have cropped up after some initial feedback.

**Added**

* Added "see more" button when variant tables have more than 6 rows

**Changed**

* Updated location to toggle between list and grid view
* Updated padding around "taxes included" messaging

**Fixes**

* Fixed share cart URL
* Fixed cart from not adding correct quantities when rapid-clicking multiple add buttons
* Fixed menu auto opening on tablet device
* Fixed padding issues within price filter
* Fixed background overlap in product tables
* Fixed overflow when using marquee sections
{% endupdate %}

{% update date="2024-11-06" tags="1.0.0" %}
## 1.0.0 Keystone goes live

First release of Keystone. This is now available in the [Shopify theme store](https://themes.shopify.com/themes/keystone/styles/knit).
{% endupdate %}
{% endupdates %}
