# Button


## Overview

A customizable button component that renders a link styled as a button with various appearance and layout options. Supports responsive visibility controls and multiple style variants.


## Common use cases

* Create call-to-action buttons throughout your theme
* Use custom actions to trigger overlays, form submissions, or JavaScript functions
* Configure button size and color to match your theme design system
* Trigger account, search, menu, or cart overlays with preset actions


## Compatible blocks

The following blocks can be nested within this block:

* [Rich text](richtext.md)
* [Icon](icon.md)
* [Image](image.md)
* [Localization label](localization-label.md)
* [Cart count](cart-count.md)
* [Simple subtotal](cart-price.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| URL | Link destination for the button | <p>URL input (default: /collections/all)<br><br>Visible when enable_custom_action is false</p> |
| Enable custom action | When enabled a button can be used to trigger overlays, form submissions or other actions. | Checkbox (default: false) |
| Overlay | Select a predefined overlay to open when this button is clicked. | <p>• None (default)<br>• Account overlay<br>• Search overlay<br>• Menu overlay<br>• Primary cart overlay<br>• Alternative cart overlay<br>• Custom<br><br>Visible when enable_custom_action is true and enable_close_overlays is false and enable_form_submission is false and enable_logout is false and enable_back_to_top is false</p> |
| Custom overlay | Enter the ID of the overlay to open when this button is clicked. | <p>Text input<br><br>Visible when enable_custom_action is true and overlay_preset is custom</p> |
| Enable close | When enabled this button will close all overlays. | <p>Checkbox (default: false)<br><br>Visible when enable_custom_action is true and enable_form_submission is false and enable_logout is false and enable_back_to_top is false and overlay_preset is none</p> |
| Enable form submission | When enabled any form this button is part of will submit when clicked. | <p>Checkbox (default: false)<br><br>Visible when enable_custom_action is true and enable_close_overlays is false and enable_logout is false and enable_back_to_top is false and overlay_preset is none</p> |
| Enable logout | When enabled a button can be used to logout the user. | <p>Checkbox (default: false)<br><br>Visible when enable_custom_action is true and enable_close_overlays is false and enable_form_submission is false and enable_back_to_top is false and overlay_preset is none</p> |
| Enable login | When enabled a button can be used to login the user. | <p>Checkbox (default: false)<br><br>Visible when enable_custom_action is true and enable_close_overlays is false and enable_form_submission is false and enable_back_to_top is false and overlay_preset is none</p> |
| Enable back to top | Scrolls page to top when clicked | <p>Checkbox (default: false)<br><br>Visible when enable_custom_action is true and enable_close_overlays is false and enable_form_submission is false and enable_logout is false and overlay_preset is none</p> |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable internal padding | Adds internal padding to the button content | Checkbox (default: true) |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)</p> |
| Button | Select a custom button color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom</p> |
| Button | Controls the button color scheme | <p>• Plain (default)<br>• Main<br>• Blur<br>• Outline<br>• Inverted outline<br>• Transparent<br>• Inverted transparent<br><br>Visible when color_type is base</p> |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Button size | Controls the button size | <p>• Extra small<br>• Small<br>• Standard (default)<br>• Large</p> |

### Layout

| Setting | Description | Options |
|---------|-------------|----------|
| Horizontal alignment | Controls horizontal alignment | <p>• Left (default)<br>• Center<br>• Right</p> |
| Enable full width | Makes the block span the full width of its container | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
