# Progress bar

<figure><img src="../../../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

## Overview

A dynamic cart progress bar that displays visual progress toward cart-based rewards or discounts. Shows a progress bar with tier indicators and customizable messages based on cart value. Uses Alpine.js for real-time cart calculations and displays tier messages when thresholds are reached.

## Common use cases

* Encourage customers to reach free shipping thresholds
* Display progress toward discount tiers or rewards
* Show visual indicators for cart value milestones
* Customize tier messages and thresholds for different reward levels
* Use in cart drawers or checkout pages to incentivize additional purchases

## Compatible blocks

The following blocks can be nested within this block:

* [Progress tier](progress-tier.md)

## Block settings

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals visibility settings | Checkbox (default: false) |

### Content

| Setting                  | Description                       | Options                                |
| ------------------------ | --------------------------------- | -------------------------------------- |
| Progress bar calculation | Method used to calculate progress | <p>• Subtotal<br>• Total (default)</p> |

### Spacing

| Setting                   | Description                                     | Options                                                                      |
| ------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------- |
| Enable horizontal padding | Adds horizontal padding around the progress bar | Checkbox (default: false)                                                    |
| Enable top padding        | Adds top padding around the progress bar        | Checkbox (default: false)                                                    |
| Enable bottom padding     | Adds bottom padding around the progress bar     | Checkbox (default: false)                                                    |
| Enable internal padding   | Adds internal padding to the tier message       | Checkbox (default: true)                                                     |
| Gap size                  | Spacing between progress bar elements           | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Selects color mode | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Enable inheritance** is off |
| Bar (custom) | Custom color scheme for the progress bar fill | <p>Color scheme picker</p><br><br>Visible when **Type** is **Custom** and **Enable inheritance** is off |
| Container (custom) | Custom color scheme for the tier message container | <p>Color scheme picker</p><br><br>Visible when **Type** is **Custom** and **Enable inheritance** is off |
| Color bar | Controls the progress bar fill color | <p>• Body background<br>• Body foreground<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent</p><br><br>Visible when **Type** is **Base** and **Enable inheritance** is off |
| Color container | Controls the background color for tier messages | <p>• Body background<br>• Body foreground<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1 (default)<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent</p><br><br>Visible when **Type** is **Base** and **Enable inheritance** is off |
| Color text | Controls the text color for tier messages | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3</p><br><br>Visible when **Type** is **Base** and **Enable inheritance** is off |
| Color border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong</p><br><br>Visible when **Border position** is not **None**, **Type** is **Base**, and **Enable inheritance** is off |
| Enable inheritance | Inherits color settings from parent block | Checkbox (default: true) |

### Style

| Setting         | Description                   | Options                                                                                                                                                           |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family     | Font family for tier messages | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type--</p>                                                          |
| Font size       | Font size for tier messages   | <p>• Smaller<br>• Small (default)<br>• Default<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p>                                                |

### Layout

| Setting              | Description                                       | Options                                                     |
| -------------------- | ------------------------------------------------- | ----------------------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment of the progress bar | <p>• Left (default)<br>• Center<br>• Justify<br>• Right</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
