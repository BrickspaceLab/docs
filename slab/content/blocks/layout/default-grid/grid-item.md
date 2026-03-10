# Grid item

## Overview

A block that conditionally displays its content based on a pagination index. Works with grid components to show content for specific pagination states.

## Block limitations

This is a private block. It is intended for use only within specific parent blocks and should not be added directly to sections.

## Common use cases

* Set unique index values for each paginate content block
* Use with blocks/grid\_\_content for fully functional pagination
* Ensure gap sizes match between pagination components for visual consistency
* Configure column and row spans to create complex grid layouts
* Use color schemes and borders to visually distinguish grid items

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

| Setting            | Description                                      | Options                                                                                                                           |
| ------------------ | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Enable padding     | Adds padding around the grid item content        | Checkbox (default: true)                                                                                                          |
| Gap size           | Controls spacing between child blocks            | None, Default (default), XS, SM, MD, LG, XL                                                                                       |
| Color scheme       | Controls the background and text colors          | Body, Neutral, Accent 1 (default), Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent |
| Color border       | Controls the border color                        | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when border position is not blank                     |
| Border position    | Controls where borders appear                    | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All                                                     |
| Vertical alignment | Controls vertical alignment of content           | Top (default), Middle, Bottom                                                                                                     |
| Row span           | Number of rows the grid item spans               | 1 (default), 2, 3, 4, 5, 6                                                                                                        |
| Column span        | Number of columns the grid item spans on desktop | 1, 2 (default), 3, 4, 5, 6                                                                                                        |
| Visibility         | Controls when the block is visible               | All (default), Mobile only, Desktop only                                                                                          |
