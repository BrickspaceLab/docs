# Image hotspot

### Section overview

The Hotspot section displays an image with interactive overlay points that customers can click to reveal products or navigate to specific URLs.

#### Common use cases

* Showcase product features by highlighting specific areas of a product image
* Create an interactive lookbook where customers can shop directly from model images
* Display floor plans or maps with clickable navigation points
* Build guided tours highlighting important elements within an image

#### Usage tips

* Use high-resolution images that provide clear visibility of the hotspot areas
* Ensure sufficient contrast between the image and hotspot indicators
* Limit the number of hotspots to avoid overwhelming customers
* Position hotspots strategically to avoid overlap on mobile screens
* Test thoroughly on mobile to ensure hotspots remain accessible when the image scales down
* Consider using a gradient overlay to improve text visibility when placing content over images

### Section settings

| Setting                   | Description                                                                       |
| ------------------------- | --------------------------------------------------------------------------------- |
| Image background desktop  | The main background image displayed on desktop devices                            |
| Image background mobile   | A separate image optimized for mobile devices                                     |
| Show entire image         | When enabled, displays the entire image without cropping                          |
| Vertical spacing          | Controls the height of the section from extra small to extra large                |
| Color scheme              | Sets the background and text color theme for the section                          |
| Text color                | Determines the text color, with options for default, force light, or force dark   |
| Border color              | Sets the color for section borders                                                |
| Enable gradient           | Adds a gradient overlay to improve visibility of content over images              |
| Enable background overlay | Adds a background color behind text content for improved readability              |
| Border position           | Controls where borders appear (none, top, bottom, or both)                        |
| Vertical alignment        | Positions content at the top, middle, or bottom of the section                    |
| Horizontal alignment      | Aligns content to the left, center, or right of the section                       |
| Enable margin             | When enabled, adds horizontal margin to the section content                       |
| Enable max width          | Limits the content width for improved readability                                 |
| Visibility                | Controls whether the section appears on all devices, only mobile, or only desktop |

### Block settings

#### Heading

Adds a primary heading to the section.

* Block limit: 1

| Setting | Description                        |
| ------- | ---------------------------------- |
| Content | The text to display as the heading |

#### Image

Adds an image to the section content area.

* Block limit: 3

| Setting      | Description                                  |
| ------------ | -------------------------------------------- |
| Image        | The image to display within the content area |
| Image height | Controls the height of the image in pixels   |

#### Content

Adds formatted text content to the section.

* Block limit: 3

| Setting | Description                                                          |
| ------- | -------------------------------------------------------------------- |
| Content | Rich text content that can include formatting, lists, and basic HTML |

#### Buttons

Adds primary and secondary buttons to the section.

* Block limit: 1

| Setting                | Description                                  |
| ---------------------- | -------------------------------------------- |
| Button label           | The text displayed on the primary button     |
| Button URL             | The destination URL for the primary button   |
| Button color           | The style and color of the primary button    |
| Secondary button label | The text displayed on the secondary button   |
| Secondary button URL   | The destination URL for the secondary button |
| Secondary button color | The style and color of the secondary button  |

#### Product

Creates a hotspot that reveals a product card when clicked or hovered.

* Block limit: 20

| Setting             | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| Product             | The Shopify product to display when the hotspot is activated         |
| Vertical position   | The vertical position of the hotspot as a percentage from the top    |
| Horizontal position | The horizontal position of the hotspot as a percentage from the left |

#### Link

Creates a hotspot that navigates to a URL when clicked.

* Block limit: 20

| Setting             | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| Title               | The text shown in the tooltip when hovering over the hotspot         |
| URL                 | The destination URL when the hotspot is clicked                      |
| Vertical position   | The vertical position of the hotspot as a percentage from the top    |
| Horizontal position | The horizontal position of the hotspot as a percentage from the left |
