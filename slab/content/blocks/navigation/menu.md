# Menu

<figure><img src="../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible menu block component that renders a multi-level navigation menu with customizable styling options. Supports up to three levels of navigation (parent, child, and grandchild links) with optional thumbnail images for child and grandchild menu items.

## Common use cases

* Use stacked layout for sidebar or mobile menus
* Use inline layout for horizontal navigation bars
* Enable hover animation for interactive menus with many items
* Add thumbnail images to enhance visual navigation
* Configure different styling for each menu level to create visual hierarchy
* Adjust gap sizes based on menu density and available space

## Block settings

### Content

| Setting | Description                           | Options                               |
| ------- | ------------------------------------- | ------------------------------------- |
| Menu    | Select the navigation menu to display | Link list picker (default: main-menu) |

### Parent links

| Setting     | Description                                    | Options                                                                                                                                                           |
| ----------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for parent links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains 'type--'</p>                                       |
| Font size   | Controls the font size of parent links         | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Font weight | Controls the font weight of parent links       | <p>• Default (default)<br>• Light<br>• Bold<br>• Black</p>                                                                                                        |
| Text color  | Controls the text color of parent links        | <p>• Default (default)<br>• Alternative<br>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Shade</p>                                                     |

### Child links

| Setting     | Description                                   | Options                                                                                                                                                           |
| ----------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for child links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when child font size contains 'type--'</p>                                        |
| Font size   | Controls the font size of child links         | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Font weight | Controls the font weight of child links       | <p>• Default (default)<br>• Light<br>• Bold<br>• Black</p>                                                                                                        |
| Text color  | Controls the text color of child links        | <p>• Default (default)<br>• Alternative<br>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Shade</p>                                                     |

### Grandchild links

| Setting     | Description                                        | Options                                                                                                                                                           |
| ----------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for grandchild links | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when grandchild font size contains 'type--'</p>                                   |
| Font size   | Controls the font size of grandchild links         | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Font weight | Controls the font weight of grandchild links       | <p>• Default (default)<br>• Light<br>• Bold<br>• Black</p>                                                                                                        |
| Text color  | Controls the text color of grandchild links        | <p>• Default (default)<br>• Alternative<br>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Shade</p>                                                     |

### Spacing

| Setting                   | Description                             | Options                                                                      |
| ------------------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing               | Spacing above the menu                  | 0 - 30 px (default: 0)                                                       |
| Bottom spacing            | Spacing below the menu                  | 0 - 30 px (default: 0)                                                       |
| Enable horizontal padding | Adds horizontal padding around the menu | Checkbox (default: false)                                                    |
| Enable internal padding   | Adds internal padding to menu items     | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between menu items              | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Style

| Setting     | Description                              | Options                                           |
| ----------- | ---------------------------------------- | ------------------------------------------------- |
| Hover style | Controls the hover effect for menu items | <p>• None (default)<br>• Background<br>• Fade</p> |

### Layout

| Setting              | Description                        | Options                                        |
| -------------------- | ---------------------------------- | ---------------------------------------------- |
| Layout               | Controls the menu layout direction | <p>• Stacked<br>• Inline (default)</p>         |
| Horizontal alignment | Controls horizontal alignment      | <p>• Left (default)<br>• Center<br>• Right</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
