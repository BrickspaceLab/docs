# Alert

<figure><img src="../../../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

## Overview

An alert overlay component that displays content in a floating panel that can be positioned at different corners of the screen. Supports auto-close functionality with visual progress indicator, customizable appearance, and responsive behavior.

## Common use cases

* Use for temporary notifications, messages, or calls-to-action
* Keep content concise as the alert has limited space
* Consider accessibility when choosing colors and auto-close timing
* Display important announcements or promotional messages
* Provide user feedback for actions

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../layout/container.md) (for alert content)

## Block settings

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals 8 advanced options including show close button, type, and more | Checkbox (default: false) |

### Content

| Setting             | Description                                                             | Options                                                                                                                                                                                               |
| ------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset      | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Age verification<br>• Form response<br>• Discount<br>• Error<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID          | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                                                                                      |
| Show close button   | Displays a close button in the alert                                    | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|
| Enable auto close   | Automatically closes the alert after a set duration                     | Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on|
| Auto close duration | Time before the alert automatically closes                              | <p>1 - 10 s (default: 3)<br><br>Visible when enable auto close is true</p><br><br>Visible when **Enable auto close** is on and **Show advanced settings** is on|

### Color

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset surface colors             | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off                                                                                                                                     |
| Color scheme        | Background and text pairing                        | Color scheme picker<br><br>Visible when type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off                                                                                                                                |
| Color scheme        | Background and text pairing                        | <p>• Body background (default)<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent</p><br><br>Visible when type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off                                       |
| Border color        | Alert border                                       | <p>• Subtle (default)<br>• Strong<br>• None</p><br><br>Visible when **Show advanced settings** is on, type is **Base**, and **Enable inheritance** is off                                                                                                       |
| Enable inheritance  | Inherit colors from the closest parent with a set scheme | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                     |

### Layout

| Setting             | Description                                     | Options                            |
| ------------------- | ----------------------------------------------- | ---------------------------------- |
| Horizontal position | Position of the alert along the horizontal axis | <p>• Left<br>• Right (default)</p> |
| Vertical position   | Position of the alert along the vertical axis   | <p>• Top (default)<br>• Bottom</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
