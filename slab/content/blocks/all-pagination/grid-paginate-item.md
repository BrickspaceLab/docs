# Paginate item

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within grid layout blocks that support pagination.

## Overview

A block that conditionally displays its content based on a pagination index. Works with grid components to show content for specific pagination states.

## Common use cases

* Set unique index values for each paginate content block
* Use with blocks/grid\_\_content for fully functional pagination
* Ensure gap sizes match between pagination components for visual consistency

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

| Setting            | Description                                | Options                                                                                                                           |
| ------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Index              | Pagination index this block corresponds to | Number (default: 6)                                                                                                               |
| Enable padding     | Adds padding around the content            | Checkbox (default: true)                                                                                                          |
| Gap size           | Spacing between child blocks               | None, Default (default), Xs, Sm, Md, Lg, Xl                                                                                       |
| Color scheme       | Controls the background color scheme       | Body (default), Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent |
| Border color       | Controls the border color                  | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None                                                                |
| Border position    | Controls which sides have borders          | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All                                                     |
| Vertical alignment | Controls vertical alignment of content     | Top, Middle, Bottom (default)                                                                                                     |
| Row span           | Number of rows this item spans             | 1 (default), 2, 3, 4, 5, 6                                                                                                        |
| Column span        | Number of columns this item spans          | 1 (default), 2, 3, 4, 5, 6                                                                                                        |
| Visibility         | Controls when the block is visible         | All (default), Mobile only, Desktop only                                                                                          |
