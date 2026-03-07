# Flex item

## Overview

A flexible container item designed to be used within layout__flex.liquid for creating customizable layouts. Supports responsive width adjustments, alignment controls, and spacing options.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

- Use with layout__flex.liquid to create flexible grid-like layouts
- Configure visibility settings for responsive designs that differ between mobile and desktop
- Adjust gap size to maintain consistent spacing between nested elements
- Set custom widths for mobile and desktop views
- Use sticky positioning for elements that should remain visible while scrolling

## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks

## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Enable padding | Adds padding around the flex item content | Checkbox (default: false) |
| Enable vertical spacing | Adds vertical padding (top and bottom) | Checkbox (default: true) |
| Gap size | Controls spacing between child blocks | None, Default (default), XS, SM, MD, LG, XL |
| Color scheme | Controls the background and text colors | Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent (default) |
| Color border | Controls the border color | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when border position is not blank |
| Border position | Controls where borders appear | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All |
| Width mobile | Width of the flex item on mobile devices | 5 - 100 % (default: 80). Visible when enable width fill and enable default width are false |
| Width desktop | Width of the flex item on desktop devices | 5 - 100 % (default: 40). Visible when enable width fill and enable default width are false |
| Enable width fill | Makes the flex item grow to fill available space | Checkbox (default: false) |
| Enable default width | Uses automatic width sizing | Checkbox (default: false) |
| Enable sticky layout | Enables sticky positioning | Checkbox (default: false) |
| Sticky position | Position for sticky element | None, Top, Bottom. Visible when enable sticky layout is true |
| Vertical alignment | Controls vertical alignment of content | Top, Middle, Bottom (default) |
| Visibility | Controls when the block is visible | All (default), Mobile only, Desktop only |

