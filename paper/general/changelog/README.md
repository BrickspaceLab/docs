# Changelog

{% updates format="full" %}
{% update date="2025-02-27" tags="8.1.2" %}
## Cart note handling fixes

#### Fixes

* Fixed cart note handling, including special-character/script issues and note toggle clearing behavior

{% endupdate %}

{% update date="2025-12-12" tags="8.1.1" %}
## Product template, currency, and footer fixes

#### Fixes

* Fixed an issue where the "Learn more" link inside the product template didn't work correctly in the theme editor
* Adjusted the currency meta tag to behave correctly across multi-market stores, improving compatibility with region-specific pricing and SEO expectations
* Resolved a bug where the newsletter logo in the footer failed to appear on mobile devices

{% endupdate %}

{% update date="2025-09-29" tags="8.1.0" %}
## High-variant product support and bug fixes

#### Improvements

* Improved support for high-variant products — merchants can uncheck "Enable default variant" and force users to pick their options even on high-variant products with over 250 variants

#### Fixes

* Fixed background color settings for video section
* Fixed header bar using wrong text capitalization
* Fixed menu items not highlighting parent heading
* Fixed broken layout when returning to a paginated collection page
* Fixed cart not displaying products when using specific apps
* Fixed videos not displaying within fullscreen gallery
* Fixed text capitalization setting not being applied to headings
* Fixed minor issues with combined listing products

{% endupdate %}

{% update date="2025-09-05" tags="8.0.5" %}
## Template installation fixes

#### Fixes

* Fixed broken default settings preventing all section files from importing on installation

{% endupdate %}

{% update date="2025-08-05" tags="8.0.4" %}
## Listing preset defaults fix

#### Fixes

* Fixed broken default settings preventing all section files from importing on installation

{% endupdate %}

{% update date="2025-06-23" tags="8.0.3" %}
## Install experience and header bar fixes

#### Fixes

* Fixed listing directory with better defaults for an improved install experience
  * Removed image setting so theme is installed without images
  * Removed internal Intercom widget used on theme store
* Fixed "Enable click-to-open dropdown" not working when toggled on

{% endupdate %}

{% update date="2025-06-09" tags="8.0.2" %}
## Theme file restructure for theme store redesign

#### Improvements

* Created subfolders for preset listings
* Changed preset names in the config file
* Added the .json files matching each preset's demo store/templates and /sections into their respective subfolders

{% endupdate %}

{% update date="2025-04-14" tags="8.0.1" %}
## Mobile option selector fix

#### Fixes

* Fixed broken option selector on mobile

{% endupdate %}

{% update date="2025-04-09" tags="8.0.0" %}
## Revamped product options, high-variant support, and major bug fixes

#### Added

* Added revised header bar with more block options — multiple navigation styles can be used including full-width dropdowns, single columns, and content blocks
* Added more block types to mobile menu drawers
* Added support for high-variant products with the increased variant limit
* Added improvements to swatch rendering with more settings to fine-tune display on collection and product pages
* Added improved pagination when returning to an infinite-scrolled collection — users can "load previous" and "load next page" results
* Added better control when displaying sale prices — new setting to display sale start prices or sale ranges
* Added setting to change how cart upsells are displayed
* Added check to hide cart upsells that are already in the cart
* Added improved design of search dropdown
* Added better alt text display on product pages
* Added placeholder image to banner section
* Added better mobile support to hotspot section
* Added previous and next buttons to blog
* Added alt text to fullscreen product image gallery
* Added option to set play button text for video section
* Added new before/after image slider section

#### Changed

* Changed theme default settings to remove deprecated fonts

#### Fixes

