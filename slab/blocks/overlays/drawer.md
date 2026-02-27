# Overlay drawer

## Overview

A customizable drawer component that displays content in a sliding overlay panel. This component creates an interactive drawer that can be positioned at the bottom, left, or right of the screen with a button to trigger its visibility.

## Common use cases

* Use for navigation menus, filters, cart drawers, or any content that should appear on demand
* Consider the best position based on content type (e.g., filters often work well as left/right drawers)
* Ensure drawer content is accessible and navigable by keyboard
* Customize colors and borders to match your theme design

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../containers/container.md) (for drawer content)
* [Container](../containers/container.md) (for drawer footer)

## Block settings

### Content

| Setting           | Description                                                             | Options                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset    | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID        | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                    |
| Show close button | Displays a close button in the drawer                                   | Checkbox (default: false)                                                                                                           |

### Color

| Setting      | Description                                        | Options                                                                                                                                                                                    |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text color combination | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color                          | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                                            |

### Layout

| Setting             | Description                                      | Options                                        |
| ------------------- | ------------------------------------------------ | ---------------------------------------------- |
| Horizontal position | Position of the drawer along the horizontal axis | <p>• Left<br>• Center<br>• Right (default)</p> |
| Vertical position   | Position of the drawer along the vertical axis   | <p>• Top (default)<br>• Bottom</p>             |
| Enable full height  | Makes the drawer extend to full viewport height  | Checkbox (default: false)                      |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
