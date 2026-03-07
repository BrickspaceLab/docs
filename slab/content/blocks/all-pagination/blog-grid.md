# Layout blog

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within blog templates.

## Overview

A block for displaying paginated blog articles in a customizable grid layout with configurable columns, spacing, and styling. This block supports blog templates and contains provisions for sidebar and top bar filters.

## Common use cases

* Adjust items\_per\_page based on your store's needs
* Set appropriate row\_desktop and row\_mobile values for responsive design

## Compatible blocks

The following blocks can be nested within this block:

* Grid paginate item blocks
* [Container](../basics/containers/container.md) blocks (for top bar, sidebars, bottom bar)
* [Pagination](../navigation/pagination.md)

## Block settings

### Content

| Setting        | Description                 | Options              |
| -------------- | --------------------------- | -------------------- |
| Items per page | Number of articles per page | 1 - 32 (default: 10) |

### Spacing

| Setting                   | Description                             | Options                                                                      |
| ------------------------- | --------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing               | Spacing above the grid                  | 0 - 300 px (default: 0)                                                      |
| Bottom spacing            | Spacing below the grid                  | 0 - 300 px (default: 0)                                                      |
| Enable horizontal padding | Adds horizontal padding around the grid | Checkbox (default: false)                                                    |
| Gap size                  | Spacing between grid items              | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting      | Description               | Options                               |
| ------------ | ------------------------- | ------------------------------------- |
| Border color | Controls the border color | <p>• Subtle (default)<br>• Strong</p> |

### Style

| Setting         | Description                       | Options                                                          |
| --------------- | --------------------------------- | ---------------------------------------------------------------- |
| Border position | Controls which sides have borders | <p>• None (default)<br>• Top<br>• Bottom<br>• Top and bottom</p> |

### Layout

| Setting       | Description                  | Options                   |
| ------------- | ---------------------------- | ------------------------- |
| Row desktop   | Number of columns on desktop | 1 - 8 (default: 5)        |
| Row mobile    | Number of columns on mobile  | 1 - 3 (default: 2)        |
| Enable margin | Adds margin around the grid  | Checkbox (default: false) |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