* Updated "skip to content" button to be hidden when scrolling up
* Updated search bar to show current search term
* Fixed image sliders not allowing the user to slide through all images
* Fixed search getting cut off after opening full-screen gallery
* Fixed scroll reflow after using collection filters
* Fixed textarea field in blog comment not using correct style
* Fixed error where items get added above their quantity
* Fixed add to cart breaking when "Enable default variant" is unchecked
* Fixed pagination not working when inside theme editor
* Fixed savings badge appearing on PDP incorrectly
* Fixed inputs not inheriting parent color
* Fixed collection block text being cut off
* Fixed collection blocks not appearing on additional pages
* Fixed subtotals being shown when cart is empty
* Fixed padding around checkout "taxes included" message
* Fixed blip when showing search icon instead of input
* Fixed content shift when collection pages are loading
* Fixed content shift when using open accordions
* Fixed unexpected center alignment in collage
* Fixed product overlap with image hotspot
* Fixed layout issue with collection grid appearing more narrow
* Fixed image layout in blog articles
* Fixed line breaks not working in product descriptions
* Fixed age verification displaying when adding a product to cart
* Fixed checkboxes appearing incorrectly when using bottom border

{% endupdate %}

{% update date="2025-01-29" tags="7.6.2" %}
## Deprecated font replacements

#### Improvements

* Changed default fonts for presets, replacing deprecated fonts with recommended replacements

{% endupdate %}

{% update date="2024-10-16" tags="7.6.1" %}
## Linked products block fix

#### Fixes

* Fixed duplicate buttons on product page linked products block

{% endupdate %}

{% update date="2024-10-11" tags="7.6.0" %}
## Safari fixes, metaobject swatch support, and new sections

#### Added

* Added new setting to adjust product page gallery slider item size for both mobile and desktop
* Added new CSS to ensure consistent design of "Buy it now" buttons
* Added new tab block to show up to three tabs on product section
* Added new slider and arrow button for "Linked products" block when a page has many linked products
* Added metaobject swatch support even when the option is not labeled "colour"
* Added new fullscreen zoom gallery on product pages with more intuitive vertical scrolling
* Added new comparison table section
* Added new setting to choose whether collection filters are displayed on top or on the side
* Added new setting to change the width of items displayed in a product and collection slider
* Added support for videos as the first media in a product card

#### Changed

* Revised Liquid code with performance improvements
* Improved 3D model component on product pages
* Improved color rendering when using a dark body background
* Updated map store locator section to use Mapbox API
* Updated collection sections to use "collection_list" input for easier selection of many collections

#### Removed

* Removed default background color on some images so .PNG files appear as expected with a transparent background

#### Fixes

* Fixed content overflow issues when viewing the zoom gallery on product pages
* Fixed edit address popup not loading the correct region selector when a store has only one shipping country
* Fixed tag filtering not highlighting the current tag filter
* Fixed some structured data errors by implementing default schema
* Fixed grid gallery not showing/sliding to the correct image
* Fixed multiple video sections used on one template breaking
* Fixed vertical alignment on content cards in Collage and Slider sections
* Fixed a variety of Safari display issues

{% endupdate %}

{% update date="2024-08-29" tags="7.5.0" %}
## Translation fixes, variant strikethrough rework, and "Sign in with Shop"

#### Added

* Added Sign in with Shop button

#### Improvements

* Completely reworked how options and variants get crossed out when sold out or unavailable — now works consistently for content using special characters or letters
* Created new rating snippet file so metafields can be swapped in one place
* Added missing color settings to newsletter block in menu

#### Fixes

* Fixed video crop in product gallery
* Fixed missing image on featured product item
* Fixed missing translations in theme editor
* Fixed quick search not retrieving results using extra fields
* Fixed variant selection when options include a space
* Fixed quantity increment getting disabled incorrectly
* Fixed mobile gallery when using grid view
* Fixed special characters breaking option selection

{% endupdate %}

{% update date="2024-07-09" tags="7.4.0" %}
## Image hotspot section and reworked locale files

#### Added

* Added new section to display image hotspots

#### Improvements

* Added better-sorted language files
* Reworked Paper section locale files

#### Fixes

* Fixed star rating display
* Fixed missing variables in interface
* Fixed missing placeholders in contact forms

{% endupdate %}

