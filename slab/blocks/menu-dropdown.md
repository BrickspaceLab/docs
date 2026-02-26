# Menu dropdown


## Overview

A container component that handles menu dropdown functionality and styling. Provides a flexible menu system with support for nested links, dropdowns, and featured content blocks.


## Common use cases

* Create a multi-level navigation dropdown menu with customizable typography and colors
* Build header navigation with mega menu dropdowns
* Configure separate styles for parent, child, and grandchild links


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
| Top spacing | Top spacing in pixels | 0 - 30 px (default: 15 px) |
| Bottom spacing | Bottom spacing in pixels | 0 - 30 px (default: 15 px) |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Gap size | Spacing between content blocks within the container | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |

### Colors

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls text color mode | <p>• Custom<br>• Base (default)<br><br>Visible when enable_text_inheritance is false</p> |
| Text | Select a custom text color scheme | <p>Color scheme picker<br><br>Visible when text_color_type is custom and enable_text_inheritance is false</p> |
| Text | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3<br><br>Visible when text_color_type is base and enable_text_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |

### Layout

| Setting | Description | Options |
|---------|-------------|----------|
| Horizontal alignment | Controls horizontal alignment | <p>• Left (default)<br>• Center<br>• Right</p> |

### Parent links

| Setting | Description | Options |
|---------|-------------|----------|
| Font family | Font family for parent menu links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains type--</p> |
| Font size | Font size for parent menu links | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Enable dropdown icons | Shows dropdown indicator icons | Checkbox (default: true) |
| Enable click to open | When enabled the parent menu items will not be linked and instead act as buttons to open a dropdown. | Checkbox (default: false) |

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

### Dropdown

| Setting | Description | Options |
|---------|-------------|----------|
| Layout | Controls the dropdown layout style | <p>• Stacked (default)<br>• Inline</p> |
| Enable internal padding | Adds internal padding to the dropdown | Checkbox (default: true) |
| Enable margin | Adds margin around the dropdown | <p>Checkbox (default: true)<br><br>Visible when menu_columns is not blank</p> |
| Gap size | Spacing between items in the dropdown | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |
| Full width dropdown | Enter a comma-separated list of menu links that should display with a full width dropdown. E.g. Best sellers, Sale, New arrivals | Text input |

### Dropdown colors

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls dropdown color mode | <p>• Custom<br>• Base (default)<br><br>Visible when enable_dropdown_inheritance is false</p> |
| Scheme | Select a custom dropdown color scheme | <p>Color scheme picker<br><br>Visible when dropdown_color_type is custom and enable_dropdown_inheritance is false</p> |
| Scheme | Controls the dropdown background color | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when dropdown_color_type is base and enable_dropdown_inheritance is false</p> |
| Border | Controls the dropdown border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when dropdown_color_type is base and enable_dropdown_inheritance is false</p> |
| Divider | Controls the dropdown divider color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when dropdown_color_type is base and enable_dropdown_inheritance is false</p> |
| Enable inheritance | Inherit dropdown colors from parent | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
