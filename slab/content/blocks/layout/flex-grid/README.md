# Flex grid

<figure><img src="../../../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible container component that provides customizable flex layout options for child blocks. Enables responsive alignment, spacing, and visibility controls through the theme editor. Supports both horizontal and vertical flex directions with comprehensive alignment options.

## Common use cases

* Create flexible row or column layouts for content organization
* Use horizontal direction for side-by-side content arrangements
* Use vertical direction for stacked content layouts
* Configure gap sizes to control spacing between flex items
* Adjust alignment settings to position content within the flex container

## Compatible blocks

The following blocks can be nested within this block:

* [Flex item](flex-item.md)

## Block settings

### Spacing

| Setting                   | Description                                  | Options                                                                      |
| ------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------- |
| Top spacing               | Padding space at the top of the container    | 0 - 300 px (default: 0)                                                      |
| Bottom spacing            | Padding space at the bottom of the container | 0 - 300 px (default: 0)                                                      |
| Enable horizontal padding | Adds horizontal padding around the container | Checkbox (default: false)                                                    |
| Gap size                  | Controls spacing between flex items          | <p>• None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL</p> |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default)</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank</p>                                       |

### Style

| Setting         | Description                   | Options                                                                                                            |
| --------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Border position | Controls where borders appear | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting                       | Description                                                | Options                                                                                                             |
| ----------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Direction                     | Controls the flex direction                                | <p>• Horizontal (default)<br>• Vertical</p>                                                                         |
| Horizontal alignment (row)    | Controls horizontal alignment when direction is horizontal | <p>• Left (default)<br>• Center<br>• Right<br>• Between<br><br>Visible when direction is horizontal</p>             |
| Vertical alignment (row)      | Controls vertical alignment when direction is horizontal   | <p>• Start (default)<br>• Middle<br>• End<br>• Between<br>• Stretch<br><br>Visible when direction is horizontal</p> |
| Vertical alignment (column)   | Controls vertical alignment when direction is vertical     | <p>• Start (default)<br>• Middle<br>• End<br>• Between<br><br>Visible when direction is vertical</p>                |
| Horizontal alignment (column) | Controls horizontal alignment when direction is vertical   | <p>• Left<br>• Center<br>• Right<br>• Between<br>• Stretch (default)<br><br>Visible when direction is vertical</p>  |

### Display

| Setting          | Description                        | Options                                                                                                    |
| ---------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Adds scroll-triggered animations   | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