{% update date="2024-06-06" tags="7.3.0" %}
## Combined listing support, discount popup, and swatch improvements

#### Added

* Added setting to toggle header dropdown behavior
* Added popup to highlight any active discounts
* Added support for Shopify combined listing app
* Added help widget with multiple blocks

#### Improvements

* Updated rating text to show half stars for decimal points
* Updated swatches to support new Shopify metafield setup
* Updated Twitter icon to x.com icon
* Revised design of blog items in search results

#### Fixes

* Fixed hover opacity applying to banners on mobile
* Fixed overlap when using zoom gallery with sticky add button
* Fixed broken YouTube embed on product page
* Fixed bug with single variant and single option products
* Fixed missing image in newsletter block
* Fixed missing translations

{% endupdate %}

{% update date="2024-04-30" tags="7.2.1" %}
## Tertiary button color, zoom level settings, and fixes

#### Added

* Added tertiary button color option to all sections
* Added "Show location and language" setting to footer
* Added support for different zoom levels to product gallery

#### Fixes

* Fixed and revised "show prices in button" setting
* Fixed alignment of star badge on product page
* Fixed underline with subtag filtering
* Fixed cart alert opening on top of cart drawer when using upsell
* Fixed "when option is not available with any variant" with dropdown
* Fixed missing prices on selling plan widget
* Improved collection template block support
* Updated pagination "page" type to include all page numbers

{% endupdate %}

{% update date="2024-04-01" tags="7.2.0" %}
## App block support for banners and mobile menu content blocks

#### Added

* Added support for app blocks within banner
* Added support for content/newsletter blocks in mobile menu
* Added improved unavailable indication setting

#### Removed

* Removed redundant/broken settings

#### Fixes

* Updated block settings for more flexibility
* Fixed broken gift card form
* Fixed product descriptions appearing behind photos when set to "left"
* Fixed product galleries not showing featured image from selected variant
* Fixed errors on customer account page
* Fixed radius not applying when showing secondary media on hover
* Fixed "Show search as icon on mobile" setting
* Fixed missing chevron icon in select form input
* Fixed missing zip code in customer account
* Fixed button layout on account verification page
* Fixed mobile video in banners
* Fixed "Buy now" buttons appearing for unavailable products
* Fixed missing setting for "Show video on mobile"

{% endupdate %}

{% update date="2024-02-28" tags="7.1.2" %}
## Quick bug fixes

#### Fixes

* Fixed missing zip code in account pages
* Fixed cart notes appearing with empty notes
* Fixed cart upsells not opening correct quick add
* Fixed image resolution on "linked products" block

{% endupdate %}

{% update date="2024-02-28" tags="7.1.1" %}
## Mobile banner image fix

#### Fixes

* Fixed missing mobile images on all banners

{% endupdate %}

{% update date="2024-02-27" tags="7.1.0" %}
## Gift card scheduling, new settings, and bug fixes

#### Added

* Added setting to enable/disable the login button in footer
* Added support for gift card scheduling
* Added option to show search icon instead of input on mobile
* Added setting to toggle review badges
* Added more customizable features to contact template

#### Changed

* Revised extra small spacing on collection banners
* Reverted to sticky position for product grid photos

#### Fixes

* Fixed error on customer account pages
* Fixed missing arrow on featured collection slider
* Fixed missing image on mobile collection banner
* Fixed image_url filters that don't contain required size
* Fixed gap on mobile Safari above product images
* Fixed awkward mobile layout on discount banner
* Fixed overlap in mobile menu drawer
* Fixed broken cart notes
* Fixed image resolution on mobile

{% endupdate %}

{% update date="2024-02-14" tags="7.0.0" %}
## Rebuilt product page, new card and price settings, and improved border controls

#### Added

* Added new product, collection, and blog card settings — split from a single setting so blog cards can be styled differently from product cards
* Added new price and revised price settings — reworked for different currencies with options to hide currency codes and remove trailing zeros
* Added new border and input settings — set border widths for form inputs, buttons, and page elements independently
* Added new setting to set the quick-add button color

