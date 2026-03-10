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

### Content

| Setting             | Description                                                             | Options                                                                                                                                                                                               |
| ------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset      | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Age verification<br>• Form response<br>• Discount<br>• Error<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID          | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                                                                                      |
| Show close button   | Displays a close button in the alert                                    | Checkbox (default: false)                                                                                                                                                                             |
| Enable auto close   | Automatically closes the alert after a set duration                     | Checkbox (default: false)                                                                                                                                                                             |
| Auto close duration | Time before the alert automatically closes                              | <p>1 - 10 s (default: 3)<br><br>Visible when enable auto close is true</p>                                                                                                                            |

### Color

| Setting      | Description                                        | Options                                                                                                                                                                                    |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text color combination | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color                          | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                                            |

### Layout

| Setting             | Description                                     | Options                            |
| ------------------- | ----------------------------------------------- | ---------------------------------- |
| Horizontal position | Position of the alert along the horizontal axis | <p>• Left<br>• Right (default)</p> |
| Vertical position   | Position of the alert along the vertical axis   | <p>• Top (default)<br>• Bottom</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
