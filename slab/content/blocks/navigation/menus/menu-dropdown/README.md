# Menu dropdown

<figure><img src="../../../../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

## Overview

A container component that handles menu dropdown functionality and styling. Provides a flexible menu system with support for nested links, dropdowns, and featured content blocks. Uses Alpine.js for dropdown menu interactions and positioning, supports full-width dropdowns for specified menu columns, and handles nested menu items up to grandchild level.

## Common use cases

* Use for main navigation menus that require dropdowns
* Configure menu\_columns setting for full-width mega menus
* Add navigation images to enhance visual hierarchy
* Customize fonts and spacing to match site design
* Leverage blocks to add featured content in dropdowns

## Compatible blocks

The following blocks can be nested within this block:

* [Menu item](menu-item.md)

## Block settings

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals 10 advanced options including enable dropdown icons, enable click to open, and more | Checkbox (default: false) |

### Content

| Setting | Description                | Options                               |
| ------- | -------------------------- | ------------------------------------- |
| Menu    | Select the menu to display | Link list picker (default: main-menu) |

### Parent links

| Setting               | Description                                       | Options                                                                                                                                                           |
| --------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family           | Font family for parent menu links                 | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when parent font size contains type--</p>                                                   |
| Font size             | Font size for parent menu links                   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Enable dropdown icons | Shows chevron icons for menu items with dropdowns | Checkbox (default: true)<br><br>Visible when **Show advanced settings** is on|
| Enable click to open  | Opens dropdowns on click instead of hover only   | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|
| Enable link as button | Converts parent links with children to buttons    | Checkbox (default: false)                                                                                                                                         |

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

### Dropdown

| Setting                 | Description                                                         | Options                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Layout                  | Layout style for dropdown menus                                     | <p>• Stacked (default)<br>• Inline</p>                                                                                                                                                     |
| Enable internal padding | Adds internal padding to dropdown content                           | Checkbox (default: true)                                                                                                                                                                   |
| Enable margin           | Applies margin for full-width dropdown columns                      | Checkbox (default: true)<br><br>Visible when **Menu columns** is not blank and **Show advanced settings** is on                                                                            |
| Gap size                | Spacing between dropdown menu items                                 | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p>                                                                                                               |
| Menu columns            | Comma-separated list of menu items to display as full-width columns | Text input                                                                                                                                                                                 |

### Dropdown colors

These settings appear in the theme editor when **Show advanced settings** is on. They control the dropdown panel surface.

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset dropdown colors            | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off (dropdown colors)                                                                                                                    |
| Color scheme        | Background and text pairing                        | Color scheme picker<br><br>Visible when dropdown type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off (dropdown colors)                                                                                                      |
| Color scheme        | Preset background pairing                          | <p>• Body background (default)<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent</p><br><br>Visible when dropdown type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off (dropdown colors)          |
| Border              | Dropdown panel border                              | <p>• None<br>• Subtle (default)<br>• Strong</p><br><br>Visible when **Show advanced settings** is on, dropdown type is **Base**, and **Enable inheritance** is off (dropdown colors)                                                                           |
| Divider             | Divider between stacked dropdown items             | <p>• None<br>• Subtle (default)<br>• Strong</p><br><br>Visible when **Show advanced settings** is on, dropdown type is **Base**, and **Enable inheritance** is off (dropdown colors)                                                                           |
| Enable inheritance  | Inherit dropdown colors from the closest parent    | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                        |

### Link colors

These settings appear when **Show advanced settings** is on. They control parent, child, and grandchild link text colors.

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset link text colors           | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off (link colors)                                                                                                                        |
| Text                | Text color pairing                                 | Color scheme picker<br><br>Visible when link type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off (link colors)                                                                                                             |
| Text                | Preset text color                                  | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1–3</p><br><br>Visible when link type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off (link colors)                                     |
| Enable inheritance  | Inherit link colors from the closest parent        | <p>Checkbox (default: true)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                         |

### Spacing

| Setting                   | Description                                 | Options                                                                      |
| ------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing               | Padding space at the top of parent links    | 0 - 30 px (default: 15)                                                      |
| Bottom spacing            | Padding space at the bottom of parent links | 0 - 30 px (default: 15)                                                      |
| Enable horizontal padding | Adds horizontal padding around the menu     | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between menu items                  | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Layout

| Setting              | Description                               | Options                                        |
| -------------------- | ----------------------------------------- | ---------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment of the menu | <p>• Left (default)<br>• Center<br>• Right</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
