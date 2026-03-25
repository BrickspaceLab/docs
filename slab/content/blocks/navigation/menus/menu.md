# Menu

<figure><img src="../../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

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

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals 10 advanced options including top spacing, bottom spacing, and more | Checkbox (default: false) |

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
| Top spacing               | Spacing above the menu                  | 0 - 30 px (default: 0)<br><br>Visible when **Show advanced settings** is on|
| Bottom spacing            | Spacing below the menu                  | 0 - 30 px (default: 0)<br><br>Visible when **Show advanced settings** is on|
| Enable horizontal padding | Adds horizontal padding around the menu | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|
| Enable internal padding   | Adds internal padding to menu items     | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|
| Gap size                  | Spacing between menu items              | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p><br><br>Visible when **Show advanced settings** is on|

### Color

These settings appear in the theme editor when **Show advanced settings** is on.

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset text colors                | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off                                                                                                                                     |
| Text                | Text color pairing                                 | Color scheme picker<br><br>Visible when type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off                                                                                                                                |
| Text                | Preset text color                                  | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1–3</p><br><br>Visible when type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off                                                           |
| Enable inheritance  | Inherit colors from the closest parent with a set scheme | <p>Checkbox (default: true)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                    |

### Style

| Setting     | Description                              | Options                                           |
| ----------- | ---------------------------------------- | ------------------------------------------------- |
| Hover style | Controls the hover effect for menu items | <p>• None (default)<br>• Background<br>• Fade</p><br><br>Visible when **Show advanced settings** is on|

### Layout

| Setting              | Description                        | Options                                        |
| -------------------- | ---------------------------------- | ---------------------------------------------- |
| Layout               | Controls the menu layout direction | <p>• Stacked<br>• Inline (default)</p>         |
| Horizontal alignment | Controls horizontal alignment      | <p>• Left (default)<br>• Center<br>• Right</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
