# Slider gallery

A product media gallery component that displays images, videos, and 3D models in a slider format. Designed for use within the slider layout block.


## Overview

Renders product media items as horizontally scrollable slider items with responsive width controls. Supports variant image filtering, aspect ratio settings, and customizable color and border styling.


## Common use cases

Use this block to display a product's media gallery in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires a product context to access media items and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and is not designed for standalone use.


## Block settings

| Setting | Description | Options |
| --- | --- | --- |
| Show selected variant images only | Filters gallery to show only images associated with the selected variant | Checkbox (default: false) |

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Product | Product to display media from | Product picker |
| Item count | Number of media items to display | Number input (default: 7) |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Mobile width | Width of each slider item on mobile | 5 – 100 % (default: 80) |
| Desktop width | Width of each slider item on desktop | 5 – 100 % (default: 40) |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Chooses between custom and base color modes | • Custom<br>• Base (default) |
| Scheme | Selects a custom color scheme | Color scheme picker |
| Background | Sets the background color | • Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent |
| Border | Sets the border color style | • None<br>• Subtle (default)<br>• Strong<br>• Body foreground |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme | Checkbox (default: false) |

### Style

| Setting | Description | Options |
| --- | --- | --- |
| Border position | Sets the position of the border | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All |
| Enable aspect ratio | Maintains a consistent aspect ratio for media items | Checkbox (default: false) |
| Show entire image | Shows the full image without cropping | Checkbox (default: true) |
| Aspect ratio | Sets the aspect ratio for the media container | • Square<br>• Landscape<br>• Portrait<br>• None (default) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