#### Changed

* Updated styles so focus-state borders are only shown when navigating with a keyboard

#### Improvements

* Introduced more components to reduce code duplication using snippets for images, videos, cart items, and upsells
* Improved swatch support so color swatches appear correctly even when color options are labeled in different languages
* Improved video support so videos can autoplay on mobile where support is available

#### Fixes

* Fixed error breaking gift card page when customers do not include a gift card note
* Fixed blurry product photos on recent and recommended sliders
* Fixed product grid to avoid extra white space between product photos

{% endupdate %}

{% update date="2023-12-05" tags="6.2.0" %}
## Cart settings, shipping bar improvements, and bug fixes

#### Added

* Added viewport-specific cart settings
* Updated shipping bar with a setting to show progress based on subtotal or total

#### Changed

* Updated quick adds to show based on variant count instead of "Default title"
* Quantity selector buttons on product page are now disabled when the customer would go below 0 or above available inventory

#### Fixes

* Updated pickup availability so "Default title" is hidden
* Fixed buildUrlFilter breaking when a filter value contains an ampersand
* Fixed formatting in cart drawer error message
* Error messages are now properly localized
* Updated linked products block to avoid cutting off the selected element
* Fixed missing "Follow on Shop" button
* Fixed the price filter slider not working on Firefox
* Fixed nested mobile menu breaking when it has more items than the device height
* Fixed announcement bar alignment on mobile
* Fixed image content shift in product page grid gallery on Safari

{% endupdate %}

{% update date="2023-11-07" tags="6.1.7" %}
## Variant strikethrough and hidden option bug fixes

#### Fixes

* Fixed a bug where some variants would be wrongfully hidden
* Fixed a bug where unchecked "Enable Default Variant" setting would cause variants to be hidden
* Fixed a bug where additional strikethroughs were wrongfully assigned

{% endupdate %}

{% update date="2023-11-01" tags="6.1.6" %}
## Swatch images and sold out display fixes

#### Fixes

* Fixed missing swatch images in color filters
* Fixed a bug where sold out indications would not show up properly
* Non-existing variants will no longer be displayed

{% endupdate %}

{% update date="2023-10-25" tags="6.1.5" %}
## Variant indicator and subscription widget fixes

#### Fixes

* Fixed duplicate "popup" blocks
* Fixed unavailable variant indicator sometimes appearing incorrectly
* Fixed subscription widget sometimes showing wrong percentage discount
* Fixed variant image checkbox feature for mobile
* Small accessibility fixes

{% endupdate %}

{% update date="2023-10-11" tags="6.1.4" %}
## Store locator, currency, and subscription widget fixes

#### Fixes

* Fixed special characters breaking the store locator section
* Fixed a bug where price in cart was shown in the store's original currency
* Fixed a bug where savings badge calculations were showing the wrong percentage
* Fixed a bug where "Sold Out" text in dropdown selectors would multiply unexpectedly
* Fixed subscription widget price and selling plan bugs in quick add section

{% endupdate %}

{% update date="2023-09-27" tags="6.1.3" %}
## Clickable banner setting and section updates

#### Added

* Added setting to banner to make entire area clickable

#### Improvements

* Updated button defaults for better merchant experience
* Updated the way lazy loading is handled in banner sections
* Updated product images to go to first available image when switching variants while using multiple variant images setting
* Updated placeholder logic in collection grid and collection slider sections to use presets
* Updated structured data for products

{% endupdate %}

{% update date="2023-09-21" tags="6.1.2" %}
## Currency filter, dropdown overlap, and subscription fixes

#### Fixes

* Fixed price collection filter removing extra zeroes on stores using non-decimal currencies
* Fixed arrow overlap when using the dropdown menu above a Slideshow section
* Fixed subscription widget issues with multiple variants
* Fixed broken recent view script
* Fixed some currencies not being displayed in the correct format
* Fixed rogue JS code displaying on search page filters

{% endupdate %}

