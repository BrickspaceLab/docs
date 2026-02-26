# Rich text


## Overview

A flexible rich text content block that allows for formatted text content with customizable typography, text color, alignment, and responsive visibility options. Supports scroll-based animations and custom font sizing with line height and letter spacing controls.


## Common use cases

* Display formatted text content such as paragraphs, headings, and lists
* Use custom typography settings for unique text presentations
* Configure scroll animations for engaging page transitions


## Block settings

### Content

| Setting | Description | Options |
|---------|-------------|---------|
| Content | Controls the content | Rich text input |

### Spacing

| Setting | Description | Options |
|---------|-------------|---------|
| Enable horizontal padding | Controls the enable horizontal padding | Checkbox (default: false) |
| Enable top padding | Controls the enable top padding | Checkbox (default: false) |
| Enable bottom padding | Controls the enable bottom padding | Checkbox (default: false) |

### Color

| Setting | Description | Options |
|---------|-------------|---------|
| Type | Controls the type | <p>• Custom<br>• Base (default)<br><br>Visible when enable inheritance is false</p> |
| Text color | Controls the text color | <p>Color scheme picker<br><br>Visible when color type is custom and enable inheritance is false</p> |
| Text color | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Link<br>• Error<br>• Success<br>• Shade 1<br>• Shade 2<br>• Shade 3<br><br>Visible when color type is base and enable inheritance is false</p> |
| Enable inheritance | Colors will be inherited from the closest parent block that has a set scheme. | Checkbox (default: true) |

### Style

| Setting | Description | Options |
|---------|-------------|---------|
| Font family | Controls the font family | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains type-- or font size is custom</p> |
| Font size | Controls the font size | • Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br>• Custom |
| Size | Controls the size | <p>4 – 200 px (default: 16)<br><br>Visible when font size is custom</p> |
| Line height | Controls the line height | <p>100 – 300 % (default: 150)<br><br>Visible when font size is custom</p> |
| Letter spacing | Controls the letter spacing | <p>-3 – 3 rem (default: 0)<br><br>Visible when font size is custom</p> |

### Layout

| Setting | Description | Options |
|---------|-------------|---------|
| Horizontal alignment | Controls the horizontal alignment | • Left (default)<br>• Center<br>• Justify<br>• Right |
| Enable max width | Controls the enable max width | Checkbox (default: true) |

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Visibility | Controls the visibility | • Show on all devices (default)<br>• Show on mobile only<br>• Show on desktop only |
| Scroll animation | Controls the scroll animation | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
