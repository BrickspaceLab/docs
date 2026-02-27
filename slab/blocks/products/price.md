# Price


## Overview

A comprehensive product price display block that renders pricing information for products including regular prices, sale prices, price ranges, and unit pricing. Automatically handles product variants by using selected_or_first_available_variant and displays sale pricing with strikethrough compare-at prices when available. Unit pricing appears below main price when available on the selected variant.


## Common use cases

- Display product pricing on product pages and product cards
- Show price ranges for products with multiple variants
- Display sale prices with strikethrough compare-at prices
- Show unit pricing for products sold by weight or volume
- Configure appropriate font sizes based on context (smaller for cards, larger for product pages)
- Use alignment settings that match your overall product layout design


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the product to display pricing for | Product picker |
| Price range | How to display prices for products with multiple variants | • Range (default)<br>• Starting price |
| Sale price range | How to display sale prices for products with multiple variants | • Range (default)<br>• Starting price |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the price | Checkbox (default: false) |
| Enable top padding | Adds top padding around the price | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the price | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color text | Controls the text color | • Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Font family for the price text | • Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type-- |
| Font size | Font size for the price text | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls horizontal alignment of the price | • Left (default)<br>• Center<br>• Right |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
