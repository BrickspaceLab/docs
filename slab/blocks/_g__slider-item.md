# Slider item


## Overview

A slider item block that displays its content as an individual slide within a slider layout. It supports customizable width for mobile and desktop, spacing, color schemes, and responsive visibility options.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use as a child of a slider layout to create individual slides with independently sized and styled content.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds internal padding to the block | Checkbox (default: false) |
| Gap size | Spacing between child elements | &bull; None<br>&bull; Default (default)<br>&bull; Extra small<br>&bull; Small<br>&bull; Medium<br>&bull; Large<br>&bull; Extra large |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent (default) |
| Border | Border color for the block | &bull; Body foreground<br>&bull; Subtle<br>&bull; Strong<br>&bull; None (default) |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Position of the border on the block | &bull; None (default)<br>&bull; Top<br>&bull; Bottom<br>&bull; Left<br>&bull; Right<br>&bull; Top & bottom<br>&bull; Left & right<br>&bull; All |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Mobile width | Width of the slide on mobile devices | 5 – 100% (default: 80) |
| Desktop width | Width of the slide on desktop devices | 5 – 100% (default: 40) |
| Enable default width | Uses the parent container's default width setting for equal-width slides | Checkbox (default: false) |
| Vertical alignment | Vertical alignment of child content | &bull; Top<br>&bull; Middle<br>&bull; Bottom (default) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
