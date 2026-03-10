# Pagination

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within paginated layout blocks.

## Overview

A pagination component that provides options for infinite scroll, load more button, and numbered page navigation within paginated content.

## Common use cases

* Use within paginated collections or search results
* Choose pagination type based on user experience needs

## Block settings

| Setting              | Description                            | Options                                                                                                                           |
| -------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Pagination type      | Type of pagination to display          | Scroll (default), Load, Pages                                                                                                     |
| Label                | Custom label for load more button      | Text input                                                                                                                        |
| Show page count      | Displays current page and total pages  | Checkbox (default: true)                                                                                                          |
| Top spacing          | Spacing above the pagination           | 0 - 300 px (default: 0)                                                                                                           |
| Bottom spacing       | Spacing below the pagination           | 0 - 300 px (default: 0)                                                                                                           |
| Enable padding       | Adds padding around the pagination     | Checkbox (default: true)                                                                                                          |
| Color scheme         | Controls the background color scheme   | Body, Neutral, Accent 1, Accent 2, Accent 3, Shade 1, Shade 2, Shade 3, Primary, Secondary, Tertiary, Blur, Transparent (default) |
| Border color         | Controls the border color              | Body, Subtle (default), Strong, Primary, Secondary, Tertiary, None. Visible when border position is not empty                     |
| Button color         | Color style for pagination buttons     | Primary, Secondary (default), Tertiary, Neutral, Plain, Outline, Inverted outline, Blur, Link, Inverted link                      |
| Border position      | Controls which sides have borders      | None (default), Top, Bottom, Left, Right, Top and bottom, Left and right, All                                                     |
| Button size          | Size of pagination buttons             | Extra small, Small (default), Standard, Large                                                                                     |
| Horizontal alignment | Controls horizontal alignment          | Left, Center (default), Right                                                                                                     |
| Sticky position      | Makes the pagination stick to viewport | None (default), Top, Bottom                                                                                                       |
| Visibility           | Controls when the block is visible     | All (default), Mobile only, Desktop only                                                                                          |