{% update date="2023-09-14" tags="6.1.1" %}
## Logo settings, subscription widget, and quantity button fixes

#### Added

* Added logo settings to both newsletter and content block in footer

#### Changed

* Updated alternative product options to only control selling plans
* Updated "subscribe and save" button to auto-select first plan

#### Fixes

* Fixed quantity buttons redirecting to cart
* Fixed recently viewed script not firing
* Fixed product template breaking when using subscription widget
* Removed help widget from theme editor

{% endupdate %}

{% update date="2023-09-05" tags="6.1.0" %}
## Improved image performance, reworked variant image setting, and new footer controls

We've done a lot of work optimizing how images are rendered in the theme and were able to see real performance gains. We also reworked how the variant-specific image setting works — no more editing alt tags on each image; just order the images and the theme figures out which to show.

#### Added

* Added better alignment settings to email sign-up section
* Added top/bottom spacing settings to all banner sections
* Added support to show color swatches in the collection filter
* Added support to move any footer block to any column
* Added new setting for collection-aware product links
* Added ability to disable quick-add on individual products

#### Changed

* Removed back in stock feature
* Improved variant-specific image setting to not use alt text
* Back to top button now appears earlier

#### Improvements

* Updated images to cut down on size and significantly improve page loading speeds
* Updated videos to render with original aspect ratio
* Updated section preview for Featured collection grid and Featured collection slider sections
* Updated product app block to use the same page margins

#### Fixes

* Fixed a subscription product bug where price would not update correctly
* Fixed border settings for footer section
* Fixed a bug where a second product form would prevent some apps from working properly
* Fixed special characters in SKU breaking the product page
* Fixed translation issue in the Recently viewed section
* Fixed subtag filtering so it works with tags that have spaces
* Fixed alignment on blog and page content

{% endupdate %}

{% update date="2023-08-10" tags="6.0.1" %}
## Post-launch fixes for 6.0.0

#### Changed

* "Starting from" now only shows if the product price varies

#### Fixes

* Fixed loading indicator on product page after product gets added to the cart
* Fixed fullscreen gallery not jumping to the correct image
* Fixed featured product section to properly add product to the cart

{% endupdate %}

{% update date="2023-08-04" tags="6.0.0" %}
## Product bundling, edit cart, and major new features

Our new update provides several significant enhancements, including the ability to bundle multiple single-variant products for sale on a single page. The new "Edit Cart" feature lets customers adjust product options without deleting and re-adding items.

#### Added

* Added new setting to select aspect ratio in the Video section
* Added support to include videos in the Slider section
* Added new product block to link products together as variants
* Added new collection template with filters displayed along the left-hand side
* Added new Slideshow banner section
* Added new Promo banner section
* Added new cart drawer feature to edit items — customers can change product options without deleting and re-adding
* Added a variety of new settings to fine-tune how prices are displayed — remove trailing zeros, optionally hide the currency symbol
* Added new back in stock feature — customers that share their email are tagged with the variant ID of the sold-out product
* Added support to display product blocks in the left or right column
* Added option to disable default product option selector when using a third-party subscription app
* Added new bundling feature to sell multiple single-variant products on a single page

#### Changed

* Changed all support links to point to the revamped help center
* Changed support integration with custom help widget using Intercom

#### Fixes

* Fixed open graph image tags not correctly linking to selected images
* Fixed section previews when clicking "Add section"
* Fixed mobile bar color on iOS Safari devices to use correct color
* Fixed wrong price appearing in recommendation slider
* Fixed product options breaking with special characters
* Fixed structured data breaking with special characters
* Fixed missing translations for gift card form
* Improved sold-out indicators by crossing out unavailable options while users make their selection
* Improved product page performance by removing lazy loading on the first product image
* Improved the Collage section so each block has a larger click area
* Improved product upsell block to be hidden when no upsells are available
* Updated Featured product section to avoid updating the URL with the selected variant ID

{% endupdate %}

