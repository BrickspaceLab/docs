# Tab item

## Overview

A configurable tab item block for creating tabbed content sections in Shopify themes. This block is designed to work with tab navigation systems and displays content only when its corresponding tab is selected.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Use consistent tab names across related tab items
* Consider responsive visibility settings for different content on mobile/desktop
* Adjust spacing and gap size to maintain visual consistency with your theme
* Configure color schemes to match your theme design

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

| Setting                   | Description                                                                    | Options                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Tab key                   | Unique identifier for this tab item (must match tab name in parent tabs block) | Text input                                                                                                                        |
| Enable horizontal padding | Adds horizontal padding to the tab content                                     | Checkbox (default: false)                                                                                                         |
| Enable vertical padding   | Adds vertical padding to the tab content                                       | Checkbox (default: true)                                                                                                          |
| Gap size                  | Controls spacing between child blocks                                          | None, Default (default), XS, SM, MD, LG, XL                                                                                       |
| Color scheme              | Controls the background and text colors                                        | Body (default), Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent |
| Vertical alignment        | Controls vertical alignment of content                                         | Top, Middle, Bottom                                                                                                               |
| Visibility                | Controls when the block is visible                                             | All (default), Mobile only, Desktop only                                                                                          |
