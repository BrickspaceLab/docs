# Main product

### Section overview

The main product section is the core container for product template content. It initializes product state, renders product-related blocks, and provides shared controls for spacing, colors, borders, and visibility.

#### Common use cases

* Building the default product detail page layout.
* Combining media, options, pricing, and purchase controls in one section.
* Applying page-level background and spacing styles for product templates.
* Controlling desktop and mobile visibility from section settings.

#### Usage tips

* Always select a product resource before finalizing layout and content.
* Keep spacing and gap settings balanced so buy actions remain above the fold.
* Use background media sparingly to avoid reducing product content readability.
* Test variant, quantity, and purchase flows after block reordering.

### Section settings

| Setting | Description |
| --- | --- |
| Product | Selects the product resource used by this section. |
| Enable default variant | Preselects a default variant on load. |
| Enable background image or video | Turns on background media rendering for the section. |
| Image background desktop | Background image used on desktop. |
| Image background mobile | Optional background image override for mobile. |
| Video background | Optional background video source. |
| Show video on mobile | Enables background video playback on mobile devices. |
| Show entire image | Displays full image rather than cropping to fill. |
| Top spacing | Adds top padding to the section container. |
| Bottom spacing | Adds bottom padding to the section container. |
| Minimum height | Sets a minimum section height. |
| Gap size | Controls spacing between child layout elements. |
| Color scheme | Sets section background and text color treatment. |
| Color border | Sets section border color style. |
| Border position | Controls where borders appear. |
| Vertical alignment | Aligns content vertically within the section. |
| Enable margin | Applies global horizontal margin settings. |
| Enable header overlap | Allows section to overlap the header when enabled globally. |
| Scroll snap align | Applies scroll snap alignment when enabled globally. |
| Visibility | Controls device visibility (all, mobile, or desktop). |

### Block settings

The section supports product-specific blocks plus theme and app blocks. Common product blocks include:

* `product-media`
* `product-options`
* `product-price`
* `product-buy`
* `product-badges`
* `product-swatches`
* `shop-pay-installments`
