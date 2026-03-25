# Sidebar

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

* [Container](../layout/container.md) (for sidebar content)
* [Container](../layout/container.md) (for sidebar footer)

## Block settings

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals 6 advanced options including show close button, type, and more | Checkbox (default: false) |

### Content

| Setting           | Description                                                             | Options                                                                                                                             |
| ----------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset    | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID        | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                    |
| Show close button | Displays a close button in the sidebar                                  | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|

### Color

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset surface colors             | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off                                                                                                                                     |
| Color scheme        | Background and text pairing                        | Color scheme picker<br><br>Visible when type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off                                                                                                                                |
| Color scheme        | Background and text pairing                        | <p>• Body background (default)<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent</p><br><br>Visible when type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off                                       |
| Border color        | Sidebar border                                     | <p>• Subtle (default)<br>• Strong<br>• None</p><br><br>Visible when **Show advanced settings** is on, type is **Base**, and **Enable inheritance** is off                                                                                                       |
| Enable inheritance  | Inherit colors from the closest parent with a set scheme | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                     |

### Layout

| Setting             | Description                                       | Options                            |
| ------------------- | ------------------------------------------------- | ---------------------------------- |
| Horizontal position | Position of the sidebar along the horizontal axis | <p>• Left<br>• Right (default)</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
