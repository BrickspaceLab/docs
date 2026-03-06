# Form response

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Overview

A dynamic error message display block that renders error text from an Alpine.js store. Provides customizable styling options including text color, font family, size, alignment, and responsive visibility controls.

## Common use cases

* Enable max\_width (default: true) for better readability of error messages
* Consider the context where errors will appear when choosing text color and size
* Use appropriate padding settings based on surrounding content
* Display form submission feedback and validation messages

## Block settings

### Spacing

| Setting                   | Description                                | Options                   |
| ------------------------- | ------------------------------------------ | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the content | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the content        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the content     | Checkbox (default: false) |

### Color

| Setting    | Description             | Options                                                                                                                                                                                                                                                                              |
| ---------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Text color | Controls the text color | <p>• Default (default)<br>• Alternative<br>• Primary background<br>• Primary foreground<br>• Secondary background<br>• Secondary foreground<br>• Tertiary background<br>• Tertiary foreground<br>• Neutral background<br>• Neutral foreground<br>• Shade<br>• Error<br>• Success</p> |

### Style

| Setting     | Description                                | Options                                                                                                                                                           |
| ----------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for the text | <p>• Standard<br>• Heading<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--'</p>                                                        |
| Font size   | Controls the font size of the text         | <p>• Smaller<br>• Small<br>• Default (default)<br>• Big<br>• Bigger<br>• Heading 1<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Layout

| Setting              | Description                                  | Options                                                     |
| -------------------- | -------------------------------------------- | ----------------------------------------------------------- |
| Horizontal alignment | Controls horizontal text alignment           | <p>• Left (default)<br>• Center<br>• Justify<br>• Right</p> |
| Enable max width     | Limits the maximum width of the text content | Checkbox (default: true)                                    |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
