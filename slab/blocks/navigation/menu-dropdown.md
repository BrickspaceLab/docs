# Menu dropdown


## Overview

A container component that handles menu dropdown functionality and styling. Provides a flexible menu system with support for nested links, dropdowns, and featured content blocks. Uses Alpine.js for dropdown menu interactions and positioning, supports full-width dropdowns for specified menu columns, and handles nested menu items up to grandchild level.


## Common use cases

- Use for main navigation menus that require dropdowns
- Configure menu_columns setting for full-width mega menus
- Add navigation images to enhance visual hierarchy
- Customize fonts and spacing to match site design
- Leverage blocks to add featured content in dropdowns


## Compatible blocks

The following blocks can be nested within this block:

- [Menu item](menu-item.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Menu | Select the menu to display | Link list picker (default: main-menu) |


### Parent links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Font family for parent menu links | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains type-- |
| Font size | Font size for parent menu links | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |
| Enable dropdown icons | Shows chevron icons for menu items with dropdowns | Checkbox (default: true) |
| Enable link as button | Converts parent links with children to buttons | Checkbox (default: false) |


### Child links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Font family for child menu links | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when child font size contains type-- |
| Font size | Font size for child menu links | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |


### Grandchild links

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Font family for grandchild menu links | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when grandchild font size contains type-- |
| Font size | Font size for grandchild menu links | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |


### Dropdown

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Background and text color scheme for dropdown | • Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent |
| Color border | Border color for dropdown | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None |
| Layout | Layout style for dropdown menus | • Stacked (default)<br>• Inline |
| Color divider | Divider color between stacked dropdown items | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None |
| Enable internal padding | Adds internal padding to dropdown content | Checkbox (default: false)<br><br>Visible when dropdown is not full-width |
| Enable margin | Applies margin based on theme settings | Checkbox (default: true)<br><br>Visible when menu columns is not blank |
| Gap size | Spacing between dropdown menu items | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |
| Menu columns | Comma-separated list of menu items to display as full-width columns | Text input |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Padding space at the top of parent links | 0 - 30 px (default: 15) |
| Bottom spacing | Padding space at the bottom of parent links | 0 - 30 px (default: 15) |
| Enable horizontal padding | Adds horizontal padding around the menu | Checkbox (default: false) |
| Gap size | Spacing between menu items | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the menu | • Left (default)<br>• Center<br>• Right |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
