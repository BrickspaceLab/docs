# Grid recommendations

## Overview

A dynamic product recommendations block that displays recommended products in a grid layout. This block uses Alpine.js to asynchronously load product recommendations from Shopify's recommendation engine based on a source product.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Set a source product in block settings before adding to ensure relevant recommendations
* Adjust item count (default: 5) based on your grid layout and available space
* Use tag filtering when you want to show only products from specific collections or categories
* Enable "show products in cart" for cross-sell scenarios, disable for upsell to avoid redundancy
* Configure the nested product card blocks to match your theme's design system
* Consider using responsive visibility options to show different recommendation counts on mobile vs desktop
* The block works best when placed on product pages, cart pages, or thank you pages

## Compatible blocks

The following blocks can be nested within this block:

* [Product card](../../cards/product-card.md)

## Block settings

### Content

| Setting               | Description                                                    | Options                                       |
| --------------------- | -------------------------------------------------------------- | --------------------------------------------- |
| Intent                | Type of product recommendations                                | <p>• Related (default)<br>• Complementary</p> |
| Product               | Source product for generating recommendations                  | Product picker                                |
| Item count            | Maximum number of recommendations to display                   | Number input (default: 5)                     |
| Filter by tag         | Filter recommendations by a specific tag                       | Text input                                    |
| Show products in cart | Shows recommended products even if they're already in the cart | Checkbox (default: true)                      |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
