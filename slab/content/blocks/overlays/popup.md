# Popup

<figure><img src="../../../.gitbook/assets/image (54).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable popup modal component that displays content in an overlay triggered by a button. Provides smooth animations, responsive behavior, and extensive styling options through block settings.

## Common use cases

* Use semantic HTML within popup content for better accessibility
* Keep popup content concise to avoid overwhelming users
* Consider mobile viewports when designing popup content
* Test keyboard navigation and screen reader compatibility
* Use appropriate color contrast for overlay background

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../layout/container.md) (for popup content)

## Block settings

### General

| Setting                | Description                                                                                         | Options                   |
| ---------------------- | --------------------------------------------------------------------------------------------------- | ------------------------- |
| Show advanced settings | Reveals close button, full background, colors, inheritance, margin, width, and device visibility | Checkbox (default: false) |

### Content

| Setting                | Description                                                             | Options                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset         | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Age verification<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID             | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is **Custom**</p>                                                                                        |
| Show close button      | Displays a close button in the popup                                    | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                     |
| Enable full background | Makes the popup background cover the entire viewport                    | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                     |

### Color

| Setting             | Description                                        | Options                                                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Type                | Custom scheme vs preset surface colors             | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Show advanced settings** is on and **Enable inheritance** is off                                                                                                                                     |
| Color scheme        | Background and text pairing                        | Color scheme picker<br><br>Visible when type is **Custom**, **Show advanced settings** is on, and **Enable inheritance** is off                                                                                                                                |
| Color scheme        | Background and text pairing                        | <p>• Body background (default)<br>• Body foreground<br>• Accent 1–3<br>• Shade 1–3<br>• Blur<br>• Transparent</p><br><br>Visible when type is **Base**, **Show advanced settings** is on, and **Enable inheritance** is off                                    |
| Border color        | Popup border                                       | <p>• Subtle (default)<br>• Strong<br>• None</p><br><br>Visible when **Show advanced settings** is on, type is **Base**, and **Enable inheritance** is off                                                                                                        |
| Enable inheritance  | Inherit colors from the closest parent with a set scheme | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                                                                                                                                  |

### Layout

| Setting             | Description                          | Options                                                                                                                                    |
| ------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Margin              | Outer margin around the popup        | <p>• Default<br>• Narrow<br>• Standard<br>• Wide<br>• Full<br>• None (default)</p><br><br>Visible when **Show advanced settings** is on      |
| Enable custom width | Enables a custom width percentage    | <p>Checkbox (default: false)<br><br>Visible when **Show advanced settings** is on</p>                                                      |
| Width               | Popup width                          | <p>0–100 % (default: 100 %)<br><br>Visible when **Enable custom width** and **Show advanced settings** are on</p>                          |

### Display

| Setting    | Description                        | Options                                                                                          |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------ |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on |
