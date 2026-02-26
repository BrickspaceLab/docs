# Product recommendations

A dynamic product recommendations slider that displays related or complementary products in a horizontally scrollable layout. Designed for use within the slider layout block.


## Overview

Renders product recommendations from the Shopify Product Recommendations API as horizontally scrollable slider items with responsive width controls. Supports related and complementary intent modes, tag filtering, and optionally hiding products already in the cart.


## Common use cases

Use this block to display product recommendations in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires a source product for generating recommendations and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and uses the Shopify Product Recommendations API loaded via Alpine.js.


## Block settings

| Setting | Description | Options |
| --- | --- | --- |
| Intent | Controls the type of product recommendations returned | • Related (default)<br>• Complementary |

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Product | Source product for generating recommendations | Product picker |
| Item count | Number of recommended products to display | Number input (default: 5) |
| Filter by tag | Filters recommendations to only show those with this tag | Text input |
| Show products in cart | When disabled, products that are added to the cart will not be shown | Checkbox (default: true) |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Mobile width | Width of each slider item on mobile | 5 – 100 % (default: 80) |
| Desktop width | Width of each slider item on desktop | 5 – 100 % (default: 20) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
