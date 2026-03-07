# Overlay sidebar

<figure><img src="../../../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

## Overview

A configurable sidebar overlay component that can slide in from either the left or right side of the screen. Creates a responsive sidebar drawer with customizable styling, positioning, and content.

## Common use cases

* Provide a unique overlay\_id for each sidebar instance
* Use the visibility settings to control display on different device sizes
* Consider user experience when configuring close button visibility
* Create navigation menus, filters, or supplementary content panels

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../basics/containers/container.md) (for sidebar content)
* [Container](../basics/containers/container.md) (for sidebar footer)

## Block settings

### Content

| Setting           | Description                                                             | Options                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset    | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID        | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                    |
| Show close button | Displays a close button in the sidebar                                  | Checkbox (default: false)                                                                                                           |

### Color

| Setting      | Description                                        | Options                                                                                                                                                                                    |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text color combination | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color                          | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                                            |

### Layout

| Setting             | Description                                       | Options                            |
| ------------------- | ------------------------------------------------- | ---------------------------------- |
| Horizontal position | Position of the sidebar along the horizontal axis | <p>• Left<br>• Right (default)</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
