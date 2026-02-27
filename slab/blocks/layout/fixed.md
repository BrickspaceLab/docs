# Fixed


## Overview

A flexible overlay container component that allows positioning child blocks in fixed positions on the screen corners. Supports both app and theme blocks with customizable corner positioning and z-index control. Ideal for chat widgets, promotional banners, or notification elements.


## Common use cases

- Use for floating/fixed position blocks on the screen like chat widgets, promotional banners, or notification elements
- Configure position and spacing using the block settings
- Control visibility for different device sizes


## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks


## Block settings

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds padding around the overlay content | Checkbox (default: true) |
| Gap size | Controls spacing between child blocks | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background and text colors | • Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Rotation | Rotates the overlay content | • None (default)<br>• Right 90°<br>• Left 90° |
| Horizontal position | Controls horizontal positioning of the overlay | • Left (default)<br>• Center<br>• Right |
| Vertical position | Controls vertical position as percentage from top | 0 - 100 % (default: 100) |
| Enable margin | Applies margin based on theme settings | Checkbox (default: false) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
