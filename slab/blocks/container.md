# Container


## Overview

A flexible container block that holds other theme or app blocks with configurable spacing, gap size, and display visibility options.


## Common use cases

* Group and style nested blocks with backgrounds, spacing, and color schemes
* Create layout sections with background images or videos
* Build card-style containers with borders and rounded corners
* Use as a layout wrapper for complex block arrangements


## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| URL | Set a URL to make the entire section clickable. Using this while adding links within the section may break the layout. | URL input |
| Enable background image or video | Enable background image or video | Checkbox (default: false) |
| Desktop background | 2800 x 1200px recommended. | <p>Image picker<br><br>Visible when enable background image or video</p> |
| Mobile background | 760 x 1010px recommended. | <p>Image picker<br><br>Visible when enable background image or video</p> |
| Background video | Background video | <p>Video picker<br><br>Visible when enable background image or video</p> |
| Show video on mobile | Shows the background video on mobile | <p>Checkbox (default: true)<br><br>Visible when enable background image or video</p> |
| Show entire image | Shows the entire image within the container | <p>Checkbox (default: false)<br><br>Visible when enable background image or video</p> |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Top spacing | Top spacing in pixels | 0 - 300 px (default: 0 px) |
| Bottom spacing | Bottom spacing in pixels | 0 - 300 px (default: 0 px) |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable vertical padding | Adds vertical padding | Checkbox (default: false) |
| Enable margin | Adds margin around the block | Checkbox (default: false) |
| Gap size | Spacing between content blocks within the container | <p>• None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large</p> |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when border_position is not  and color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: false) |
| Enable color difference | Colors are inverted when this block overlaps any other content. | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All</p> |
| Radius | Controls the border radius | <p>• None<br>• Default (default)<br>• Small<br>• Medium<br>• Large<br>• 1x Large<br>• 2x Large<br>• Full</p> |
| Enable crop | Clips content that extends beyond the container. | Checkbox (default: true) |
| Enable shadow | Adds a shadow effect | Checkbox (default: false) |

### Layout

| Setting | Description | Options |
|---------|-------------|----------|
| Width | Controls the width of the block | 5 - 100 % (default: 100 %) |
| Minimum height | Minimum height of the block | <p>0 - 1200 px (default: 0 px)<br><br>Visible when enable_height_fill is false</p> |
| Enable height fill | Fill the container to the height of the parent container. | Checkbox (default: true) |
| Enable overlay | The container will be displayed on top of the parent block. | Checkbox (default: false) |
| Show on hover | Opens on hover instead of click | Checkbox (default: false) |
| Enable block elevation | Elevates the block above surrounding content | Checkbox (default: false) |
| Enable sticky layout | Makes the block sticky when scrolling | Checkbox (default: false) |
| Sticky position | To use this setting, ensure 'Enable height fill' is disabled. | <p>• None (default)<br>• Top<br>• Bottom<br><br>Visible when enable_sticky_layout is true</p> |
| Vertical alignment | Controls vertical alignment | <p>• Top (default)<br>• Middle<br>• Bottom</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
| Scroll animation | Controls how the block appears when scrolled into view. | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
