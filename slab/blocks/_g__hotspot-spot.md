# Spot


## Overview

A hotspot spot block that positions nested content at configurable coordinates on a hotspot image. It supports independent positioning and sizing for mobile and desktop viewports along with optional entrance animations.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use to create interactive hotspot markers on images that reveal product details, descriptions, or other content at precise positions.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body (default)<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Enable animations | Enables entrance animations for the hotspot | Checkbox (default: false) |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Vertical position of the hotspot on desktop | 0 – 100% (default: 20) |
| Horizontal alignment | Horizontal position of the hotspot on desktop | 0 – 100% (default: 20) |
| Width | Width of the hotspot content area on desktop | 20 – 800px (default: 300) |

### Layout mobile

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Vertical position of the hotspot on mobile | 0 – 100% (default: 20) |
| Horizontal alignment | Horizontal position of the hotspot on mobile | 0 – 100% (default: 20) |
| Width | Width of the hotspot content area on mobile | 5 – 400px (default: 250) |
