# Product gallery


## Overview

A product gallery block that displays media from a selected product in a grid layout. It supports images, videos, external videos, and 3D models with configurable aspect ratios, color schemes, and responsive device visibility settings.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use to display product media in a grid, with optional variant-based image filtering and customizable aspect ratios.


## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Show selected variant images only | Displays only images associated with the selected variant | Checkbox (default: false) |

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display media from | Product picker |
| Item count | Maximum number of media items to display | Number input (default: 7) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body (default)<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent |
| Border | Border color for the block | &bull; None<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; Body foreground |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | &bull; None (default)<br>&bull; Top<br>&bull; Bottom<br>&bull; Left<br>&bull; Right<br>&bull; Top & bottom<br>&bull; Left & right<br>&bull; All |
| Enable aspect ratio | Maintains consistent aspect ratio for all media items | Checkbox (default: false) |
| Show entire image | Displays the entire image without cropping | Checkbox (default: true) |
| Aspect ratio | Aspect ratio for media items | &bull; Square<br>&bull; Landscape<br>&bull; Portrait<br>&bull; None (default) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
