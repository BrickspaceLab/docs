# Drawer

<figure><img src="../../../.gitbook/assets/image (53).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable drawer component that displays content in a sliding overlay panel. This component creates an interactive drawer that can be positioned at the bottom, left, or right of the screen with a button to trigger its visibility.

## Common use cases

* Use for navigation menus, filters, cart drawers, or any content that should appear on demand
* Consider the best position based on content type (e.g., filters often work well as left/right drawers)
* Ensure drawer content is accessible and navigable by keyboard
* Customize colors and borders to match your theme design

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../layout/container.md) (for drawer content)
* [Container](../layout/container.md) (for drawer footer)

## Block settings

### General

| Setting                | Description                                                                                                      | Options                   |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals close button, colors, inheritance, margin, width, full height, and device visibility                  | Checkbox (default: false) |

### Content

| Setting           | Description                                                             | Options                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset    | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID        | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is **Custom**</p>                                                                  |
| Show close button | Displays a close button in the drawer                                   | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                               |

### Color

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset surface colors             | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off                                                                                                                                     |
| Color scheme        | Background and text pairing                        | Color scheme picker<br><br>Visible when type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off                                                                                                                                |
| Color scheme        | Background and text pairing                        | <p>• Body background (default)<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent</p><br><br>Visible when type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off                                       |
| Border color        | Drawer border                                      | <p>• Subtle (default)<br>• Strong<br>• None</p><br><br>Visible when **Show advanced settings** is on, type is **Base**, and **Enable inheritance** is off                                                                                                       |
| Enable inheritance  | Inherit colors from the closest parent with a set scheme | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                     |

### Layout

| Setting             | Description                                      | Options                                                                                          |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| Horizontal position | Position of the drawer along the horizontal axis | <p>• Left<br>• Center<br>• Right (default)</p>                                                   |
| Vertical position   | Position of the drawer along the vertical axis   | <p>• Top (default)<br>• Bottom</p><br><br>Visible when horizontal position is **Center**        |
| Margin              | Outer margin around the drawer panel             | <p>• Default<br>• Narrow<br>• Standard<br>• Wide<br>• Full<br>• None (default)</p><br><br>Visible when **Show advanced settings** is on |
| Enable full height  | Makes the drawer extend to full viewport height  | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>             |
| Enable custom width | Enables a custom width percentage                | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>           |
| Width               | Drawer width                                     | <p>0–100 % (default: 35 %)<br><br>Visible when **Enable custom width** and **Show advanced settings** are on</p> |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |
