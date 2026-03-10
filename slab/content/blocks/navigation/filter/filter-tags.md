# Tag filter

## Overview

Displays a block of filter tags sourced from a collection or blog metafield, allowing buyers to filter collections or blog posts by custom tags. The block supports flexible layout (stacked or inline), alignment, spacing, color, font, and device visibility options. It renders a link to view all items and individual tag links, highlighting the active tag. Tag data is pulled from a metafield defined by the merchant in block settings.

## Common use cases

* Ensure the collection or blog metafield contains a comma-separated list of tags for best results
* Use the block in collection or blog templates to provide buyers with easy tag-based filtering
* Adjust gap size and alignment to match the design context and available space
* Use device visibility settings to tailor the block's presence on mobile or desktop as needed
* Combine with other navigation or filtering blocks for a comprehensive browsing experience

## Block settings

### Content

| Setting        | Description                                         | Options    |
| -------------- | --------------------------------------------------- | ---------- |
| Metafield tags | Metafield reference for tags (namespace.key format) | Text input |

### Spacing

| Setting                   | Description                             | Options                                                                      |
| ------------------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing               | Spacing above the tags                  | 0 - 30 px (default: 0)                                                       |
| Bottom spacing            | Spacing below the tags                  | 0 - 30 px (default: 0)                                                       |
| Enable horizontal padding | Adds horizontal padding around the tags | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between tags                    | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting    | Description                     | Options                                                                                                       |
| ---------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Text color | Controls the text color of tags | <p>• Default (default)<br>• Alternative<br>• Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Shade</p> |

### Style

| Setting     | Description                            | Options                                                                                                                                                           |
| ----------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for tags | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--'</p>                                                        |
| Font size   | Controls the font size of tags         | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Layout

| Setting              | Description                       | Options                                        |
| -------------------- | --------------------------------- | ---------------------------------------------- |
| Layout               | Controls the tag layout direction | <p>• Stacked<br>• Inline (default)</p>         |
| Horizontal alignment | Controls horizontal alignment     | <p>• Left (default)<br>• Center<br>• Right</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
