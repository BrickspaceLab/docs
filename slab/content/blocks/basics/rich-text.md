# Rich text

<figure><img src="../../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

## Overview

A flexible rich text content block that allows for formatted text content with customizable text color, alignment, and responsive visibility options.

## Common use cases

* Use for any formatted text content like paragraphs, headings, lists
* Consider text color contrast when using force light/dark options
* Use visibility options to create different content for mobile/desktop
* Default text alignment is left-aligned for better readability

## Block settings

### Content

| Setting | Description                      | Options         |
| ------- | -------------------------------- | --------------- |
| Content | The main text content to display | Rich text input |

### Spacing

| Setting                   | Description                                | Options                   |
| ------------------------- | ------------------------------------------ | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the content | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the content        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the content     | Checkbox (default: false) |

### Color

| Setting    | Description             | Options                                                                                                                                                                                                                                                      |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Text color | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade</p> |

### Style

| Setting        | Description                                        | Options                                                                                                                                                                       |
| -------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family    | Controls the font family used for the text         | <p>• Standard (default)<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--' or font size is "custom"</p>                                 |
| Font size      | Controls the font size of the text                 | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6<br>• Custom</p> |
| Size           | Custom font size when using custom typography      | <p>4 - 200 px (default: 16)<br><br>Visible when font size is "custom"</p>                                                                                                     |
| Line height    | Custom line height when using custom typography    | <p>100 - 300 % (default: 150)<br><br>Visible when font size is "custom"</p>                                                                                                   |
| Letter spacing | Custom letter spacing when using custom typography | <p>-3 - 3 rem (default: 0)<br><br>Visible when font size is "custom"</p>                                                                                                      |

### Layout

| Setting              | Description                                  | Options                                                     |
| -------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| Horizontal alignment | Controls horizontal text alignment           | <p>• Left (default)<br>• Center<br>• Justify<br>• Right</p> |
| Enable max width     | Limits the maximum width of the text content | Checkbox (default: true)                                    |

### Display

| Setting          | Description                               | Options                                                                                                    |
| ---------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Visibility       | Controls when the block is visible        | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                  |
| Scroll animation | Adds scroll-based animations to the block | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
