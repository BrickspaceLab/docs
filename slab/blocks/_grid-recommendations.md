# Product recommendations


## Overview

A product recommendations block that displays recommended products from Shopify's recommendation engine in a grid layout. It supports related and complementary intents, tag filtering, configurable item count, and responsive device visibility.


## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.


## Common use cases

- Use to display product recommendations in a grid, with support for related or complementary product suggestions.


## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Intent | Type of product recommendations to display | &bull; Related (default)<br>&bull; Complementary |

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Product | Select the source product for generating recommendations | Product picker |
| Item count | Maximum number of recommendations to display | Number input (default: 5) |
| Filter by tag | Filter recommendations by a specific tag | Text input |
| Show products in cart | Shows recommended products even if they are already in the cart | Checkbox (default: true) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | &bull; All (default)<br>&bull; Mobile only<br>&bull; Desktop only |
