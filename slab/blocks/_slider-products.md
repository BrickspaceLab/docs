# Slider products

A product slider component for displaying collection products in a horizontally scrollable layout. Designed for use within the slider layout block.


## Overview

Renders products from a selected collection as horizontally scrollable slider items with responsive width controls. Supports filtering by tag and optionally hiding products already in the cart.


## Common use cases

Use this block to feature product collections in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires a collection selection and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and is not designed for standalone use.


## Block settings

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Collection | Collection to display products from | Collection picker |
| Item count | Number of products to display | Number input (default: 7) |
| Filter by tag | Filters products to only show those with this tag | Text input |
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
