# Default grid


## Overview

A flexible grid container component that allows for dynamic layout configuration of child blocks. Supports both app and theme blocks in a responsive grid layout with customizable columns for desktop and mobile views. Ideal for product grids, image galleries, or any content that benefits from a grid structure.


## Common use cases

- Display multiple blocks in a grid layout for product grids, image galleries, or any content that benefits from a grid structure
- Configure desktop and mobile columns based on content size and screen real estate
- Use gap settings to control spacing between grid items
- Enable scroll animations for dynamic content reveals


## Compatible blocks

The following blocks can be nested within this block:

- [Grid products](../all-pagination/product-grid.md)
- [Grid articles](../all-pagination/article-grid.md)
- [Grid collections](../all-pagination/grid-collection-grid.md)
- [Grid gallery](../all-pagination/product-gallery.md)
- [Grid recommendations](../all-pagination/grid-product-recommendations.md)
- [Grid recent](../all-pagination/grid-recently-viewed.md)
- [Grid item](grid-item.md)
- All theme blocks
- App blocks


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Padding space at the top of the container | 0 - 300 px (default: 0) |
| Bottom spacing | Padding space at the bottom of the container | 0 - 300 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding around the container | Checkbox (default: false) |
| Gap size | Controls spacing between grid items | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


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
| Row desktop | Number of columns in grid on desktop | 1 - 8 (default: 5) |
| Row mobile | Number of columns in grid on mobile | 1 - 3 (default: 2) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-triggered animations | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
