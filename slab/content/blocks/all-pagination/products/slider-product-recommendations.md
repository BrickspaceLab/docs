# Slider recommendations

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Slider](../../layout/slider/) block.

## Overview

A dynamic product recommendations block that displays recommended products in a horizontal slider layout with scroll snap behavior. This block uses Alpine.js to asynchronously load product recommendations from Shopify's recommendation engine based on a source product. Products are displayed as horizontally scrollable cards with configurable widths and support for filtering by tags, cart status, and responsive visibility options.

## Common use cases

* Set a source product in block settings before adding to ensure relevant recommendations
* Adjust item count (default: 5) based on your slider layout and desired scroll behavior
* Configure width\_mobile (default: 80vw) and width\_desktop (default: 40vw) to control how many items are visible at once
* Use tag filtering when you want to show only products from specific collections or categories
* Enable "show products in cart" for cross-sell scenarios, disable for upsell to avoid redundancy
* The block works best when placed on product pages, cart pages, or thank you pages
* Best suited for contexts where horizontal scrolling is preferred over a static grid layout

## Block settings

### Content

| Setting               | Description                                           | Options                                       |
| --------------------- | ----------------------------------------------------- | --------------------------------------------- |
| Intent                | Recommendation type                                   | <p>• Related (default)<br>• Complementary</p> |
| Product               | Source product for recommendations                    | Product picker                                |
| Item count            | Number of recommendations to display                  | Number (default: 5)                           |
| Filter by tag         | Filter recommendations by a specific tag              | Text input                                    |
| Show products in cart | Displays products even if they're already in the cart | Checkbox (default: true)                      |

### Spacing

| Setting       | Description                          | Options                 |
| ------------- | ------------------------------------ | ----------------------- |
| Width mobile  | Width of each slider item on mobile  | 5 - 100 % (default: 80) |
| Width desktop | Width of each slider item on desktop | 5 - 100 % (default: 20) |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
