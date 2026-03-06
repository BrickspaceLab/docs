# Product quick buy

<figure><img src="../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Overview

A quick buy button block for product pages that allows customers to add a product to their cart or open a quick buy modal without navigating to the product detail page. Automatically handles single-variant products by adding them directly to the cart, and multi-variant products by opening a quick buy modal for variant selection.

## Common use cases

* Use on collection pages or featured product sections for streamlined shopping
* Enable dynamic label for custom button text based on product state (e.g., "Pre-order")
* Configure button size and color to match your theme's design system
* Use full width option for prominent call-to-action buttons
* Consider alignment settings based on surrounding content layout

## Block settings

### Content

| Setting              | Description                                                | Options                                                                 |
| -------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------- |
| Product              | Select the product to display quick buy button for         | Product picker                                                          |
| Dynamic label        | Custom button text when dynamic label is enabled           | <p>Rich text input<br><br>Visible when enable dynamic label is true</p> |
| Enable dynamic label | Allows custom button text instead of default "Add to Cart" | Checkbox (default: false)                                               |

### Spacing

| Setting                   | Description                               | Options                   |
| ------------------------- | ----------------------------------------- | ------------------------- |
| Enable internal padding   | Adds internal padding to the button       | Checkbox (default: true)  |
| Enable horizontal padding | Adds horizontal padding around the button | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the button        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the button     | Checkbox (default: false) |

### Color

| Setting      | Description                      | Options                                                                                                                                                   |
| ------------ | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Button color | Controls the button color scheme | <p>• Primary<br>• Secondary (default)<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link</p> |

### Style

| Setting     | Description              | Options                                                            |
| ----------- | ------------------------ | ------------------------------------------------------------------ |
| Button size | Controls the button size | <p>• Extra small<br>• Small (default)<br>• Standard<br>• Large</p> |

### Layout

| Setting              | Description                                           | Options                                                                                       |
| -------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment of the button           | <p>• Left (default)<br>• Center<br>• Right<br><br>Visible when enable full width is false</p> |
| Enable full width    | Makes the button span the full width of its container | Checkbox (default: false)                                                                     |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
