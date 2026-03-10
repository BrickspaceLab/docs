# Overlay

## Overview

A flexible overlay container component that allows positioning child blocks in fixed positions on the screen corners. Supports both app and theme blocks with customizable corner positioning and z-index control. Ideal for chat widgets, promotional banners, or notification elements.

## Common use cases

* Use for floating/fixed position blocks on the screen like chat widgets, promotional banners, or notification elements
* Configure position and spacing using the block settings
* Control visibility for different device sizes

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

### Spacing

| Setting        | Description                             | Options                                                                      |
| -------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Enable padding | Adds padding around the overlay content | Checkbox (default: true)                                                     |
| Gap size       | Controls spacing between child blocks   | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank</p>                                       |

### Style

| Setting         | Description                   | Options                                                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting             | Description                                       | Options                                              |
| ------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| Rotation            | Rotates the overlay content                       | <p>• None (default)<br>• Right 90°<br>• Left 90°</p> |
| Horizontal position | Controls horizontal positioning of the overlay    | <p>• Left (default)<br>• Center<br>• Right</p>       |
| Vertical position   | Controls vertical position as percentage from top | 0 - 100 % (default: 100)                             |
| Enable margin       | Applies margin based on theme settings            | Checkbox (default: false)                            |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
