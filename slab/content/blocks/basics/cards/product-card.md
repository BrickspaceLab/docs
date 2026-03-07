# Product card

<figure><img src="../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible product card block for displaying a single product and its associated content blocks. This block is designed to be used within grid or slider layouts and supports a wide range of content types, including rich text, images, videos, icons, product price, badges, swatches, and media. The block offers extensive customization options for spacing, color scheme, border style, layout, and responsive visibility, making it suitable for various merchandising and design needs.

## Common use cases

* Use within grid or slider sections to create product galleries or featured product displays
* Configure the content blocks to highlight key product information, such as price, badges, and media
* Adjust spacing and color settings to match your theme's design language and improve visual hierarchy
* Use the visibility settings to tailor the product card display for different devices and layouts
* Leverage scroll animations to add engaging motion effects to product cards

## Compatible blocks

The following blocks can be nested within this block:

* App blocks
* [Rich text](../rich-text.md)
* [Image](../image.md)
* [Icon](../icon.md)
* [Divider](../layout/divider.md)
* [Tags](../../navigation/tags.md)
* [Container](../containers/container.md)
* [Button](../button.md)
* [Video](../video.md)
* [Quick buy](../../products/quick-buy-button.md)
* [Price](../../products/price.md)
* [Inventory](../../products/inventory-availability.md)
* [Badges](../../products/badges.md)
* [Swatches](../../products/swatches.md)
* [Product media](../../products/product-media.md)
* [Slider](../layout/slider/)
* [Grid](../layout/default-grid/)
* [Flex](../layout/flex-grid/)

## Block settings

### Content

| Setting | Description                   | Options        |
| ------- | ----------------------------- | -------------- |
| Product | Select the product to display | Product picker |

### Spacing

| Setting                   | Description                                     | Options                                                                      |
| ------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- |
| Enable horizontal padding | Adds horizontal padding around the product card | Checkbox (default: false)                                                    |
| Enable vertical padding   | Adds vertical padding around the product card   | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between content blocks within the card  | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None</p>                                                                                        |

### Style

| Setting                 | Description                                              | Options                                                                                                            |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position         | Controls where borders appear                            | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |
| Show underline on hover | Displays an underline effect when hovering over the card | Checkbox (default: false)                                                                                          |

### Display

| Setting          | Description                                      | Options                                                                                                    |
| ---------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible               | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Animation effect when the card scrolls into view | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
