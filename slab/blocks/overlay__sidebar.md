# Overlay sidebar


## Overview

A sidebar overlay block that slides in from the left or right side of the screen. Supports customizable color schemes, positioning, and responsive visibility options.


## Common use cases

- Display navigation menus, filters, or supplementary content panels in a sidebar that slides in from the side of the screen.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Overlay preset | Select a preset overlay ID or use a custom one | &bull; Account<br>&bull; Search<br>&bull; Menu<br>&bull; Primary cart<br>&bull; Alternative cart<br>&bull; Quick buy<br>&bull; Quick edit<br>&bull; Custom (default) |
| Overlay ID | Custom identifier for the overlay | Text input<br><br>_Visible when overlay preset is "Custom"_ |
| Show close button | Displays a close button in the sidebar | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default)<br><br>_Visible when enable inheritance is disabled_ |
| Color scheme | Controls the color scheme | Color scheme picker<br><br>_Visible when type is "Custom" and enable inheritance is disabled_ |
| Color scheme | Controls the background and text color combination | &bull; Body<br>&bull; Accent 1 (default)<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent<br><br>_Visible when type is "Base" and enable inheritance is disabled_ |
| Border color | Controls the border color | &bull; Subtle (default)<br>&bull; Strong<br>&bull; None<br><br>_Visible when type is "Base" and enable inheritance is disabled_ |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal position | Position of the sidebar along the horizontal axis | &bull; Left<br>&bull; Right (default) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
