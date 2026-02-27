# Layout marquee

## Overview

A marquee layout block that creates a scrolling effect for its child blocks. It supports various customization options such as animation duration, pause on hover, reverse animation, and alignment settings. This block is ideal for showcasing featured content in a dynamic and engaging manner.

## Common use cases

* Highlight important announcements or featured products with a scrolling marquee
* Adjust animation settings to create a smooth and visually appealing effect
* Consider the content length when setting the animation duration to avoid abrupt loops
* Use pause on hover for better user interaction

## Compatible blocks

The following blocks can be nested within this block:

* [Rich text](../basics/rich-text.md)
* [Image](../basics/image.md)
* [Icon](../basics/icon.md)
* [Button](../basics/button.md)
* [Container](../containers/container.md)

## Block settings

### Content

| Setting                  | Description                                     | Options                   |
| ------------------------ | ----------------------------------------------- | ------------------------- |
| Animation duration       | Duration of the marquee animation in seconds    | 1 - 90 s (default: 60)    |
| Enable pause on hover    | Pauses animation when hovering over the marquee | Checkbox (default: false) |
| Enable reverse animation | Reverses the scroll direction                   | Checkbox (default: false) |

### Spacing

| Setting                   | Description                                | Options                   |
| ------------------------- | ------------------------------------------ | ------------------------- |
| Top spacing               | Padding space at the top of the marquee    | 0 - 300 px (default: 0)   |
| Bottom spacing            | Padding space at the bottom of the marquee | 0 - 300 px (default: 0)   |
| Enable horizontal padding | Adds horizontal padding around the marquee | Checkbox (default: false) |

### Color

| Setting      | Description                             | Options                                                                                                                                                                                    |
| ------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background and text colors | <p>• Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default)</p> |
| Color border | Controls the border color               | <p>• Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank</p>                                       |

### Style

| Setting          | Description                       | Options                                                                                                            |
| ---------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Block max height | Maximum height for block elements | 0 - 500 px (default: 100)                                                                                          |
| Border position  | Controls where borders appear     | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |

### Layout

| Setting            | Description                            | Options                                        |
| ------------------ | -------------------------------------- | ---------------------------------------------- |
| Vertical alignment | Controls vertical alignment of content | <p>• Top<br>• Middle (default)<br>• Bottom</p> |

### Display

| Setting          | Description                        | Options                                                                                                    |
| ---------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Adds scroll-triggered animations   | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
