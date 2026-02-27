# Product grid


## Overview

A product grid block that displays products from a selected collection. Supports filtering by tag and customizable display settings including item count and device visibility.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use this block when you want to display a specific collection's products in a grid layout
- Set an appropriate item_count to control the number of products shown
- Use the tag filter to display a subset of products that match a specific tag
- Optionally hide products that are already in the customer's cart


## Compatible blocks

The following blocks can be nested within this block:

- [Product card](../cards/product-card.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Collection | Select the collection to display products from | Collection picker |
| Item count | Maximum number of products to display | Number input (default: 7) |
| Filter by tag | Filter products by a specific tag | Text input |
| Show products in cart | Shows products even if they're already in the cart | Checkbox (default: true) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
