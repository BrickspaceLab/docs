# Tags

## Overview

A block that lists and styles tags for the nearest context (article, product, or collection). It collects tags from closest.article, closest.product, or closest.collection, then renders each as plain text or as a styled badge depending on the display_type setting.

## Block limitations

This is a private block that can only be used within specific sections or parent blocks. It automatically detects tags from the nearest article, product, or collection context and is not intended for standalone use.

## Common use cases

- Place inside article, product, or collection contexts where tags are present
- Prefer badge display type for emphasis; use text for subtle inline labels
- Tune alignment, font family, and font size to match surrounding typography
- Use padding settings sparingly to keep spacing consistent with adjacent blocks
- Enable overlay for absolute positioning when tags should appear over other content

## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the tags | Checkbox (default: false) |
| Enable top padding | Adds top padding around the tags | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the tags | Checkbox (default: false) |
| Color scheme | Controls the background and text colors for badges | Body (default), Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent. Visible when display type is badge |
| Color border | Controls the border color for badges | Body (default), Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when display type is badge |
| Enable color difference | Applies mix-blend-difference for better visibility on varying backgrounds | Checkbox (default: false) |
| Display type | Controls how tags are displayed | Text, Badge (default) |
| Font family | Controls the font family | Standard (default), Heading, Subheading, Accent |
| Font size | Controls the font size | Smaller, Small, Default (default), Big, Bigger, Heading 1, Heading 2, Heading 3, Heading 4, Heading 5, Heading 6. Visible when display type is text |
| Horizontal alignment | Controls horizontal alignment | Left (default), Center, Right |
| Vertical alignment | Controls vertical alignment when overlay is enabled | Top (default), Bottom. Visible when enable overlay is true |
| Enable overlay | Switches to absolute positioning | Checkbox (default: false) |
| Visibility | Controls when the block is visible | All (default), Mobile only, Desktop only |

