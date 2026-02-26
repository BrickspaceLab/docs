# Tab item


## Overview

A tab item block that displays its content when its corresponding tab is selected. It works with tab navigation systems and supports customizable spacing, color schemes, and responsive visibility options.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use as a child of a tab layout to create tabbed content sections where each tab reveals different nested content.


## Compatible blocks

The following blocks can be nested within this block:

- Any theme block
- Any app block


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Tab | Unique identifier for this tab that must match the tab name in the parent tabs block | Text input |
| Show as default tab | Displays this tab's content by default when the page loads | Checkbox (default: false) |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding to the tab content | Checkbox (default: false) |
| Enable vertical padding | Adds vertical padding to the tab content | Checkbox (default: true) |
| Gap size | Spacing between child elements | &bull; None<br>&bull; Default (default)<br>&bull; Extra small<br>&bull; Small<br>&bull; Medium<br>&bull; Large<br>&bull; Extra large |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Scheme | Color scheme picker for custom mode | Color scheme picker |
| Scheme | Color scheme for the block | &bull; Body<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent (default) |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
