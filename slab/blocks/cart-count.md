# Cart count


## Overview

A cart count indicator that displays the current number of items in the cart. Supports inline or floating badge layout with configurable position, and dynamically updates using Alpine.js.


## Common use cases

- Display the number of items in the cart as a badge on or near the cart icon
- Use floating layout to position the count badge precisely over a cart icon
- Configure a digit limit to prevent oversized indicators (e.g., "99+" instead of "100")
- Use inline layout for text-based cart count displays


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Digit limit | Maximum number of digits before truncation | Number input (default: 2) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Button color | Controls the color style of the count badge | • Plain (default)<br>• Main<br>• Blur<br>• Outline<br>• Inverted outline<br>• Transparent<br>• Inverted transparent |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for the count | • Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--' |
| Font size | Controls the font size of the count | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |
| Radius | Controls the border radius of the count badge | • None<br>• Default (default)<br>• Small<br>• Medium<br>• Large<br>• 1x Large<br>• 2x Large<br>• Full |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Layout | Controls the positioning layout of the count | • Float<br>• Inline (default) |
| Horizontal position | Horizontal offset for float layout | 0 - 100 % (default: 55)<br><br>Visible when layout is float |
| Vertical position | Vertical offset for float layout | 0 - 100 % (default: 0)<br><br>Visible when layout is float |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
