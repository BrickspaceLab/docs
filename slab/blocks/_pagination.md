# Pagination

A pagination component that provides infinite scroll, load more button, and numbered page navigation options. Designed for use within paginated layout blocks.


## Overview

Renders pagination controls for paginated content with three display modes: infinite scroll, load more on click, and next/back buttons. Supports sticky positioning, customizable button styles, and responsive visibility.


## Common use cases

Use this block to add pagination controls within paginated layout blocks such as collection grids, blog grids, or search grids.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within paginated layout blocks such as collection grid, blog grid, search grid, and collections grid. It requires a paginate object from a parent layout block and is not designed for standalone use. It is private because it depends on pagination context provided by its parent.


## Block settings

### Pagination type

| Setting | Description | Options |
| --- | --- | --- |
| Pagination type | Controls how additional pages are loaded | • Load more on scroll (default)<br>• Load more on click<br>• Next/back buttons |

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Label | Custom label text for the load more button | Text input |
| Show page count | Displays the current page and total page count | Checkbox (default: true) |

### Spacing

| Setting | Description | Options |
| --- | --- | --- |
| Top spacing | Padding space above the pagination | 0 – 300 px (default: 0) |
| Bottom spacing | Padding space below the pagination | 0 – 300 px (default: 0) |
| Enable padding | Adds padding around the pagination | Checkbox (default: true) |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Chooses between custom and base color modes | • Custom<br>• Base (default) |
| Scheme | Selects a custom color scheme for the background | Color scheme picker |
| Scheme | Sets the background color scheme | • Body<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent (default) |
| Border | Sets the border color style | • Body<br>• Subtle (default)<br>• Strong<br>• None |
| Button | Selects a custom color scheme for the button | Color scheme picker |
| Button | Sets the button color style | • Plain (default)<br>• Main<br>• Blur<br>• Outline<br>• Inverted outline<br>• Transparent<br>• Inverted transparent |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme | Checkbox (default: false) |

### Style

| Setting | Description | Options |
| --- | --- | --- |
| Border position | Sets the position of the border | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top & bottom<br>• Left & right<br>• All |
| Button size | Controls the size of pagination buttons | • Extra small<br>• Small (default)<br>• Standard<br>• Large |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Horizontal alignment | Controls horizontal alignment of the pagination | • Left<br>• Center (default)<br>• Right |
| Sticky position | Makes the pagination stick to the viewport edge | • None (default)<br>• Top<br>• Bottom |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
