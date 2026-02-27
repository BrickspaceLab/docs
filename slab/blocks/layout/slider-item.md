# Slider item

## Overview

A configurable slider item component designed to be used within the [Slider](slider.md) block. Provides customizable width settings for both mobile and desktop displays, with optional gap sizing between child elements.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

- Adjust width percentages based on desired number of visible items
- For equal width items across all slides, enable the default width setting
- Use the visibility options to create different experiences on mobile vs desktop
- Configure color schemes and borders to match your theme design

## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks

## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds padding around the slider item content | Checkbox (default: false) |
| Gap size | Controls spacing between child blocks | None, Default (default), XS, SM, MD, LG, XL |
| Color scheme | Controls the background and text colors | Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent (default) |
| Color border | Controls the border color | Body, Subtle, Strong, Primary, Secondary, Tertiary, None (default). Visible when border position is not blank |
| Border position | Controls where borders appear | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All |
| Width mobile | Width of the slider item on mobile devices | 5 - 100 % (default: 80). Visible when enable default width is false |
| Width desktop | Width of the slider item on desktop devices | 5 - 100 % (default: 40). Visible when enable default width is false |
| Enable default width | Uses automatic width sizing for equal-width items | Checkbox (default: false) |
| Vertical alignment | Controls vertical alignment of content | Top, Middle, Bottom (default) |
| Visibility | Controls when the block is visible | All (default), Mobile only, Desktop only |

