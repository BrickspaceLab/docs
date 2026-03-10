# Slider gallery

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Slider](../../layout/slider/) block.

## Overview

A product media gallery component that displays a collection of media items (images, videos, 3D models) in a slider format. This block is designed to work within a slider section, supporting responsive layouts and various media types from a product.

## Common use cases

* Best used within a slider section for product galleries
* Configure appropriate widths based on your layout needs
* Consider enabling zoom functionality for product images when detail viewing is important
* Use in conjunction with navigation controls for better user experience

## Block settings

### Content

| Setting             | Description                                  | Options                   |
| ------------------- | -------------------------------------------- | ------------------------- |
| Show variant images | Shows variant-specific images in the gallery | Checkbox (default: false) |
| Product             | Product to display media from                | Product picker            |
| Item count          | Number of media items to display             | Number (default: 7)       |

### Spacing

| Setting       | Description                          | Options                 |
| ------------- | ------------------------------------ | ----------------------- |
| Width mobile  | Width of each slider item on mobile  | 5 - 100 % (default: 80) |
| Width desktop | Width of each slider item on desktop | 5 - 100 % (default: 40) |

### Color

| Setting      | Description                          | Options                                                                                                                                                                                    |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background color scheme | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Color border | Controls the border color            | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not empty</p>                                       |

### Style

| Setting         | Description                       | Options                                                                                                            |
| --------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls which sides have borders | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting             | Description                                   | Options                                                                                                |
| ------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Enable aspect ratio | Maintains a consistent aspect ratio for media | Checkbox (default: false)                                                                              |
| Show entire image   | Shows the full image without cropping         | <p>Checkbox (default: true)<br><br>Visible when enable aspect ratio is true</p>                        |
| Aspect ratio        | Aspect ratio for the media container          | <p>• Square<br>• Landscape<br>• Portrait<br>• None<br><br>Visible when enable aspect ratio is true</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
