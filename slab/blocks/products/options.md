# Options


## Overview

A comprehensive product variant selection block that provides flexible display options for product options including colors, sizes, and other variants. The block supports both button-based and dropdown-based selection interfaces, with advanced features like swatches, tooltips, and unavailability indicators. It integrates with Alpine.js for interactive behavior and handles complex variant logic including availability checking and option state management.


## Common use cases

- Use button selection for better user experience when you have few variant options
- Enable swatches for color options to provide visual selection feedback
- Consider using unavailable indication to guide customers toward available variants
- Use grid layout when displaying many options to maintain organized appearance
- Configure appropriate gap sizes based on your design system and available space
- Enable tooltips for swatch-only displays to show option names on hover
- Test responsive behavior to ensure smooth transitions between desktop dropdowns and mobile drawers
- Ensure proper styling of disabled states when using unavailability indicators


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display options for | Product picker |
| Variant selection | Controls how non-swatch variants are displayed | • Buttons (default)<br>• Dropdowns |
| Unavailable indication | Controls how unavailable variants are indicated | • None<br>• Empty (default)<br>• Selected |
| Show labels | Displays labels for each option | Checkbox (default: true) |


### Swatches

| Setting | Description | Options |
|---------|-------------|---------|
| Swatch selection | Controls how swatch options (colors) are displayed | • Buttons (default)<br>• Dropdowns |
| Show swatch | Displays color swatches for color options | Checkbox (default: true) |
| Show tooltip | Displays tooltips showing option names on swatch hover | Checkbox (default: true)<br><br>Visible when swatch selection is "buttons" |
| Show labels | Displays text labels with swatches | Checkbox (default: false) |
| Layout | Controls the layout of swatch and label | • Stacked<br>• Inline (default)<br><br>Visible when show labels is true |
| Size | Size of the swatch indicators | 8 - 120 px (default: 16)<br><br>Visible when show swatch is true |
| Radius | Border radius for swatches | • None<br>• Default<br>• SM<br>• MD<br>• LG<br>• XL<br>• 2XL<br>• Full (default)<br><br>Visible when show swatch is true |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the options | Checkbox (default: false) |
| Enable top padding | Adds top padding around the options | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the options | Checkbox (default: false) |
| Gap size | Spacing between option elements | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Text color | Controls the text color | • Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade |
| Button color | Color scheme for option buttons | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link |
| Button color selected | Color scheme for selected option buttons | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline (default) |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for option labels | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when show labels is true |
| Font size | Controls the font size of option labels | • Smaller<br>• Small<br>• Default<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br><br>Visible when show labels is true |
| Button size | Controls the size of option buttons | • Extra small<br>• Small (default)<br>• Standard<br>• Large |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment | • Left (default)<br>• Center<br>• Right |
| Enable grid layout | Uses a grid layout instead of flex wrap | Checkbox (default: false) |
| Row desktop | Number of columns in grid on desktop | 1 - 12 (default: 4)<br><br>Visible when enable grid layout is true |
| Row mobile | Number of columns in grid on mobile | 1 - 3 (default: 2)<br><br>Visible when enable grid layout is true |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
