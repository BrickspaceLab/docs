# Cart drawer

### Section overview

The cart section is responsible for rendering and handling the functionality of the cart in a Shopify store. It includes a slide-out cart drawer, an alert cart overlay, and manages the display of cart items, upsells, subtotal, and checkout options.

#### Common use cases

* Providing a seamless checkout experience without leaving the current page
* Displaying cart items, subtotals, and discounts in a visually appealing format
* Offering upsell opportunities to increase average order value
* Implementing free shipping thresholds with progress bars

#### Usage tips

* Use the progress bar to encourage customers to reach free shipping thresholds
* Leverage upsell blocks to promote complementary products
* Keep the cart visually consistent with your store's design using color scheme settings
* For mobile responsiveness, the cart adapts to smaller screens with a bottom slide-up drawer instead of a side drawer on desktop

### Section settings

| Setting                       | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| Color scheme (top)            | Sets the color scheme for the top bar of the cart drawer             |
| Color border (top)            | Sets the border color style for the top bar                          |
| Primary background            | Sets the main background color for the cart drawer                   |
| Secondary background          | Sets the background color for item rows and sections within the cart |
| Color border (main)           | Sets the border color style for dividers between cart sections       |
| Enable cart notes             | Allows customers to add notes to their order                         |
| Enable cart share             | Enables the option for customers to share their cart with others     |
| Enable cart SKU               | Shows product SKUs in the cart items list                            |
| Color scheme (bottom)         | Sets the color scheme for the bottom checkout area                   |
| Color border (bottom)         | Sets the border color style for the bottom area                      |
| Color button                  | Sets the button style for the checkout/cart button                   |
| Cart button behavior          | Determines whether the primary button links to checkout or cart page |
| Optional text                 | Displays disclaimer text below the checkout button                   |
| Show continue shopping button | Shows an additional button to continue shopping                      |
| Show button prices            | Displays the cart total on the checkout button                       |
| Show cart subtotals           | Shows the subtotal, discount, and total information                  |

### Block settings

#### Empty cart

Displays content when the cart is empty to encourage shopping.

* Block limit: 1

| Setting                  | Description                                                 |
| ------------------------ | ----------------------------------------------------------- |
| Heading                  | Sets the heading text for the empty cart message            |
| Content                  | Sets the content text for the empty cart message            |
| Button label             | Sets the text for the call-to-action button                 |
| URL                      | Sets the destination link for the button                    |
| Image                    | Optional image to display with the empty cart message       |
| Show image as background | Toggles between showing the image as a background or inline |
| Video                    | Optional video to display with the empty cart message       |
| Enable autoplay          | Automatically plays the video when visible                  |
| Enable mute toggle       | Shows a button to toggle video sound                        |
| Enable loop              | Plays the video continuously on a loop                      |
| Minimum height           | Sets the minimum height for the empty cart content area     |
| Enable padding           | Adds padding around the empty cart content                  |
| Color scheme             | Sets the color scheme for the empty cart content            |
| Color border             | Sets the border style for the empty cart content            |
| Color text               | Sets the text color treatment for the empty cart content    |
| Color button             | Sets the button style for the empty cart content            |
| Enable gradient          | Applies a gradient effect to the background                 |
| Y alignment              | Sets the vertical alignment of the content                  |
| X alignment              | Sets the horizontal alignment of the content                |

#### Announcement

Displays an announcement message at the top of the cart.

* Block limit: 1

| Setting      | Description                                            |
| ------------ | ------------------------------------------------------ |
| Content      | Sets the announcement message text                     |
| Color scheme | Sets the color scheme for the announcement bar         |
| X alignment  | Sets the horizontal alignment of the announcement text |

#### Upsell checkbox

Adds a checkbox option to add an additional product to the cart.

* Block limit: 1

| Setting            | Description                                       |
| ------------------ | ------------------------------------------------- |
| Checkbox upsell ID | The variant ID of the product to add when checked |
| Label              | The text label displayed next to the checkbox     |

#### Upsell featured

Shows featured products as upsell opportunities in the cart.

* Block limit: 1

| Setting     | Description                                                       |
| ----------- | ----------------------------------------------------------------- |
| Collection  | Selects the collection containing products to display as upsells  |
| Upsell type | Chooses between slider, stacked, or second column display formats |

#### Content

Displays custom content in the cart, such as promotions or announcements.

* Block limit: 5

| Setting                  | Description                                                 |
| ------------------------ | ----------------------------------------------------------- |
| Heading                  | Sets the heading text for the content block                 |
| Content                  | Sets the main text content                                  |
| Button label             | Sets the text for the call-to-action button                 |
| URL                      | Sets the destination link for the button                    |
| Image                    | Optional image to display with the content                  |
| Show image as background | Toggles between showing the image as a background or inline |
| Video                    | Optional video to display with the content                  |
| Enable autoplay          | Automatically plays the video when visible                  |
| Enable mute toggle       | Shows a button to toggle video sound                        |
| Enable loop              | Plays the video continuously on a loop                      |
| Minimum height           | Sets the minimum height for the content block               |
| Enable padding           | Adds padding around the content                             |
| Color scheme             | Sets the color scheme for the content block                 |
| Color border             | Sets the border style for the content block                 |
| Color text               | Sets the text color treatment for the content block         |
| Color button             | Sets the button style for the content block                 |
| Enable gradient          | Applies a gradient effect to the background                 |
| Text position            | Sets whether text appears above or below media              |
| Y alignment              | Sets the vertical alignment of the content                  |
| X alignment              | Sets the horizontal alignment of the content                |

#### Progress bar

Shows a progress bar towards free shipping or other threshold-based goals.

* Block limit: 1

| Setting                  | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| Progress bar threshold   | The amount in dollars required to reach the goal                      |
| Progress bar calculation | Determines whether to use subtotal or total for threshold calculation |
| Progress bar success     | The message displayed when the threshold is reached                   |
