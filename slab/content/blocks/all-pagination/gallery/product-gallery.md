---
index: 0
---

# Product gallery

## Overview

A grid gallery block that displays media from a selected product. It iterates through the selected product's media to display images, videos, external videos, and 3D models. The block is highly customizable, supporting various styling options including color schemes, border configurations, and responsive visibility settings.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

To filter or reorder images by variant, use the gallery inside the **Product** section and select the same product in both settings.

## Common use cases

* Always select a product in the theme editor to populate the gallery with media
* Adjust item\_count to control the number of media items displayed in the gallery
* Utilize enable\_aspect\_ratio and aspect\_ratio settings to maintain consistent media proportions across different devices
* Experiment with color\_scheme, color\_border, and border\_position for visual customization to match the theme's aesthetic
* Use visibility options to create responsive layouts, showing different gallery configurations on mobile and desktop
* Use variant image filtering to show media for the selected option.

## Group media by variant

1. In Shopify, assign each variant its featured image. To include more media for an option, add a tag at the end of its alt text, such as `Blue shirt from the back #Color_Blue`. Use your product's actual option name and value.
2. In **Product gallery** or **Slider gallery**, turn on **Show selected variant images only**. Media with no variant assignment or recognized tag stays visible for all variants.
3. Preview the product and change variants to check the images. Filtering is available for products with fewer than 50 variants.

## Open media full screen

**Enable full screen gallery** is on by default. Customers can click or tap a photo, or use the full-screen button on a video or 3D model. The viewer opens on that item and follows the gallery’s variant filtering. **Item count** limits the inline gallery. Customers can see additional media in the full-screen view.

The viewer scrolls horizontally on desktop and vertically on mobile. Customers can also use **Previous**, **Next**, or the arrow keys to browse, and **Close** or **Esc** to return to the page.

## Block settings

### General

| Setting                | Description                                 | Options                   |
| ---------------------- | ------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals device visibility for the gallery | Checkbox (default: false) |

### Content

| Setting               | Description                                               | Options                   |
| --------------------- | --------------------------------------------------------- | ------------------------- |
| Show selected variant images only | Filter media for the selected variant on products with fewer than 50 variants. | Checkbox (default: false) |
| Move selected variant image first | Works independently of image filtering on products with fewer than 50 variants. | Checkbox (default: true) |
| Product               | Select the product to display media from                  | Product picker            |
| Item count            | Number of media items to display inline (0 = all media)          | Number input (default: 7) |
| Show alt text         | Shows each image’s alt text under the media when set      | Checkbox (default: false) |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank</p>                                       |

### Style

| Setting         | Description                   | Options                                                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting             | Description                                           | Options                                                                                                |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Enable aspect ratio | Maintains consistent aspect ratio for all media items | Checkbox (default: false) |
| Enable full screen gallery | Open the selected media in a full-screen viewer. | Checkbox (default: true) |
| Enable zoom on hover | Magnify images when customers hover over them. | Checkbox (default: false) |
| Show entire image   | Displays entire image without cropping                | <p>Checkbox (default: true)<br><br>Visible when enable aspect ratio is true</p>                        |
| Aspect ratio        | Aspect ratio for media items                          | <p>• Square<br>• Landscape<br>• Portrait<br>• None<br><br>Visible when enable aspect ratio is true</p> |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |
