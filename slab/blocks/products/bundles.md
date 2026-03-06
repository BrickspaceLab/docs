# Product bundles

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Overview

A product bundle block that lists bundle items from a metafield and allows adding all selected variants to cart at once. Displays bundle products using the c\_\_bundle-item snippet and integrates with the theme's cart functionality to add multiple line items simultaneously.

## Common use cases

* Configure product bundles using the custom.product\_bundle metafield (list of products)
* Use gap size settings to control spacing between bundle items based on your design needs
* Configure button colors to match your theme's design system
* Set appropriate padding based on the container context where the bundle block is displayed
* Test bundle functionality with products that have variants to ensure proper selection flow

## Block settings

### Content

| Setting | Description                              | Options        |
| ------- | ---------------------------------------- | -------------- |
| Product | Select the product to display bundle for | Product picker |

### Spacing

| Setting                   | Description                               | Options                                                                      |
| ------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------- |
| Enable horizontal padding | Adds horizontal padding around the bundle | Checkbox (default: false)                                                    |
| Enable top padding        | Adds top padding around the bundle        | Checkbox (default: false)                                                    |
| Enable bottom padding     | Adds bottom padding around the bundle     | Checkbox (default: false)                                                    |
| Gap size                  | Controls spacing between bundle items     | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting               | Description                                           | Options                                                                                                                                                   |
| --------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disabled button color | Color scheme for the disabled "Choose Options" button | <p>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain (default)<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link</p> |
| Main button color     | Color scheme for the active "Add to Cart" button      | <p>• Primary (default)<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