{% update date="2023-05-03" tags="5.2.0" %}
## Announcement bar delay, typography fixes, and bug fixes

#### Added

* Added automatic delay to scroll to the announcement bar

#### Changed

* Revised underline offset in typography CSS
* Revised scroll snapping property

#### Fixes

* Fixed filters breaking when using special characters
* Fixed incorrect price displayed on recently viewed items
* Fixed URL parameters being overwritten
* Fixed minor cart visual issues
* Fixed Lighthouse error for duplicate IDs
* Fixed missing translations

{% endupdate %}

{% update date="2023-05-03" tags="5.1.0" %}
## Gift card recipient support, price visibility controls, and padding settings

This patch introduces the newly supported Shopify gift card recipient feature, letting customers send gift cards to their friends directly. Also added more settings for granular control over when and how prices are shown.

#### Added

* Added support for new Shopify feature: Gift card recipient
* Added setting to always show checkout subtotals/discounts in cart
* Added setting to control visibility of prices within buttons
* Added top and bottom padding settings to missing sections

#### Changed

* Revised product page borders
* Revised product template image galleries to be sticky
* Added price ranges instead of min price to product pages
* Revised max width on featured image in header bar

#### Fixes

* Fixed full-screen image gallery from showing indicators for videos
* Fixed vertical alignment of text in Collage and Slider sections
* Fixed missing "page" results from mobile quick search
* Improved mobile filters by closing filter popup after changing filters

{% endupdate %}

{% update date="2023-04-20" tags="5.0.1" %}
## Bug fixes and default font revisions

#### Fixes

* Fixed product page images cropping with fill setting on
* Fixed unclickable buttons when using dynamic header and filters
* Fixed logo list image alignment
* Fixed page refresh when resetting password
* Fixed account forms redirection after creating account
* Fixed missing translation for "Live-search in your header…" and "Something went wrong…"
* Fixed formatting on upsell and search items
* Fixed formatting on blog thumbnails
* Fixed store locator on mobile
* Fixed missing translation for checkout button on cart page
* Fixed variant title issues when there are special characters
* Fixed the "Buy now" button color to show selected secondary color
* Fixed column span for newsletter block
* Revised default fonts
* Revised and cleaned up theme settings with links to help docs

{% endupdate %}

{% update date="2023-04-03" tags="5.0.0" %}
## Cart behavior controls, audio feedback, and device visibility settings

We're happy to present another major update to the Paper theme — lots of new functionality including audio feedback for key interactions and more options to customize your customer's shopping experience.

#### Added

* Added an option to show a "Continue shopping" button below checkout
* Added an option to change the behavior of the cart buttons (go to cart page or open cart drawer)
* Added an option to add-to-cart behavior (open drawer, display alert, or redirect to cart page)
* Added option to display SKU next to product title on product page
* Added option to show unavailable variant options
* Added settings to enable borders on product images
* Added device visibility setting to all standard sections
* Added support for custom button text
* Added setting to enable audio feedback for key interactions
* Added video support to content grid

#### Changed

* Reworked theme sliders for a more consistent and bug-free experience
* Reworked header position settings
* Revised animations across all sections and templates
* Updated progress bar to work with currency conversions
* Updated product upsell block so image/title can be linked to product page
* Updated product option block so a popup window can be included next to option label

#### Fixes

* Fixed product gallery option to "Show selected variant images only"
* Fixed missing dollar sign in price filter
* Fixed extra spacing on custom product fields
* Fixed countdown timer button so it can be correctly hidden
* Fixed selling plan groups being hidden when only one option is available
* Fixed a bug where subscriptions would not display properly
* Fixed a bug where "choose options" button would appear when it shouldn't
* Fixed menu overlap on tablet devices
* Fixed cart visibility when scrolling with dynamic header
* Fixed content shift on mobile when scrolled with dynamic header
* Fixed cart notes not being updated
* Fixed the gap from the footer causing layout shift on mobile
* Fixed minor bugs with banners
* Various minor accessibility fixes and improvements

{% endupdate %}

