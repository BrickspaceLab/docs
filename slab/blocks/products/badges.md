# Badges


## Overview

A customizable product badges block that displays various types of informational badges for products. The block can show sold out status, savings information, low stock alerts, custom product tags, and metafield-based badges. Badges can be displayed as plain text or styled badge elements with extensive customization options for positioning, colors, and layout.


## Common use cases

- Display sold out badges for unavailable products
- Show savings badges with percentage or amount saved
- Display low stock alerts when inventory is below threshold
- Use product tags prefixed with "badge_" to create custom badges
- Configure metafield badges for custom product attributes like "Featured", "New", or "Limited Edition"
- Use overlay positioning for product images to create eye-catching promotional badges
- Set appropriate stock thresholds based on your inventory management needs


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display badges for | Product picker |
| Show sold out badge | Displays a badge when the product is sold out | Checkbox (default: false) |
| Savings badge | Type of savings badge to display | • None<br>• Percent (default)<br>• Amount |
| Stock threshold | Minimum stock level to trigger low stock badge (0 = never show) | Number input |
| Metafield badges | Comma-separated list of metafield namespace.key pairs (e.g., "custom.badge,custom.featured") | Text input |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the badges | Checkbox (default: false) |
| Enable top padding | Adds top padding around the badges | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the badges | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background color scheme for badges | • Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent<br><br>Visible when display type is badge |
| Color border | Controls the border color for badges | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when display type is badge |
| Color text | Controls the text color | • Default (default)<br>• Alternative<br>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Shade |
| Enable color difference | Uses mix-blend-difference for better visibility on images | Checkbox (default: false) |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Display type | How badges are displayed | • Text<br>• Badge (default) |
| Font family | Font family for badge text | • Standard (default)<br>• Heading<br>• Subheading<br>• Accent |
| Font size | Font size for badge text | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the badges | • Left (default)<br>• Center<br>• Right |
| Vertical alignment | Controls vertical alignment when overlay is enabled | • Top (default)<br>• Bottom<br><br>Visible when enable overlay is true |
| Enable overlay | Positions badges as an overlay on product images | Checkbox (default: false) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
