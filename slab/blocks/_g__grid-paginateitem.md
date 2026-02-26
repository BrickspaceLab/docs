# Grid paginate item


## Overview

A grid container block that conditionally displays its content based on a pagination index. It works with grid components to show content for specific pagination states, supporting row and column spans, color schemes, and responsive visibility.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use within a paginated grid layout to display content that appears only at a specific pagination index.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Index | The pagination index at which this block becomes visible | Number input (default: 6) |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds internal padding to the block | Checkbox (default: true) |
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

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Vertical alignment of child content | &bull; Top<br>&bull; Middle<br>&bull; Bottom (default) |
| Row span | Number of grid rows this block spans | &bull; 1 (default)<br>&bull; 2<br>&bull; 3<br>&bull; 4<br>&bull; 5<br>&bull; 6 |
| Column span | Number of grid columns this block spans | &bull; 1 (default)<br>&bull; 2<br>&bull; 3<br>&bull; 4<br>&bull; 5<br>&bull; 6 |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
