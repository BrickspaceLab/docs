# Button

<figure><img src="../../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable button component that renders a link styled as a button with various appearance and layout options. Supports responsive visibility controls, multiple style variants, and custom actions including overlay triggers, form submissions, and navigation.

## Common use cases

* Create call-to-action buttons throughout your theme
* Use custom actions to trigger overlays, form submissions, or JavaScript functions
* Configure button size and color to match your theme's design system
* Use full-width option for prominent mobile CTAs
* Trigger account, search, menu, or cart overlays with preset actions
* Submit forms or perform logout/login actions with custom button behavior

## Compatible blocks

The following blocks can be nested within this block:

* [Rich text](rich-text.md)
* [Icon](icon.md)
* [Image](image.md)
* [Localization label](../utility/localization-label.md)
* [Cart count](/broken/pages/I1uLikf9S6Wq0KNvGdgN)
* [Cart price](/broken/pages/4VWNibJzvJcDHosz3SNd)

## Block settings

### General

| Setting                | Description                                                                 | Options                   |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals full-width and square layout, device visibility, and scroll or load animations | Checkbox (default: false) |

### Content

| Setting                | Description                                                 | Options                                                                                                                                                                                                                                                                                           |
| ---------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| URL                    | Link destination for the button                             | <p>URL input (default: /collections/all)<br><br>Visible when enable custom action is false</p>                                                                                                                                                                                                    |
| Enable custom action   | Enables custom JavaScript actions instead of URL navigation | Checkbox (default: false)                                                                                                                                                                                                                                                                         |
| Overlay preset         | Select a preset overlay action or use custom                | <p>• None (default)<br>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Custom<br><br>Visible when enable custom action is true and enable close overlays is false and enable form submission is false and enable logout is false and enable back to top is false</p> |
| Overlay custom         | Custom overlay ID for custom overlay actions                | <p>Text input<br><br>Visible when enable custom action is true and overlay preset is custom</p>                                                                                                                                                                                                   |
| Enable close overlays  | Closes all open overlays when button is clicked             | <p>Checkbox (default: false)<br><br>Visible when enable custom action is true and enable form submission is false and enable logout is false and enable back to top is false and overlay preset is none</p>                                                                                       |
| Enable form submission | Submits the nearest form when clicked                       | <p>Checkbox (default: false)<br><br>Visible when enable custom action is true and enable close overlays is false and enable logout is false and enable back to top is false and overlay preset is none</p>                                                                                        |
| Enable logout          | Redirects to account logout URL                             | <p>Checkbox (default: false)<br><br>Visible when enable custom action is true and enable close overlays is false and enable form submission is false and enable back to top is false and overlay preset is none</p>                                                                               |
| Enable login           | Redirects to account login URL                              | <p>Checkbox (default: false)<br><br>Visible when enable custom action is true and enable close overlays is false and enable form submission is false and enable back to top is false and overlay preset is none</p>                                                                               |
| Enable back to top     | Scrolls page to top when clicked                            | <p>Checkbox (default: false)<br><br>Visible when enable custom action is true and enable close overlays is false and enable form submission is false and enable logout is false and overlay preset is none</p>                                                                                    |

### Spacing

| Setting                   | Description                               | Options                   |
| ------------------------- | ----------------------------------------- | ------------------------- |
| Enable internal padding   | Adds internal padding to the button       | Checkbox (default: true)  |
| Enable horizontal padding | Adds horizontal padding around the button | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the button        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the button     | Checkbox (default: false) |

### Color

| Setting            | Description                          | Options                                                                                                                                                         |
| ------------------ | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type               | Custom color scheme vs preset styles | <p>• Custom<br>• Base (default)</p>                                                                                                                             |
| Button (custom)    | Color scheme applied to the button   | Color scheme picker<br><br>Visible when type is **Custom**                                                                                                      |
| Button (base)      | Preset button style                  | <p>• Plain<br>• Main<br>• Blur<br>• Outline<br>• Inverted outline<br>• Text<br>• Inverted text</p><br><br>Visible when type is **Base**                           |

### Style

| Setting     | Description              | Options                                                            |
| ----------- | ------------------------ | ------------------------------------------------------------------ |
| Button size | Controls the button size | <p>• Extra small<br>• Small<br>• Standard (default)<br>• Large</p> |

### Layout

| Setting              | Description                                           | Options                                                                                       |
| -------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment of the button           | <p>• Left (default)<br>• Center<br>• Right<br><br>Visible when enable full width is false</p> |
| Enable full width    | Makes the button span the full width of its container | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>           |
| Enable square        | Uses a square footprint (useful for icon-only buttons) | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>        |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |

### Advanced motion

| Setting          | Description                          | Options                                                                                                                                                                                                                         |
| ---------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Load animation   | Animation when the block first loads | <p>• None (default)<br>• Fade<br>• Fade up<br>• Offset fade<br>• Offset fade up</p><br><br>Visible when **Show advanced settings** is on and **Scroll animation** is **None**                                                       |
| Scroll animation | Animation tied to scroll position    | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p><br><br>Visible when **Show advanced settings** is on and **Load animation** is **None**                                 |
