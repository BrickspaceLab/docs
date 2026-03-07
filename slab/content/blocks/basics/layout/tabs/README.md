# Layout tab

<figure><img src="../../../../../.gitbook/assets/image (46).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible container component that provides customizable tab layout options for child blocks. Ability to show multiple containers that can be toggled with tabs. Uses Alpine.js for tab switching functionality with smooth transitions between tab content.

## Common use cases

* Organize content into multiple tabbed sections
* Create product detail tabs (description, specifications, reviews)
* Display different content views that can be toggled
* Group related information into separate tab panels
* Use for FAQ sections or multi-step content organization

## Compatible blocks

The following blocks can be nested within this block:

* [Tab item](tab-item.md)

## Block settings

### Content

| Setting | Description                                                     | Options    |
| ------- | --------------------------------------------------------------- | ---------- |
| Tabs    | Comma-separated list of tab names (e.g., "Tab 1, Tab 2, Tab 3") | Text input |

### Spacing

| Setting                 | Description                                   | Options                                                                      |
| ----------------------- | --------------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing             | Padding space at the top of the container     | 0 - 300 px (default: 0)                                                      |
| Bottom spacing          | Padding space at the bottom of the container  | 0 - 300 px (default: 0)                                                      |
| Enable internal padding | Adds horizontal padding inside the tab header | Checkbox (default: false)                                                    |
| Gap size                | Controls spacing between tab buttons          | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting      | Description                                                | Options                                                                                                                                                                                    |
| ------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors for the tab header | <p>• Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default)</p> |
| Color border | Controls the border color                                  | <p>• Subtle (default)<br>• Strong<br><br>Visible when border position is not blank</p>                                                                                                     |

### Style

| Setting         | Description                     | Options                                                                                                                                                           |
| --------------- | ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family     | Font family for tab button text | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type--</p>                                                          |
| Font size       | Font size for tab button text   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Border position | Controls where borders appear   | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p>                                                |

### Display

| Setting          | Description                        | Options                                                                                                    |
| ---------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Adds scroll-triggered animations   | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
