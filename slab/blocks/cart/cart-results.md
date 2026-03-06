# Cart results

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

## Overview

Displays cart items in a customizable container with configurable padding and responsive visibility options. Uses Alpine.js to iterate through grouped cart items and renders the template\_\_cart-item snippet for each item group.

## Common use cases

* Display cart items in cart drawers or cart pages
* Ensure template\_\_cart-item snippet exists and is properly configured
* Consider visibility settings when using multiple cart item blocks for responsive layouts
* Configure padding to match your theme's spacing system

## Block settings

### Spacing

| Setting                   | Description                                   | Options                   |
| ------------------------- | --------------------------------------------- | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the cart items | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the cart items        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the cart items     | Checkbox (default: false) |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