{% update date="2023-02-16" tags="4.1.1" %}
## Performance improvements and bug fixes

#### Improvements

* Minor performance improvements
* Updated presets on demo stores
* Minor settings revisions

#### Fixes

* Fixed spacing issues around options block
* Fixed bug that caused search bar to work improperly
* Fixed overflow of text in quick add section

{% endupdate %}

{% update date="2023-02-16" tags="4.1.0" %}
## Search suggestions and predictive search support

#### Added

* Added support for search suggestions
* Added new global settings to set what fields predictive search uses

#### Changed

* Revised spacing in product options
* Revised line-height for headings

#### Fixes

* Fixed extra preset block in theme announcement section
* Fixed so options appears as a default block in product and featured product sections
* Fixed missing translations
* Fixed broken mobile formatting on upsell items
* Fixed so the correct description is used for the meta tag on collection templates
* Fixed product images not swapping when using dropdown option selectors
* Fixed issue where scrolling would get randomly locked
* Fixed mobile menu overlap

{% endupdate %}

{% update date="2023-02-02" tags="4.0.0" %}
## Store locator section, global alignment settings, and new product blocks

Lots of new updates and features — new store locator section, and improved alignment so almost everything can be set to left, center, or right.

#### Added

* Added new Store locator section
* Added checkbox to banner sections to enable/disable lazy loading
* Added checkbox to banner sections to prevent theme from cropping images
* Added border settings to Featured product section
* Added new account login icon
* Added checkbox to enable/disable "Show second image on hover"
* Added option to display SKU on product thumbnails
* Added option to display a short description under each product thumbnail using metafields
* Added new global alignment settings to adjust grid gap sizing
* Added new product block for customer product customizations
* Added more horizontal alignment settings throughout the entire theme
* Updated all images to support focal point feature
* Updated product zoom gallery with better zoom and navigation actions
* Updated to support section groups

#### Changed

* Revised some accent colors for better contrast
* Revised spacing in active filters on desktop
* Revised spacing around quick add on mobile
* Improved dropdown desktop nav from disappearing too early

#### Fixes

* Fixed bug where content blocks would not show up in footer unless a newsletter block is also being used
* Fixed thumbnails in the product gallery from breaking layout when many photos are used
* Fixed cart alert timer bar overlapping the alert container
* Fixed icons preventing search fields from being clickable
* Fixed bold text appearing correctly in richtext sections when using a light font
* Fixed image height issue on search and cart items in Safari
* Fixed login buttons appearing when accounts are disabled
* Fixed content and slider sections breaking when including a link in body content
* Fixed content grid when block span extends over the grid size
* Fixed left alignment in icon grid
* Fixed bug preventing variants from being changed

{% endupdate %}

{% update date="2023-01-10" tags="3.0.2" %}
## Countdown timer section and color switcher fix

#### Added

* Added new countdown timer section

#### Fixes

* Fixed color toggle to use device setting instead of forcing color theme from theme settings

{% endupdate %}

{% update date="2023-01-05" tags="3.0.1" %}
## Post-launch fixes for 3.0.0

#### Fixes

* Fixed height settings for the alternative banner — the height was applied to the image rather than the entire section, causing content to shift below fold on mobile
* Fixed borders in footer where a dark background color is used — borders now use the set color within accordions

{% endupdate %}

{% update date="2023-01-04" tags="3.0.0" %}
## Icon grid section, color variant swatches, age verification, and new banner options

New sections, new features, better design, and bug fixes to start the year.

#### Added

* Added new icon grid section to highlight key store details
* Added new alternative banner section with image and text split horizontally
* Added new block settings to existing banner section with ability to set up to two buttons
* Added new section to include an age verification popup
* Added new section to include a "Back to top" button when scrolling to bottom
* Added support to display color variants as swatch buttons with custom image uploads
* Added setting to navigation slider so it can be shown on mobile only
* Added translated text for top languages (EN, FR, IT, DE, ES)

#### Changed

