# Grid gallery

## Overview

A grid gallery block that displays media from a selected product. It iterates through the selected product's media to display images, videos, external videos, and 3D models. The block is highly customizable, supporting various styling options including color schemes, border configurations, and responsive visibility settings.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Always select a product in the theme editor to populate the gallery with media
* Adjust item\_count to control the number of media items displayed in the gallery
* Utilize enable\_aspect\_ratio and aspect\_ratio settings to maintain consistent media proportions across different devices
* Experiment with color\_scheme, color\_border, and border\_position for visual customization to match the theme's aesthetic
* Use visibility options to create responsive layouts, showing different gallery configurations on mobile and desktop
* Enable variant images to show different images based on selected product variants

## Block settings

### General

| Setting                | Description                                               | Options                   |
| ---------------------- | --------------------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals device visibility for the gallery                 | Checkbox (default: false) |
| Enable variant images  | Shows different images based on selected product variants | Checkbox (default: false) |

### Content

| Setting    | Description                                      | Options                   |
| ---------- | ------------------------------------------------ | ------------------------- |
| Product    | Select the product to display media from         | Product picker            |
| Item count | Number of media items to display (0 = all media) | Number input (default: 7) |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Selects color mode | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Enable inheritance** is off |
| Scheme | Custom color scheme picker | <p>Color scheme picker</p><br><br>Visible when **Type** is **Custom** and **Enable inheritance** is off |
| Color scheme | Controls the background and text colors | <p>• Body background (default)<br>• Body foreground<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent</p><br><br>Visible when **Type** is **Base** and **Enable inheritance** is off |
| Color border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong</p><br><br>Visible when **Border position** is not **None**, **Type** is **Base**, and **Enable inheritance** is off |
| Enable inheritance | Inherits color settings from parent block | Checkbox (default: false) |

### Style

| Setting             | Description                                           | Options                                                                                                            |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position     | Controls where borders appear                         | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |
| Enable aspect ratio | Maintains consistent aspect ratio for all media items | Checkbox (default: false)                                                                                          |
| Enable zoom hover   | Enables zoom effect on image hover                    | Checkbox (default: false)                                                                                          |
| Show alt text       | Shows each image’s alt text under the media           | Checkbox (default: false)                                                                                          |
| Show entire image   | Displays entire image without cropping                | <p>Checkbox (default: true)<br><br>Visible when **Enable aspect ratio** is on</p>                                  |
| Aspect ratio        | Aspect ratio for media items                          | <p>• Square<br>• Landscape<br>• Portrait<br>• None<br><br>Visible when **Enable aspect ratio** is on</p>           |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |
