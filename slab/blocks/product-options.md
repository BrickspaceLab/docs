# Options


## Overview

A product variant selection block that provides flexible display options for product options including colors, sizes, and other variants. Supports both button and dropdown selection interfaces, with advanced features like swatches, tooltips, grid layout, and unavailability indicators.


## Common use cases

- Display product variant options with button or dropdown selection on product pages.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display options for | Product picker |
| Variant selection | Controls how non-swatch variants are displayed | &bull; Buttons (default)<br>&bull; Dropdowns |
| Unavailable indication | Controls how unavailable variants are indicated | &bull; None<br>&bull; Empty (default)<br>&bull; Selected |
| Show labels | Displays labels for each option | Checkbox (default: true) |
| Show single variant options | Displays options even when only one variant exists | Checkbox (default: true) |

### Swatches

| Setting | Description | Options |
|---------|-------------|---------|
| Swatch selection | Controls how swatch options are displayed | &bull; Buttons (default)<br>&bull; Dropdowns |
| Show swatch | Displays color swatches for color options | Checkbox (default: true) |
| Show tooltip | Displays tooltips showing option names on swatch hover | Checkbox (default: true)<br><br>_Visible when swatch selection is "Buttons"_ |
| Show labels | Displays text labels alongside swatches | Checkbox (default: false) |
| Layout | Controls the layout of swatch and label | &bull; Stacked<br>&bull; Inline (default)<br><br>_Visible when show swatch labels is enabled_ |
| Size | Size of the swatch indicators | Range: 8 - 120 px (default: 16)<br><br>_Visible when show swatch is enabled_ |
| Radius | Border radius for swatches | &bull; None<br>&bull; Default<br>&bull; SM<br>&bull; MD<br>&bull; LG<br>&bull; XL<br>&bull; 2XL<br>&bull; Full (default)<br><br>_Visible when show swatch is enabled_ |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the options | Checkbox (default: false) |
| Enable top padding | Adds top padding above the options | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the options | Checkbox (default: false) |
| Gap size | Spacing between option elements | &bull; None<br>&bull; Default (default)<br>&bull; XS<br>&bull; SM<br>&bull; MD<br>&bull; LG<br>&bull; XL |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Default button color | Color scheme for default option buttons | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Selected button color | Color scheme for selected option buttons | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Default button color | Color scheme for default option buttons | &bull; Plain (default)<br>&bull; Main<br>&bull; Blur<br>&bull; Outline<br>&bull; Inverted outline<br>&bull; Transparent<br>&bull; Inverted transparent<br><br>_Visible when type is "Base"_ |
| Selected button color | Color scheme for selected option buttons | &bull; Plain (default)<br>&bull; Main<br>&bull; Blur<br>&bull; Outline<br>&bull; Inverted outline<br>&bull; Transparent<br>&bull; Inverted transparent<br><br>_Visible when type is "Base"_ |
| Text color | Controls the text color for option labels | &bull; Default (default)<br>&bull; Alternative<br>&bull; Link<br>&bull; Error<br>&bull; Success<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br><br>_Visible when enable inheritance is disabled_ |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: true) |
| Enable selected outline | Adds an outline to the selected option button | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for option labels | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when show labels is enabled_ |
| Font size | Controls the font size of option labels | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6<br><br>_Visible when show labels is enabled_ |
| Button size | Controls the size of option buttons | &bull; Extra small<br>&bull; Small (default)<br>&bull; Standard<br>&bull; Large |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the options | &bull; Left (default)<br>&bull; Center<br>&bull; Right |
| Enable grid layout | Uses a grid layout instead of flex wrap | Checkbox (default: false) |
| Row desktop | Number of columns in grid on desktop | Range: 1 - 12 (default: 4)<br><br>_Visible when enable grid layout is enabled_ |
| Row mobile | Number of columns in grid on mobile | Range: 1 - 3 (default: 2)<br><br>_Visible when enable grid layout is enabled_ |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
