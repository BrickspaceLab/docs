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

### Content

| Setting                | Description                                                             | Options                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overlay preset         | Select a preset overlay ID or use a custom one                          | <p>• Account<br>• Search<br>• Menu<br>• Primary cart<br>• Alternative cart<br>• Age verification<br>• Quick buy<br>• Quick edit<br>• Custom (default)</p> |
| Overlay ID             | Custom identifier for the overlay (used to trigger it programmatically) | <p>Text input<br><br>Visible when overlay preset is "Custom"</p>                                                                                          |
| Show close button      | Displays a close button in the popup                                    | Checkbox (default: false)                                                                                                                                 |
| Enable full background | Makes the popup background cover the entire viewport                    | Checkbox (default: false)                                                                                                                                 |

### Color

| Setting      | Description                                        | Options                                                                                                                                                                                    |
| ------------ | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text color combination | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color                          | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                                            |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
