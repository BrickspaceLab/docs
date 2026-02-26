# Collection card


## Overview

A flexible collection card block for displaying a single collection and its associated content blocks. This block is designed to be used within grid or slider layouts and supports a wide range of content types, including rich text, images, videos, icons, and collection-specific information. The block offers extensive customization options for spacing, color scheme, border style, layout, and responsive visibility, making it suitable for various merchandising and design needs.


## Common use cases

* Display a linked collection with customizable content blocks inside grid or slider layouts
* Configure the content blocks to highlight key collection information
* Adjust spacing and color settings to match your theme design


## Compatible blocks

The following blocks can be nested within this block:

* App blocks
* [Rich text](richtext.md)
* [Image](image.md)
* [Icon](icon.md)
* [Divider](divider.md)
* [Tags](_tags.md)
* [Container](layout/container.md)
* [Button](button.md)
* [Video](video.md)
* [Slider](layout__slider.md)
* [Default grid](layout__grid.md)
* [Flex grid](layout__flex.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| Collection | Select the collection to display | Collection picker |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable vertical padding | Adds vertical padding | Checkbox (default: false) |
| Gap size | Spacing between content blocks within the container | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All</p> |
| Radius | Controls the border radius | <p>• None<br>• Default (default)<br>• Small<br>• Medium<br>• Large<br>• 1x Large<br>• 2x Large<br>• Full</p> |
| Show underline on hover | Displays an underline effect when hovering | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
| Scroll animation | Controls how the block appears when scrolled into view. | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
