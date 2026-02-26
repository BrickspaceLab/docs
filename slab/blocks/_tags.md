# Tags

A block that lists and styles tags from the nearest article, product, or collection context. Supports text and badge display modes.


## Overview

Renders tags as plain text or styled badges with configurable alignment, typography, color, and overlay positioning. Automatically collects tags from the closest article, product, or collection context.


## Common use cases

Use this block to display tags inside article, product, or collection contexts where tags are present.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within article, product, or collection contexts that provide tags. It requires a closest context object to collect tags from and is not designed for standalone use. It is private because it depends on the closest article, product, or collection to source its content.


## Block settings

### Spacing

| Setting | Description | Options |
| --- | --- | --- |
| Enable horizontal padding | Adds horizontal padding around the tags | Checkbox (default: false) |
| Enable top padding | Adds top padding above the tags | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding below the tags | Checkbox (default: false) |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Chooses between custom and base color modes | • Custom<br>• Base (default) |
| Scheme | Selects a custom color scheme | Color scheme picker |
| Scheme | Sets the background and text color scheme for badges | • Body (default)<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent |
| Border | Sets the border color style for badges | • None<br>• Subtle (default)<br>• Strong<br>• Body foreground |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme | Checkbox (default: false) |
| Enable color difference | Colors are inverted when this block overlaps any other content | Checkbox (default: false) |

### Style

| Setting | Description | Options |
| --- | --- | --- |
| Display type | Controls how tags are rendered | • Text<br>• Badge (default) |
| Font family | Sets the font family for the tags | • Standard (default)<br>• Heading<br>• Subheading<br>• Accent |
| Font size | Sets the font size for the tags | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6 |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Horizontal alignment | Controls horizontal alignment of the tags | • Left (default)<br>• Center<br>• Right |
| Vertical alignment | Controls vertical position when overlay is enabled | • Top (default)<br>• Bottom |
| Enable overlay | Switches to absolute positioning over parent content | Checkbox (default: false) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
