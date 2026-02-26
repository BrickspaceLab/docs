# Menu page


## Overview

A dynamic menu container component that creates a multi-level navigation menu with hover and click interactions. Supports up to three levels of navigation (parent, child, and grandchild links) with customizable styling and optional thumbnail images for menu items.


## Common use cases

* Create a page-style navigation menu with slide-in sub-pages for child links
* Build mobile-friendly navigation with animated page transitions
* Configure separate typography for each menu level


## Compatible blocks

The following blocks can be nested within this block:

* [Menu item](_g__menu-item.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| Menu | Select the navigation menu to display | Link list picker (default: main-menu) |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable padding | Adds padding around the content | Checkbox (default: false) |
| Enable internal padding | Adds internal padding to the menu page content | Checkbox (default: true) |
| Gap size | Spacing between content blocks within the container | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |

### Parent links

| Setting | Description | Options |
|---------|-------------|----------|
| Font family | Font family for parent menu links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains type--</p> |
| Font size | Font size for parent menu links | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Enable dropdown icons | Shows dropdown indicator icons | Checkbox (default: true) |

### Child links

| Setting | Description | Options |
|---------|-------------|----------|
| Font family | Font family for child menu links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when child font size contains type--</p> |
| Font size | Font size for child menu links | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Grandchild links

| Setting | Description | Options |
|---------|-------------|----------|
| Font family | Font family for grandchild menu links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when grandchild font size contains type--</p> |
| Font size | Font size for grandchild menu links | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
