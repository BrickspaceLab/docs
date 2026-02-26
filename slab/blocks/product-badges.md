# Badges


## Overview

A product badges block that displays various informational badges such as sold out status, savings, low stock alerts, custom tag badges, and metafield badges. Supports text or styled badge display with configurable colors, positioning, and overlay mode.


## Common use cases

- Display sold out, savings, low stock, or custom promotional badges on product cards or product pages.


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display badges for | Product picker |
| Show sold out badge | Displays a badge when the product is sold out | Checkbox (default: false) |
| Savings badge | Type of savings badge to display | &bull; None<br>&bull; Percent (default)<br>&bull; Amount |
| Stock threshold | Minimum stock level to trigger low stock badge | Number input |
| Metafield badges | Comma-separated list of metafield namespace.key pairs | Text input |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the badges | Checkbox (default: false) |
| Enable top padding | Adds top padding above the badges | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the badges | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Determines color configuration mode | &bull; Custom<br>&bull; Base (default)<br><br>_Visible when enable inheritance is disabled_ |
| Color scheme | Controls the color scheme | Color scheme picker<br><br>_Visible when type is "Custom" and enable inheritance is disabled_ |
| Background | Controls the background color for badges | &bull; Body (default)<br>&bull; Accent 1<br>&bull; Accent 2<br>&bull; Accent 3<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br>&bull; Blur<br>&bull; Transparent<br><br>_Visible when display type is "Badge", type is "Base", and enable inheritance is disabled_ |
| Border color | Controls the border color for badges | &bull; None<br>&bull; Subtle (default)<br>&bull; Strong<br>&bull; Body foreground<br><br>_Visible when display type is "Badge", type is "Base", and enable inheritance is disabled_ |
| Text color | Controls the text color | &bull; Default (default)<br>&bull; Alternative<br>&bull; Link<br>&bull; Error<br>&bull; Success<br>&bull; Shade 1<br>&bull; Shade 2<br>&bull; Shade 3<br><br>_Visible when type is "Base" and enable inheritance is disabled_ |
| Enable inheritance | Inherits color settings from the parent block | Checkbox (default: true) |
| Enable color difference | Uses mix-blend-difference for better visibility on images | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Display type | How badges are displayed | &bull; Text<br>&bull; Badge (default) |
| Font family | Font family for badge text | &bull; Standard (default)<br>&bull; Heading<br>&bull; Subheading<br>&bull; Accent<br><br>_Visible when display type is "Text"_ |
| Font size | Font size for badge text | &bull; Smaller<br>&bull; Small<br>&bull; Default (default)<br>&bull; Big<br>&bull; Bigger<br>&bull; Heading 1<br>&bull; Heading 2<br>&bull; Heading 3<br>&bull; Heading 4<br>&bull; Heading 5<br>&bull; Heading 6<br><br>_Visible when display type is "Text"_ |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the badges | &bull; Left (default)<br>&bull; Center<br>&bull; Right |
| Vertical alignment | Controls vertical alignment when overlay is enabled | &bull; Top (default)<br>&bull; Bottom<br><br>_Visible when enable overlay is enabled_ |
| Enable overlay | Positions badges as an overlay on product images | Checkbox (default: false) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
