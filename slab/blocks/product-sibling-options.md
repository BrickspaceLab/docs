# Sibling options


## Overview

A product navigation block that displays sibling products (related products from a linked collection) as either interactive buttons/swatches or in a dropdown/drawer interface. Allows customers to navigate between related product variants with visual previews using the product's featured image. Supports flexible display modes with customizable swatches, tooltips, and responsive layouts.


## Common use cases

* Configure the custom.linked_collection metafield for your products to enable sibling product navigation
* Use button/swatch mode when displaying a small number of siblings for quick visual selection
* Use dropdown mode when displaying many siblings to save space and reduce visual clutter
* Enable tooltips when showing swatches without labels to improve accessibility
* Consider enabling grid layout for consistent spacing and alignment


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Controls the product | Product picker |
| Label | Controls the label | Text input |

### Swatches

| Setting | Description | Options |
|---------|-------------|---------|
| Swatch selection | Controls the swatch selection | • Buttons (default)<br>• Dropdowns |
| Show swatch | Controls the show swatch | Checkbox (default: true) |
| Show tooltip | Controls the show tooltip | <p>Checkbox (default: true)<br><br>Visible when swatch selection is buttons</p> |
| Show labels | Controls the show labels | <p>Checkbox (default: false)<br><br>Visible when swatch selection is buttons</p> |
| Layout | Controls the layout | <p>• Stacked<br>• Inline (default)<br><br>Visible when show swatch is true and swatch selection is buttons</p> |
| Size | Controls the size | <p>8 – 120 px (default: 16)<br><br>Visible when show swatch is true</p> |
| Radius | Controls the radius | <p>• None<br>• Default<br>• Small<br>• Medium<br>• Large<br>• Extra large<br>• 2x Large<br>• Full (default)<br><br>Visible when show swatch is true</p> |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Controls the enable horizontal padding | Checkbox (default: false) |
| Enable top padding | Controls the enable top padding | Checkbox (default: false) |
| Enable bottom padding | Controls the enable bottom padding | Checkbox (default: false) |
| Gap size | Controls the gap size | • None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Controls the type | • Custom<br>• Base (default) |
| Text color | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3<br><br>Visible when label is not blank and enable inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: true) |
| Button | Controls the button | <p>Color scheme picker<br><br>Visible when color type is custom</p> |
| Button | Controls the button | <p>• Plain (default)<br>• Main<br>• Blur<br>• Outline<br>• Inverted outline<br>• Transparent<br>• Inverted transparent<br><br>Visible when color type is base</p> |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type-- and label is not blank</p> |
| Font size | Controls the font size | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br><br>Visible when label is not blank</p> |
| Button size | Controls the button size | • Extra small<br>• Small (default)<br>• Standard<br>• Large |

### Layout

This section is visible when swatch selection is buttons.

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls the horizontal alignment | <p>• Left (default)<br>• Center<br>• Right<br><br>Visible when label is not blank</p> |
| Enable grid layout | Controls the enable grid layout | <p>Checkbox (default: false)<br><br>Visible when swatch selection is buttons</p> |
| Row desktop | Controls the row desktop | <p>1 – 12 (default: 4)<br><br>Visible when enable grid layout is true and swatch selection is buttons</p> |
| Row mobile | Controls the row mobile | <p>1 – 3 (default: 2)<br><br>Visible when enable grid layout is true and swatch selection is buttons</p> |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls the visibility | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
