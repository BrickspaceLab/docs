# Progress bar


## Overview

A dynamic cart progress bar that displays visual progress toward cart-based rewards or discounts. Shows a progress bar with tier indicators and customizable messages based on cart value. Uses Alpine.js for real-time cart calculations and displays tier messages when thresholds are reached.


## Common use cases

- Encourage customers to reach free shipping thresholds
- Display progress toward discount tiers or rewards
- Show visual indicators for cart value milestones
- Customize tier messages and thresholds for different reward levels
- Use in cart drawers or checkout pages to incentivize additional purchases


## Compatible blocks

The following blocks can be nested within this block:

- [Progress tier](../progress-tier.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Progress bar calculation | Method used to calculate progress | • Subtotal<br>• Total (default) |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the progress bar | Checkbox (default: false) |
| Enable top padding | Adds top padding around the progress bar | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the progress bar | Checkbox (default: false) |
| Enable internal padding | Adds internal padding to the tier message | Checkbox (default: true) |
| Gap size | Spacing between progress bar elements | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color bar | Controls the progress bar fill color | • Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent |
| Color scheme | Controls the background and text colors for tier messages | • Body<br>• Neutral (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent |
| Color text | Controls the text color for tier messages | • Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Font family for tier messages | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type-- |
| Font size | Font size for tier messages | • Smaller<br>• Small (default)<br>• Default<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the progress bar | • Left (default)<br>• Center<br>• Justify<br>• Right |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
