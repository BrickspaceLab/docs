# Product media


## Overview

A product media block that renders product images or videos with hover effects, aspect ratio control, and flexible styling. Automatically detects and handles both image and video media types from the product's media collection.


## Common use cases

- Display product images with optional secondary image hover effects on product pages and product cards.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display media for | Product picker |
| Show second image on hover | Displays the second product image when hovering over the first | Checkbox (default: true) |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the media | Checkbox (default: false) |
| Enable top padding | Adds top padding above the media | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the media | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Color scheme | Controls the color scheme | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Background | Controls the background color | &bull; Body<br>&bull; Accent 1 (default)<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent<br><br>_Visible when type is "Base"_ |
| Border color | Controls the border color | &bull; None<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; Body foreground<br><br>_Visible when border position is not "None" and type is "Base"_ |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | &bull; None (default)<br>&bull; Top<br>&bull; Bottom<br>&bull; Left<br>&bull; Right<br>&bull; Top and bottom<br>&bull; Left and right<br>&bull; All |
| Radius | Controls the border radius of the media | &bull; None<br>&bull; Default (default)<br>&bull; SM<br>&bull; MD<br>&bull; LG<br>&bull; XL<br>&bull; 2XL<br>&bull; Full |
| Enable aspect ratio | Forces the media to maintain a specific aspect ratio | Checkbox (default: false) |
| Show entire image | Uses object-contain instead of object-cover to show full image | Checkbox (default: true)<br><br>_Visible when enable aspect ratio is enabled_ |
| Aspect ratio | The aspect ratio to maintain | &bull; Square<br>&bull; Landscape<br>&bull; Portrait<br>&bull; None<br><br>_Visible when enable aspect ratio is enabled_ |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
