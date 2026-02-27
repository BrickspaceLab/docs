# Container


## Overview

The Container block is a fundamental building block that serves as a flexible wrapper for organizing and styling content. It can hold any theme or app blocks and provides extensive customization options for spacing, colors, borders, backgrounds, positioning, and layout. Think of it as a versatile box that can be styled in countless ways to group related content, create visual sections, add backgrounds, and control how content appears and behaves on your pages.

The Container block is used extensively throughout the theme to create structured layouts, organize content, and apply consistent styling to groups of blocks. It's the foundation for building complex layouts while maintaining flexibility and design consistency.


## Common use cases

- Group related blocks with consistent spacing and styling
- Create visually distinct sections with background colors or images
- Build card-like layouts with borders, radius, and padding
- Organize content within accordions, dropdowns, and other nested structures
- Create clickable card sections by adding a URL
- Implement sticky navigation bars or headers
- Build overlay content that appears on top of other elements
- Create hover-reveal content with the "Show on hover" option
- Control responsive layouts with device-specific visibility settings
- Add scroll-triggered animations to content sections


## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| URL | Optional URL to make the entire container clickable | URL input |
| Enable background image or video | Enables background image or video settings | Checkbox (default: false) |
| Image background desktop | Desktop background image | Image picker<br><br>Visible when enable background image or video is true |
| Image background mobile | Mobile background image | Image picker<br><br>Visible when enable background image or video is true |
| Video background | Background video | Video picker<br><br>Visible when enable background image or video is true |
| Show video on mobile | Displays video on mobile devices | Checkbox (default: true)<br><br>Visible when enable background image or video is true |
| Show entire image | Shows the full image without cropping | Checkbox (default: false)<br><br>Visible when enable background image or video is true |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Top spacing | Spacing above the container | 0 - 300 px (default: 0) |
| Bottom spacing | Spacing below the container | 0 - 300 px (default: 0) |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable vertical padding | Adds vertical padding inside the container | Checkbox (default: false) |
| Enable margin | Adds margin around the container | Checkbox (default: false) |
| Gap size | Spacing between child blocks | • None<br>• Default (default)<br>• Xs<br>• Sm<br>• Md<br>• Lg<br>• Xl |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background color scheme | • Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent |
| Border color | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not empty |
| Enable color difference | Applies color blend mode for overlay effects | Checkbox (default: false) |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls which sides have borders | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |
| Radius | Controls the border radius | • None<br>• Default (default)<br>• Sm<br>• Md<br>• Lg<br>• Xl<br>• 2xl<br>• Full |
| Enable crop | Clips content that overflows the container | Checkbox (default: true) |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Width | Controls the width of the container | 5 - 100 % (default: 100) |
| Minimum height | Minimum height of the container | 0 - 1200 px (default: 0)<br><br>Visible when enable height fill is false |
| Enable height fill | Fills the container to the height of the parent | Checkbox (default: true) |
| Enable overlay | Positions the container as an absolute overlay | Checkbox (default: false) |
| Show on hover | Only displays the container on hover | Checkbox (default: false) |
| Enable block elevation | Increases z-index for sticky positioning | Checkbox (default: false)<br><br>Visible when enable sticky layout is true |
| Enable sticky layout | Makes the container stick to viewport while scrolling | Checkbox (default: false) |
| Sticky position | Position where the container sticks | • None (default)<br>• Top<br>• Bottom<br><br>Visible when enable sticky layout is true |
| Vertical alignment | Controls vertical alignment of content | • Top (default)<br>• Middle<br>• Bottom |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-based animations to the block | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
