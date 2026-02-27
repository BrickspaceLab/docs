# Float


## Overview

A float block that wraps other theme or app blocks and positions them absolutely according to x and y coordinate settings. Supports responsive positioning for different desktop and mobile layouts with rotation effects for dynamic floating content.


## Common use cases

- Position blocks at specific coordinates on the page for floating elements like tooltips, badges, or overlays
- Ensure the parent container has position: relative for proper positioning
- Use responsive positioning for different desktop and mobile layouts
- Apply rotation effects for dynamic floating content


## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks


## Block settings

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background and text colors | • Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default) |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |
| Enable color difference | Applies mix-blend-difference for visual contrast | Checkbox (default: false) |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |


### Layout (desktop)

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Vertical position percentage on desktop | 0 - 100 % (default: 50) |
| Horizontal alignment | Horizontal position percentage on desktop | 0 - 100 % (default: 50) |
| Width | Width of the floating block as viewport percentage | 5 - 100 % (default: 30) |
| Rotation | Rotation angle in degrees | 0 - 360 deg (default: 15) |


### Layout (mobile)

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Vertical position percentage on mobile | 0 - 100 % (default: 50) |
| Horizontal alignment | Horizontal position percentage on mobile | 0 - 100 % (default: 50) |
| Width | Width of the floating block as viewport percentage | 5 - 100 % (default: 70) |
| Rotation | Rotation angle in degrees | 0 - 360 deg (default: 15) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-triggered animations | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
