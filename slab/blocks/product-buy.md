# Buy buttons


## Overview

A product purchase form block that handles variant selection, quantity input, and cart actions. Displays different button states based on product availability and option selection, and supports dynamic checkout buttons and real-time price display.


## Common use cases

- Add a product purchase form with add-to-cart, quantity input, and dynamic checkout buttons to a product page.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display buy buttons for | Product picker |
| Dynamic label | Custom label for the add to cart button | Rich text input<br><br>_Visible when enable dynamic label is enabled_ |
| Enable dynamic label | Replaces "Add to cart" with custom label text | Checkbox (default: false) |
| Enable quantity input | Displays a quantity selector input field | Checkbox (default: false) |
| Enable dynamic checkout | Displays dynamic checkout buttons (Shop Pay, Apple Pay, etc.) | Checkbox (default: true) |
| Show price | Displays the product price on the add to cart button | Checkbox (default: true) |
| Show gift card form | Displays form fields for gift card recipient information | Checkbox (default: false) |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the form | Checkbox (default: false) |
| Enable top padding | Adds top padding above the form | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the form | Checkbox (default: false) |
| Gap size | Spacing between form elements | &bull; None<br>&bull; Default (default)<br>&bull; XS<br>&bull; SM<br>&bull; MD<br>&bull; LG<br>&bull; XL |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default) |
| Default button color | Color scheme for the add to cart button | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Default button color | Color scheme for the add to cart button | &bull; Plain (default)<br>&bull; Main<br>&bull; Blur<br>&bull; Outline<br>&bull; Inverted outline<br>&bull; Transparent<br>&bull; Inverted transparent<br><br>_Visible when type is "Base"_ |
| Disabled button color | Color scheme for disabled buttons | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Disabled button color | Color scheme for disabled buttons | &bull; Plain (default)<br>&bull; Main<br>&bull; Blur<br>&bull; Outline<br>&bull; Inverted outline<br>&bull; Transparent<br>&bull; Inverted transparent<br><br>_Visible when type is "Base"_ |
| Dynamic checkout button color | Color scheme for dynamic checkout buttons | Color scheme picker<br><br>_Visible when type is "Custom"_ |
| Dynamic checkout button color | Color scheme for dynamic checkout buttons | &bull; Plain (default)<br>&bull; Main<br>&bull; Blur<br>&bull; Outline<br>&bull; Inverted outline<br>&bull; Transparent<br>&bull; Inverted transparent<br><br>_Visible when type is "Base"_ |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Button size | Controls the size of buttons | &bull; Extra small<br>&bull; Small<br>&bull; Standard (default)<br>&bull; Large |
| Quantity input | Style of the quantity input field | &bull; Default (default)<br>&bull; Minimal<br><br>_Visible when enable quantity input is enabled_ |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Layout | Controls the layout of quantity and button | &bull; Stacked (default)<br>&bull; Inline |
| Enable full width | Makes buttons span the full width of the container | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
