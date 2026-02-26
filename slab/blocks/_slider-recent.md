# Recently viewed

A slider component that displays recently viewed products in a horizontally scrollable layout. Designed for use within the slider layout block.


## Overview

Renders recently viewed products as horizontally scrollable slider items with responsive width controls. Products are dynamically loaded from the browser using Alpine.js and the Shopify API.


## Common use cases

Use this block to display recently viewed products in a horizontal slider format within the slider layout block.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within the slider layout block. It requires browser-side recently viewed product data and must be nested inside a slider container. It is private because it depends on the slider layout for its scrollable behavior and Alpine.js store data for its content.


## Block settings

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Item count | Number of recently viewed products to display | Number input (default: 5) |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Mobile width | Width of each slider item on mobile | 5 – 100 % (default: 80) |
| Desktop width | Width of each slider item on desktop | 5 – 100 % (default: 20) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
