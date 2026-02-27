# Sibling options


## Overview

A product navigation block that displays sibling products (related products from a linked collection) as either interactive buttons/swatches or in a dropdown/drawer interface. Allows customers to navigate between related product variants with visual previews using the product's featured image. Supports flexible display modes with customizable swatches, tooltips, and responsive layouts.


## Common use cases

- Configure the custom.linked_collection metafield for your products to enable sibling product navigation
- Use button/swatch mode when displaying a small number of siblings (2-6 products) for quick visual selection
- Use dropdown mode when displaying many siblings (7+ products) to save space and reduce visual clutter
- Enable tooltips when showing swatches without labels to improve accessibility
- Consider enabling grid layout for consistent spacing and alignment
- Adjust swatch size (8-120px) based on design context: smaller for compact layouts, larger for hero sections
- Set appropriate gap sizes to balance density and readability


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display sibling options for | Product picker |
| Label | Optional label text displayed above the sibling options | Text input |
| Swatch selection | Controls how sibling options are displayed | • Buttons (default)<br>• Dropdowns |
| Show swatch | Displays product featured image as swatch background | Checkbox (default: true) |
| Show tooltip | Displays tooltip on hover showing product title | Checkbox (default: true)<br><br>Visible when swatch selection is buttons |
| Show labels | Displays product title alongside swatches | Checkbox (default: false)<br><br>Visible when swatch selection is buttons |
| Layout | Controls how swatches and labels are arranged | • Stacked<br>• Inline (default)<br><br>Visible when show labels and swatch selection is buttons |
| Swatch size | Size of the swatch preview images | 8 - 120 px (default: 16)<br><br>Visible when show swatch is true |
| Swatch radius | Controls the border radius of swatches | • None<br>• Default<br>• SM<br>• MD<br>• LG<br>• XL<br>• 2XL<br>• Full (default)<br><br>Visible when show swatch is true |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the block | Checkbox (default: false) |
| Enable top padding | Adds top padding around the block | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the block | Checkbox (default: false) |
| Gap size | Controls spacing between sibling option buttons | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Text color | Controls the text color for labels | • Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade<br><br>Visible when label is not blank |
| Button color | Controls the button/swatch color scheme | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family for labels | • Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type-- and label is not blank |
| Font size | Controls the font size for labels | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br><br>Visible when label is not blank |
| Button size | Controls the size of buttons/swatches | • Extra small<br>• Small (default)<br>• Standard<br>• Large |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment | • Left (default)<br>• Center<br>• Right<br><br>Visible when label is not blank |
| Enable grid layout | Displays options in a grid instead of flex wrap | Checkbox (default: false)<br><br>Visible when swatch selection is buttons |
| Row desktop | Number of columns in grid on desktop | 1 - 12 (default: 4)<br><br>Visible when enable grid layout and swatch selection is buttons |
| Row mobile | Number of columns in grid on mobile | 1 - 3 (default: 2)<br><br>Visible when enable grid layout and swatch selection is buttons |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
