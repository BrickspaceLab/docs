# Buy buttons


## Overview

A comprehensive product purchase form block that handles variant selection, quantity input, and cart actions. The block dynamically displays different button states based on product availability and option selection, including "Choose Options", "Sold Out", "Unavailable", and "Add to Cart" states. Supports optional quantity input, dynamic checkout buttons, and real-time price display.


## Common use cases

- Ensure all product options are configured before adding this block
- Use inline layout only when horizontal space is sufficient for both quantity and button
- Enable quantity input for products that customers typically buy in bulk
- Configure appropriate button colors to match your theme's design system
- Test with products that have multiple variants to ensure proper option selection flow
- Consider enabling dynamic checkout for improved conversion rates


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display buy buttons for | Product picker |
| Dynamic label | Custom label for the add to cart button (e.g., "Pre-order") | Rich text input<br><br>Visible when enable dynamic label is true |
| Enable dynamic label | Replaces "Add to cart" with custom label text | Checkbox (default: false) |
| Enable quantity input | Displays a quantity selector input field | Checkbox (default: false) |
| Enable dynamic checkout | Displays dynamic checkout buttons (Shop Pay, Apple Pay, etc.) | Checkbox (default: true) |
| Show price | Displays the product price on the add to cart button | Checkbox (default: true) |
| Show gift card form | Displays form fields for gift card recipient information | Checkbox (default: false) |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the form | Checkbox (default: false) |
| Enable top padding | Adds top padding around the form | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the form | Checkbox (default: false) |
| Gap size | Spacing between form elements | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Main button color | Color scheme for the add to cart button | • Primary (default)<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link |
| Disabled button color | Color scheme for disabled/placeholder buttons | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link |
| Dynamic checkout button color | Color scheme for dynamic checkout buttons | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default) |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Button size | Controls the size of buttons | • Extra small<br>• Small<br>• Standard (default)<br>• Large |
| Quantity input | Style of the quantity input field | • Default (default)<br>• Minimal<br><br>Visible when enable quantity input is true |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Layout | Controls the layout of quantity and button | • Stacked (default)<br>• Inline |
| Enable full width | Makes buttons span the full width of the container | Checkbox (default: false) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
