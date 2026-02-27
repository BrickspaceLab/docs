# Flex grid


## Overview

A flexible container component that provides customizable flex layout options for child blocks. Enables responsive alignment, spacing, and visibility controls through the theme editor. Supports both horizontal and vertical flex directions with comprehensive alignment options.


## Common use cases

- Create flexible row or column layouts for content organization
- Use horizontal direction for side-by-side content arrangements
- Use vertical direction for stacked content layouts
- Configure gap sizes to control spacing between flex items
- Adjust alignment settings to position content within the flex container


## Compatible blocks

The following blocks can be nested within this block:

- [Flex item](flex-item.md)


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Padding space at the top of the container | 0 - 300 px (default: 0) |
| Bottom spacing | Padding space at the bottom of the container | 0 - 300 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding around the container | Checkbox (default: false) |
| Gap size | Controls spacing between flex items | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background and text colors | • Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default) |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Direction | Controls the flex direction | • Horizontal (default)<br>• Vertical |
| Horizontal alignment (row) | Controls horizontal alignment when direction is horizontal | • Left (default)<br>• Center<br>• Right<br>• Between<br><br>Visible when direction is horizontal |
| Vertical alignment (row) | Controls vertical alignment when direction is horizontal | • Start (default)<br>• Middle<br>• End<br>• Between<br>• Stretch<br><br>Visible when direction is horizontal |
| Vertical alignment (column) | Controls vertical alignment when direction is vertical | • Start (default)<br>• Middle<br>• End<br>• Between<br><br>Visible when direction is vertical |
| Horizontal alignment (column) | Controls horizontal alignment when direction is vertical | • Left<br>• Center<br>• Right<br>• Between<br>• Stretch (default)<br><br>Visible when direction is vertical |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-triggered animations | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
