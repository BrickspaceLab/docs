# Inventory availability


## Overview

A product inventory block that displays stock level information and provides visual feedback when inventory falls below a configurable threshold. Designed to alert customers when stock is low, using customizable appearance settings.


## Common use cases

- Display low stock alerts on product pages to encourage customers to purchase before stock runs out.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display inventory for | Product picker |
| Inventory threshold | Minimum stock level before showing inventory alert | Number input (default: 5) |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the inventory display | Checkbox (default: false) |
| Enable top padding | Adds top padding above the inventory display | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the inventory display | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default)<br><br>_Visible when enable inheritance is disabled_ |
| Text color | Controls the text color | Color scheme picker<br><br>_Visible when type is "Custom" and enable inheritance is disabled_ |
| Text color | Controls the text color | &bull; Default (default)<br>&bull; Alternative<br>&bull; Link<br>&bull; Error<br>&bull; Success<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br><br>_Visible when type is "Base" and enable inheritance is disabled_ |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: true) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family used for the inventory text | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when font size contains "type--"_ |
| Font size | Controls the font size of the inventory text | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6 |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the inventory text | &bull; Left (default)<br>&bull; Center<br>&bull; Right |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
