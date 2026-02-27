# Image


## Overview

A flexible image block component that renders a single image with customizable styling options. Supports responsive display, color schemes, aspect ratios, and alignment controls.


## Common use cases

- Consider image optimization by setting appropriate max_width
- Choose aspect ratio based on image content and layout needs
- Utilize color schemes to maintain fallback colors or backgrounds when using transparent images


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Image | The image to display | Image picker |


### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Adds horizontal padding around the content | Checkbox (default: false) |
| Enable top padding | Adds top padding around the content | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding around the content | Checkbox (default: false) |


### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Color scheme | Controls the background color scheme | • Body (default)<br>• Neutral<br>• Accent 1<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur |
| Border color | Controls the border color | • Body<br>• Subtle (default)<br>• Strong<br>• Primary<br>• Secondary<br>• Tertiary<br>• None<br><br>Visible when border position is not empty |


### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Border position | Controls which sides have borders | • None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All |
| Radius | Controls the border radius | • None (default)<br>• Default<br>• Sm<br>• Md<br>• Lg<br>• Xl<br>• 2xl<br>• Full |
| Enable aspect ratio | Forces the image to maintain a specific aspect ratio | Checkbox (default: false) |
| Aspect ratio | The aspect ratio to maintain | • Square<br>• Landscape<br>• Portrait<br>• None<br><br>Visible when enable aspect ratio is true |


### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Width | Controls the width of the image | 5 - 100 % (default: 100) |
| Horizontal alignment | Controls horizontal alignment | • Left (default)<br>• Center<br>• Right |


### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls when the block is visible | • All (default)<br>• Mobile only<br>• Desktop only |
| Scroll animation | Adds scroll-based animations to the block | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
