# Menu page

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

## Overview

A dynamic menu container component that creates a multi-level navigation menu with hover and click interactions. Supports up to three levels of navigation (parent, child, and grandchild links) with customizable styling and optional thumbnail images for menu items. Uses Alpine.js for menu interaction handling and includes hover and focus states with configurable timing.

## Common use cases

* Create multi-level navigation menus with parent, child, and grandchild links
* Use consistent image sizes for navigation thumbnails (recommended 64px)
* Configure menu depth and content for optimal mobile usability
* Keep menu labels concise for better layout
* Test hover/click interactions across different devices
* Use dropdown icons for better UX when submenus are present

## Compatible blocks

The following blocks can be nested within this block:

* [Menu item](menu-dropdown/menu-item.md)

## Block settings

### Content

| Setting | Description                | Options                               |
| ------- | -------------------------- | ------------------------------------- |
| Menu    | Select the menu to display | Link list picker (default: main-menu) |

### Parent links

| Setting               | Description                                       | Options                                                                                                                                                           |
| --------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family           | Font family for parent menu links                 | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains type--</p>                                                   |
| Font size             | Font size for parent menu links                   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Enable dropdown icons | Shows chevron icons for menu items with dropdowns | Checkbox (default: true)                                                                                                                                          |

### Child links

| Setting     | Description                      | Options                                                                                                                                                           |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Font family for child menu links | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when child font size contains type--</p>                                                    |
| Font size   | Font size for child menu links   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Grandchild links

| Setting     | Description                           | Options                                                                                                                                                           |
| ----------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Font family for grandchild menu links | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when grandchild font size contains type--</p>                                               |
| Font size   | Font size for grandchild menu links   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Page

| Setting      | Description                                    | Options                                                                                                                                                         |
| ------------ | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Color scheme | Background and text color scheme for menu page | <p>• Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary</p> |
| Color border | Border color for menu page                     | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                 |

### Spacing

| Setting                 | Description                           | Options                                                                      |
| ----------------------- | ------------------------------------- | ---------------------------------------------------------------------------- |
| Enable padding          | Adds padding around the menu          | Checkbox (default: false)                                                    |
| Enable internal padding | Adds internal padding to menu content | Checkbox (default: true)                                                     |
| Gap size                | Spacing between menu items            | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
