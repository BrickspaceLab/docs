# Cart drawer

### Section overview

The Cart section manages the display and functionality of the shopping cart in your Shopify store, providing both overlay and sidebar cart options with customizable appearance and features.

#### Common use cases

* Creating a slide-out cart drawer for a seamless shopping experience
* Displaying cart items, subtotals, and checkout options
* Adding upsell products or promotional content to the cart interface
* Providing shipping threshold indicators with progress bars

#### Usage tips

* Choose between overlay and sidebar cart styles based on your store's design
* Customize color schemes for the top, main, and bottom areas of the cart
* Use cart blocks to add empty cart messaging, announcements, or promotional content
* Consider mobile responsiveness by testing both drawer styles (the mobile view defaults to bottom positioning)
* For upsell features, carefully select products that complement items typically added to cart

### Section settings

| Setting                       | Description                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------- |
| Top color scheme              | Sets the background and text color for the top section of the cart drawer.    |
| Top color border              | Determines the border style for the top section of the cart drawer.           |
| Primary background            | Sets the main background color for the cart drawer content area.              |
| Secondary background          | Sets the secondary background color for alternating elements within the cart. |
| Main color border             | Determines the border style for the main content area of the cart.            |
| Enable cart notes             | Allows customers to add notes to their order during checkout.                 |
| Enable cart share             | Enables cart sharing functionality.                                           |
| Enable cart SKU               | Shows product SKUs in the cart items list.                                    |
| Show cart subtotals           | Displays subtotal prices for individual line items.                           |
| Bottom color scheme           | Sets the background and text color for the bottom section of the cart drawer. |
| Bottom color border           | Determines the border style for the bottom section of the cart drawer.        |
| Bottom color button           | Sets the style for buttons in the bottom section of the cart.                 |
| Cart button behavior          | Determines whether the primary button leads to checkout or cart page.         |
| Optional text                 | Adds disclaimer or promotional text below the checkout buttons.               |
| Show continue shopping button | Displays a button to continue shopping below the checkout button.             |
| Show button prices            | Shows prices on the checkout and cart buttons.                                |

### Block settings

#### Empty cart

Displays content when the cart is empty, providing a message and call-to-action for customers.

* Block limit: 1

| Setting               | Description                                                    |
| --------------------- | -------------------------------------------------------------- |
| Heading               | Sets the heading text for the empty cart message.              |
| Content               | Provides detailed messaging for when the cart is empty.        |
| Button label          | Sets the text for the call-to-action button.                   |
| URL                   | Determines where the button links to when clicked.             |
| Image                 | Adds a featured image to the empty cart display.               |
| Image background      | Adds a background image behind content.                        |
| Video                 | Adds a video to the empty cart display.                        |
| Enable video autoplay | Automatically plays the video when visible.                    |
| Enable mute button    | Shows a button to toggle sound for the video.                  |
| Enable video loop     | Continuously loops the video.                                  |
| Minimum height        | Sets the minimum height for the empty cart content area.       |
| Enable padding        | Adds padding around the empty cart content.                    |
| Color scheme          | Sets the background and text color for the empty cart message. |
| Color border          | Determines the border style for the empty cart message.        |
| Color button          | Sets the style for the call-to-action button.                  |
| Enable gradient       | Applies a gradient effect to the background.                   |
| Vertical alignment    | Controls the vertical positioning of content.                  |
| Horizontal alignment  | Controls the horizontal positioning of content.                |
| Text position         | Determines whether text appears above or below media.          |

#### Announcement

Displays an announcement message at the top of the cart drawer.

* Block limit: 1

| Setting              | Description                                                   |
| -------------------- | ------------------------------------------------------------- |
| Content              | Sets the text for the announcement message.                   |
| Color scheme         | Sets the background and text color for the announcement.      |
| Horizontal alignment | Controls the horizontal positioning of the announcement text. |

#### Upsell checkbox

Adds a checkbox upsell for a specific product variant that can be added to cart.

* Block limit: 1

| Setting    | Description                                                      |
| ---------- | ---------------------------------------------------------------- |
| Variant ID | The Shopify variant ID for the product to be upsold.             |
| Label      | The text describing the upsell offer shown next to the checkbox. |

#### Upsell featured

Displays featured products as upsell recommendations in the cart.

* Block limit: 1

| Setting    | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| Collection | Selects a collection of products to display as upsell recommendations. |

#### Content

Adds custom content sections within the cart drawer.

* Block limit: 5

| Setting               | Description                                               |
| --------------------- | --------------------------------------------------------- |
| Heading               | Sets the heading text for the content block.              |
| Content               | Provides the main text for the content block.             |
| Button label          | Sets the text for the call-to-action button.              |
| URL                   | Determines where the button links to when clicked.        |
| Image                 | Adds a featured image to the content block.               |
| Image background      | Adds a background image behind content.                   |
| Video                 | Adds a video to the content block.                        |
| Enable video autoplay | Automatically plays the video when visible.               |
| Enable mute button    | Shows a button to toggle sound for the video.             |
| Enable video loop     | Continuously loops the video.                             |
| Minimum height        | Sets the minimum height for the content block.            |
| Enable padding        | Adds padding around the content.                          |
| Color scheme          | Sets the background and text color for the content block. |
| Color border          | Determines the border style for the content block.        |
| Color button          | Sets the style for the call-to-action button.             |
| Enable gradient       | Applies a gradient effect to the background.              |
| Vertical alignment    | Controls the vertical positioning of content.             |
| Horizontal alignment  | Controls the horizontal positioning of content.           |
| Text position         | Determines whether text appears above or below media.     |

#### Progress bar

Displays a progress bar showing how close the customer is to reaching a threshold for promotions like free shipping.

* Block limit: 1

| Setting         | Description                                                        |
| --------------- | ------------------------------------------------------------------ |
| Threshold       | The amount that must be reached to complete the progress bar.      |
| Calculation     | Determines whether to use cart subtotal or total for calculations. |
| Success message | The message displayed when the threshold has been reached.         |
