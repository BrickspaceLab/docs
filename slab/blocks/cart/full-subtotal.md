# Full subtotal

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

## Overview

A Shopify theme block component that displays cart total pricing information including subtotal, discounts, and final total with reactive updates using Alpine.js.

## Common use cases

* Display comprehensive cart totals in cart drawers or cart pages
* Use appropriate spacing settings based on surrounding elements
* Consider adjusting font sizes for better hierarchy between subtotal and total
* Ensure all translation keys are properly defined in locale files

## Block settings

### Content

| Setting              | Description                          | Options                  |
| -------------------- | ------------------------------------ | ------------------------ |
| Show currency symbol | Displays currency symbol with prices | Checkbox (default: true) |

### Spacing

| Setting                   | Description                               | Options                   |
| ------------------------- | ----------------------------------------- | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the totals | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the totals        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the totals     | Checkbox (default: false) |

### Color

| Setting    | Description             | Options                                                                                                                                                                                                                                                      |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Text color | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade</p> |

### Style

| Setting     | Description              | Options                                                                                                                                                           |
| ----------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type--</p>                                                |
| Font size   | Controls the font size   | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