* Revised border layouts for header dropdown to fit larger navigation links

#### Removed

* Removed background color from images that should be displayed with transparent backgrounds

#### Fixes

* Improved promo blocks on collection and product grids — merchants can now have promo blocks span multiple columns, include custom colors, and add background images
* Fixed missing arrows for featured image sliders in the header dropdown
* Fixed rating badges showing extra decimal points
* Fixed all sliders skipping some slides when they have a larger width
* Fixed content overlapping issues when setting header to sticky
* Fixed videos when hovering on a product thumbnail not correctly filling the border area
* Fixed some text elements using incorrect font families

{% endupdate %}

{% update date="2022-12-05" tags="2.0.0" %}
## Savings badge, sticky header, thumbnail gallery, and design improvements

#### Added

* Added automatic badge to product thumbnails to highlight percent or dollar savings
* Added new feature to set header bar as sticky
* Added stock count to product thumbnails
* Added a new product gallery option to display images with thumbnails

#### Changed

* Improved variant button selector design with better active state
* Updated product page alt text to only display visually when feature is enabled and alt text has been customized
* Updated video sections to use native HTML5 video rather than Vimeo embeds
* Updated to support CSS grid-gap for more consistent spacing
* Implemented minor design tweaks to pickup availability block
* Included more developer notes and comments in theme code
* Moved slider arrows on most sections to avoid overlapping and crowding images

#### Removed

* Removed "Edge to edge" grid setting
* Removed default background color on images so transparent .png images behave as expected

#### Fixes

* Fixed some thumbnails not using correct font families from theme settings
* Fixed slider margins with less-than-ideal design
* Fixed product upsell block not working
* Fixed vendor names displaying incorrectly in search
* Fixed bug causing add-to-cart to break when variants have spaces
* Fixed bug causing checkout button formatting issues on cart template
* Fixed typography settings not correctly applying to some header bar text

{% endupdate %}

{% update date="2022-11-14" tags="1.2.2" %}
## Product title special character fix

#### Fixes

* Fixed symbols in product titles not being escaped properly, which caused accidental rendering of x-data on the product page

{% endupdate %}

{% update date="2022-11-09" tags="1.2.1" %}
## Contact form 404 fix

#### Fixes

* Fixed contact form bug that was causing the form to 404

{% endupdate %}

{% update date="2022-10-27" tags="1.2.0" %}
## Vertical spacing controls, product recommendations intent setting, and new upsell block

This update introduces more vertical spacing controls so merchants can fine-tune spacing as needed, and new settings to support the intent property for the Product Recommendations API.

#### Added

* Added vertical spacing controls to almost all sections and blocks
* Added a new setting to the product recommendation section to set intent to either "recommended" or "complementary"
* Added new block to product section to include product up-sells or cross-sells
* Added a new color setting to match the mobile bar color to the announcement bar
* Added a new border setting for "none" to theme-wide sections
* Added a new preset for hardware and department stores
* Added border options to all blocks on a product template

#### Changed

* Changed styling of presets to accommodate recent changes
* Updated border styling in the footer section
* Updated newsletter grid item to display full width
* Updated content block design under "add to cart" on product pages
* Updated banner sections to let merchants upload videos directly
* Improved height options for banners to better fit different device sizes
* Reduced size of search bar on mobile for a cleaner feel

#### Removed

* Removed "Default Title" from sticky add to cart bar

#### Fixes

* Fixed favicons not appearing
* Fixed blog thumbnails not correctly applying theme radius styles
* Fixed logo appearing slightly off center on mobile
* Fixed cart upsell arrows breaking when an item is unavailable
* Fixed bug causing weird grid alignment on recently viewed sections
* Fixed bug causing weird layout on mobile when using the "grid" product gallery
* Fixed bugs causing text color to overlap with background color on some sections

{% endupdate %}

{% update date="2022-10-11" tags="1.0.0" %}
## Paper goes live

Paper's first release on the Shopify Theme Store.
{% endupdate %}
{% endupdates %}
