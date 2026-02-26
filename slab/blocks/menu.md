# Menu


## Overview

A flexible menu block that renders a multi-level navigation menu with customizable styling. Supports up to three levels of navigation (parent, child, and grandchild links) with configurable typography, color, and layout options.


## Common use cases

- Add a navigation menu to your header, footer, or sidebar with customizable styling for each link level.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Menu | Select the navigation menu to display | Link list picker (default: main-menu) |

### Parent links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for parent links | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when parent font size contains 'type--'_ |
| Font size | Controls the font size of parent links | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6 |
| Font weight | Controls the font weight of parent links | &bull; Default (default)<br>&bull; Light<br>&bull; Bold<br>&bull; Black |

### Child links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for child links | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when child font size contains 'type--'_ |
| Font size | Controls the font size of child links | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6 |
| Font weight | Controls the font weight of child links | &bull; Default (default)<br>&bull; Light<br>&bull; Bold<br>&bull; Black |

### Grandchild links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for grandchild links | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when grandchild font size contains 'type--'_ |
| Font size | Controls the font size of grandchild links | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6 |
| Font weight | Controls the font weight of grandchild links | &bull; Default (default)<br>&bull; Light<br>&bull; Bold<br>&bull; Black |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Spacing above the menu | 0 – 30 px (default: 0) |
| Bottom spacing | Spacing below the menu | 0 – 30 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding around the menu | Checkbox (default: false) |
| Enable internal padding | Adds internal padding to menu items | Checkbox (default: false) |
| Gap size | Spacing between menu items | &bull; None<br>&bull; Default (default)<br>&bull; XS<br>&bull; SM<br>&bull; MD<br>&bull; LG<br>&bull; XL |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default)<br><br>_Visible when enable inheritance is disabled_ |
| Text color | Color scheme picker for custom mode | Color scheme picker<br><br>_Visible when type is "custom" and enable inheritance is disabled_ |
| Text color | Controls the text color | &bull; Default (default)<br>&bull; Alternative<br>&bull; Link<br>&bull; Error<br>&bull; Success<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br><br>_Visible when type is "base" and enable inheritance is disabled_ |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: true) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Hover style | Controls the hover effect for menu items | &bull; None (default)<br>&bull; Background<br>&bull; Fade |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Layout | Controls the menu layout direction | &bull; Stacked<br>&bull; Inline (default) |
| Horizontal alignment | Controls horizontal alignment of the menu | &bull; Left (default)<br>&bull; Center<br>&bull; Right |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
