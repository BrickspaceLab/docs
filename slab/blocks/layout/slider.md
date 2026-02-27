# Slider


## Overview

A flexible slider/carousel container component that provides smooth scrolling functionality for child content blocks. Features auto-scroll capabilities, navigation arrows, progress indicators, and responsive behavior. All JavaScript functionality is contained within Alpine.js x-data attributes for efficient performance.


## Common use cases

- Create image carousels or product sliders
- Display featured content in a scrollable horizontal layout
- Use auto-scroll for automatic content rotation
- Add navigation controls for user interaction
- Show progress indicators to display slide position
- Enable scroll animations for engaging content reveals


## Compatible blocks

The following blocks can be nested within this block:

- [Slider item](slider-item.md)
- [Slider products](../all-pagination/slider-products.md)
- [Slider articles](../all-pagination/slider-articles.md)
- [Slider collections](../all-pagination/slider-collections.md)
- [Slider gallery](../all-pagination/slider-gallery.md)
- [Slider recommendations](../all-pagination/slider-product-recommendations.md)
- [Slider recent](../all-pagination/slider-recently-viewed.md)


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Show arrows | Displays navigation arrows for the slider | Checkbox (default: true) |
| Show indicators | Displays progress indicators (dots or numbers) | Checkbox (default: true) |
| Show controls on hover | Shows controls only when hovering over the slider | Checkbox (default: false)<br><br>Visible when show arrows or show indicators is true |
| Show scrollbar | Displays a scrollbar for the slider | Checkbox (default: false) |
| Show progress bar | Displays a progress bar at the top of the slider | Checkbox (default: false)<br><br>Visible when enable auto scroll is true |
| Enable instant transition | Removes smooth scrolling for instant slide changes | Checkbox (default: false) |
| Enable auto scroll | Automatically scrolls through slides | Checkbox (default: false) |
| Auto scroll delay | Time delay between auto-scroll transitions | 0 - 20 s (default: 0)<br><br>Visible when enable auto scroll is true |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Padding space at the top of the slider | 0 - 300 px (default: 0) |
| Bottom spacing | Padding space at the bottom of the slider | 0 - 300 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding around the slider | Checkbox (default: false) |
| Gap size | Controls spacing between slider items | • None<br>• Default (default)<br>• XS<br>• SM<br>• MD<br>• LG<br>• XL |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background and text colors | • Body<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent (default) |
| Color border | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not blank |
| Color arrow | Controls the color of navigation arrows | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline<br>• Inverted outline<br>• Blur<br>• Link<br>• Inverted link<br><br>Visible when show arrows is true |
| Color indicator | Controls the color of progress indicators | • Primary<br>• Secondary<br>• Tertiary<br>• Neutral<br>• Plain<br>• Outline<br>• Inverted outline<br>• Blur<br>• Transparent<br><br>Visible when show indicators is true |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Button size | Controls the size of navigation arrow buttons | • Extra small<br>• Small (default)<br>• Standard<br>• Large<br><br>Visible when show arrows is true |
| Border position | Controls where borders appear | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |
| Indicator radius | Controls the border radius of progress indicators | • None<br>• Default (default)<br>• Sm<br>• Md<br>• Lg<br>• Xl<br>• 2xl<br>• Full |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Vertical alignment | Controls vertical alignment of slider items | • Top (default)<br>• Middle<br>• Bottom |
| Control alignment | Controls horizontal alignment of navigation controls | • Left<br>• Center<br>• Right (default)<br><br>Visible when show arrows or show indicators is true |
| Control placement | Controls vertical placement of navigation controls | • Top (default)<br>• Middle<br>• Bottom<br>• Under<br><br>Visible when show arrows or show indicators is true |
| Enable scroll margin | Applies margin based on theme settings for scroll padding | Checkbox (default: false) |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-triggered animations | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
