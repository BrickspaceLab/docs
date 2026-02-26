# Video


## Overview

A customizable video block component that supports both native and custom video controls. Provides flexible styling options including color schemes, button styles, and layout controls.


## Common use cases

* Embed promotional videos on homepage or landing pages
* Showcase product demonstrations
* Display brand storytelling content with custom controls


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|----------|
| Video | The video file to display | Video picker |
| Enable autoplay | Automatically plays the video when loaded | Checkbox (default: true) |
| Enable loop | Restarts video when it ends | Checkbox (default: true) |
| Show default video controls | Shows native browser video controls | Checkbox (default: false) |
| Show custom video controls | Shows custom branded play/pause controls | Checkbox (default: true) |

### Spacing

| Setting | Description | Options |
|---------|-------------|----------|
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding | Adds top padding | Checkbox (default: false) |
| Enable bottom padding | Adds bottom padding | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|----------|
| Type | Controls color mode (custom or base) | <p>• Custom<br>• Base (default)<br><br>Visible when enable_inheritance is false</p> |
| Scheme | Select a custom color scheme | <p>Color scheme picker<br><br>Visible when color_type is custom and enable_inheritance is false</p> |
| Scheme | Controls the background and text colors | <p>• Body<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Border | Controls the border color | <p>• None<br>• Subtle (default)<br>• Strong<br>• Body foreground<br><br>Visible when color_type is base and enable_inheritance is false</p> |
| Enable inheritance | Inherit colors from parent block | Checkbox (default: false) |

### Style

| Setting | Description | Options |
|---------|-------------|----------|
| Width | Controls the width of the block | 5 - 100 % (default: 100 %) |
| Minimum width | Minimum width of the block | 5 - 500 px (default: 500 px) |
| Radius | Controls the border radius | <p>• None<br>• Default (default)<br>• Small<br>• Medium<br>• Large<br>• 1x Large<br>• 2x Large<br>• Full</p> |

### Layout

| Setting | Description | Options |
|---------|-------------|----------|
| Horizontal alignment | Controls horizontal alignment | <p>• Left (default)<br>• Center<br>• Right</p> |

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Visibility | Controls when the block is visible | <p>• Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only</p> |
