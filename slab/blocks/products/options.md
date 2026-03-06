# Product options

<figure><img src="../../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Overview

A comprehensive product variant selection block that provides flexible display options for product options including colors, sizes, and other variants. The block supports both button-based and dropdown-based selection interfaces, with advanced features like swatches, tooltips, and unavailability indicators. It integrates with Alpine.js for interactive behavior and handles complex variant logic including availability checking and option state management.

## Common use cases

* Use button selection for better user experience when you have few variant options
* Enable swatches for color options to provide visual selection feedback
* Consider using unavailable indication to guide customers toward available variants
* Use grid layout when displaying many options to maintain organized appearance
* Configure appropriate gap sizes based on your design system and available space
* Enable tooltips for swatch-only displays to show option names on hover
* Test responsive behavior to ensure smooth transitions between desktop dropdowns and mobile drawers
* Ensure proper styling of disabled states when using unavailability indicators

## Block settings

### Content

| Setting                | Description                                     | Options                                          |
| ---------------------- | ----------------------------------------------- | ------------------------------------------------ |
| Product                | Select the product to display options for       | Product picker                                   |
| Variant selection      | Controls how non-swatch variants are displayed  | <p>• Buttons (default)<br>• Dropdowns</p>        |
| Unavailable indication | Controls how unavailable variants are indicated | <p>• None<br>• Empty (default)<br>• Selected</p> |
| Show labels            | Displays labels for each option                 | Checkbox (default: true)                         |

### Swatches

| Setting          | Description                                            | Options                                                                                                                         |
| ---------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Swatch selection | Controls how swatch options (colors) are displayed     | <p>• Buttons (default)<br>• Dropdowns</p>                                                                                       |
| Show swatch      | Displays color swatches for color options              | Checkbox (default: true)                                                                                                        |
| Show tooltip     | Displays tooltips showing option names on swatch hover | <p>Checkbox (default: true)<br><br>Visible when swatch selection is "buttons"</p>                                               |
| Show labels      | Displays text labels with swatches                     | Checkbox (default: false)                                                                                                       |
| Layout           | Controls the layout of swatch and label                | <p>• Stacked<br>• Inline (default)<br><br>Visible when show labels is true</p>                                                  |
| Size             | Size of the swatch indicators                          | <p>8 - 120 px (default: 16)<br><br>Visible when show swatch is true</p>                                                         |
| Radius           | Border radius for swatches                             | <p>• None<br>• Default<br>• SM<br>• MD<br>• LG<br>• XL<br>• 2XL<br>• Full (default)<br><br>Visible when show swatch is true</p> |

### Spacing

| Setting                   | Description                                | Options                                                                      |
| ------------------------- | ------------------------------------------ | ---------------------------------------------------------------------------- |
| Enable horizontal padding | Adds horizontal padding around the options | Checkbox (default: false)                                                    |
| Enable top padding        | Adds top padding around the options        | Checkbox (default: false)                                                    |
| Enable bottom padding     | Adds bottom padding around the options     | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between option elements            | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting               | Description                              | Options                                                                                                                                                                                                                                                      |
| --------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Text color            | Controls the text color                  | <p>• Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade</p> |
| Button color          | Color scheme for option buttons          | <p>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link</p>                                                                                                    |
| Button color selected | Color scheme for selected option buttons | <p>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline (default)</p>                                                                                                                                                                 |

### Style

| Setting     | Description                                     | Options                                                                                                                                                                                         |
| ----------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for option labels | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when show labels is true</p>                                                                                              |
| Font size   | Controls the font size of option labels         | <p>• Smaller<br>• Small<br>• Default<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br><br>Visible when show labels is true</p> |
| Button size | Controls the size of option buttons             | <p>• Extra small<br>• Small (default)<br>• Standard<br>• Large</p>                                                                                                                              |

### Layout

| Setting              | Description                             | Options                                                                   |
| -------------------- | --------------------------------------- | ------------------------------------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment           | <p>• Left (default)<br>• Center<br>• Right</p>                            |
| Enable grid layout   | Uses a grid layout instead of flex wrap | Checkbox (default: false)                                                 |
| Row desktop          | Number of columns in grid on desktop    | <p>1 - 12 (default: 4)<br><br>Visible when enable grid layout is true</p> |
| Row mobile           | Number of columns in grid on mobile     | <p>1 - 3 (default: 2)<br><br>Visible when enable grid layout is true</p>  |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
