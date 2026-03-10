# Menu item

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Menu dropdown](./) or [Menu page](../menu-page.md) blocks.

## Overview

A menu item block component that renders content within a menu dropdown. Provides a container for theme and app blocks to be displayed when a menu item is selected.

## Common use cases

* Use this block to add custom content like featured products, images or promotions to menu dropdowns
* Configure gap size and padding based on content type and design needs
* Ensure menu\_key matches the parent menu item title for proper functionality

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

| Setting                   | Description                                       | Options                                                                                                                           |
| ------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Menu key                  | Key that matches the parent menu item (handlized) | Text input                                                                                                                        |
| Enable horizontal padding | Adds horizontal padding inside the container      | Checkbox (default: false)                                                                                                         |
| Enable vertical padding   | Adds vertical padding inside the container        | Checkbox (default: false)                                                                                                         |
| Gap size                  | Spacing between child blocks                      | None, Default (default), Xs, Sm, Md, Lg, Xl                                                                                       |
| Color scheme              | Controls the background color scheme              | Body (default), Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent |
| Border color              | Controls the border color                         | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when border position is not empty                     |
| Border position           | Controls which sides have borders                 | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All                                                     |
| Visibility                | Controls when the block is visible                | All (default), Mobile only, Desktop only                                                                                          |
