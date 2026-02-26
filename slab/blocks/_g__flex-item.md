# Flex item


## Overview

A flexible container block that displays its content within a flex layout. It supports customizable width, spacing, sticky positioning, color schemes, scroll animations, and responsive visibility options.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use as a child of a flex layout to create responsive multi-column arrangements with independently sized and styled content areas.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds internal padding to the block | Checkbox (default: false) |
| Enable vertical spacing | Adds vertical spacing around the block | Checkbox (default: true) |
| Gap size | Spacing between child elements | &bull; None<br>&bull; Default (default)<br>&bull; Extra small<br>&bull; Small<br>&bull; Medium<br>&bull; Large<br>&bull; Extra large |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent (default) |
| Border | Border color for the block | &bull; Body foreground<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; None |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Position of the border on the block | &bull; None (default)<br>&bull; Top<br>&bull; Bottom<br>&bull; Left<br>&bull; Right<br>&bull; Top & bottom<br>&bull; Left & right<br>&bull; All |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Mobile width | Width of the block on mobile devices | 5 – 100% (default: 80) |
| Desktop width | Width of the block on desktop devices | 5 – 100% (default: 40) |
| Enable width fill | Allows the block to fill available space in the flex container | Checkbox (default: false) |
| Enable default width | Uses the parent container's default width setting | Checkbox (default: false) |
| Enable sticky layout | Makes the block sticky when scrolling | Checkbox (default: false) |
| Sticky position | Position where the block sticks when scrolling | &bull; None (default)<br>&bull; Top<br>&bull; Bottom |
| Vertical alignment | Vertical alignment of child content | &bull; Top<br>&bull; Middle<br>&bull; Bottom (default) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
| Scroll animation | Animation applied to the block on scroll | &bull; None (default)<br>&bull; Fade<br>&bull; Slide up<br>&bull; Slide down<br>&bull; Slide left<br>&bull; Slide right<br>&bull; Zoom |
