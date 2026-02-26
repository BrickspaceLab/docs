# Menu item


## Overview

A menu item block that renders content within a navigation menu dropdown. It provides a container for nested theme and app blocks that display when the corresponding menu item is selected.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use to add custom content such as featured products, images, or promotions to navigation menu dropdowns.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Menu | Key that matches the parent menu item handle | Text input |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable vertical padding | Adds vertical padding inside the container | Checkbox (default: false) |
| Gap size | Spacing between child elements | &bull; None<br>&bull; Default (default)<br>&bull; Extra small<br>&bull; Small<br>&bull; Medium<br>&bull; Large<br>&bull; Extra large |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body (default)<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent |
| Border | Border color for the block | &bull; Body foreground<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; None |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Position of the border on the block | &bull; None (default)<br>&bull; Top<br>&bull; Bottom<br>&bull; Left<br>&bull; Right<br>&bull; Top & bottom<br>&bull; Left & right<br>&bull; All |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
