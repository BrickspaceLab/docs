# Blog grid

A paginated grid layout for displaying blog articles with configurable columns, spacing, and styling options. Designed for use within blog templates.


## Overview

Renders blog articles in a responsive grid with pagination support. Includes provisions for sidebar filters and top/bottom bar containers.


## Common use cases

Use this block to display paginated blog articles in a customizable grid layout on blog pages.


## Block limitations

This is a private block, indicated by the `_` prefix. It is intended for use exclusively within blog templates. It requires a blog context to paginate articles and must be placed inside a section that provides blog data. It is private because it depends on the blog template context and is not designed for standalone use.


## Compatible blocks

This block accepts the following nested block types:

- `_g__grid-paginateitem`


## Block settings

### Content

| Setting | Description | Options |
| --- | --- | --- |
| Items per page | Number of items displayed per page | 1 – 32 (default: 10) |

### Spacing

| Setting | Description | Options |
| --- | --- | --- |
| Top spacing | Padding space above the block content | 0 – 300 px (default: 0) |
| Bottom spacing | Padding space below the block content | 0 – 300 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding to the block | Checkbox (default: false) |
| Gap size | Controls the space between grid items | • None<br>• Default (default)<br>• Extra small<br>• Small<br>• Medium<br>• Large<br>• Extra large |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Chooses between custom and base color modes | • Custom<br>• Base (default) |
| Scheme | Selects a custom color scheme | Color scheme picker |
| Border | Sets the border color style | • Subtle (default)<br>• Strong<br>• Body foreground |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme | Checkbox (default: false) |

### Style

| Setting | Description | Options |
| --- | --- | --- |
| Border position | Sets the position of the border | • None (default)<br>• Top<br>• Bottom<br>• Top & bottom |

### Layout

| Setting | Description | Options |
| --- | --- | --- |
| Desktop row size | Number of columns displayed on desktop | 1 – 8 (default: 5) |
| Mobile row size | Number of columns displayed on mobile | 1 – 3 (default: 2) |
| Enable margin | Adds outer margin to the block | Checkbox (default: false) |

### Display

| Setting | Description | Options |
| --- | --- | --- |
| Visibility | Controls which devices the block appears on | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
