# Block reveal

### Section overview

The Block Reveal section is a dynamic content display that reveals different content blocks when a user hovers, clicks, or scrolls through a list of titles. It creates an interactive experience by seamlessly transitioning between content blocks.

#### Common use cases

* Product feature showcases where each title reveals detailed information about a specific feature
* FAQ sections where clicking on questions reveals the answers
* Step-by-step guides or processes where each step is revealed in sequence
* Portfolio showcases where different projects can be browsed through titles

#### Usage tips

* Keep title text concise for better readability, especially on mobile devices
* Ensure content blocks have similar heights for a consistent user experience
* Consider using the hover reveal option for desktop but rely on click actions for mobile
* Use complementary colors for titles and content to create visual hierarchy
* For scroll-based reveals, ensure the section has sufficient vertical space to properly trigger transitions

### Section settings

| Setting                | Description                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Enable hover reveal    | When enabled, hovering over a title will reveal its content (default: disabled)    |
| Top spacing            | Sets the padding at the top of the section (default: 100px)                        |
| Bottom spacing         | Sets the padding at the bottom of the section (default: 100px)                     |
| Color scheme           | Controls the background color of the section (default: body)                       |
| Custom color           | Sets a custom background color when custom color scheme is selected                |
| Text color             | Forces text to be light or dark, or uses the default based on the background       |
| Border color           | Controls the color of the section border (options: subtle or strong)               |
| Enable color fade      | Enables smooth color transitions as user scrolls through the section               |
| Border position        | Controls where borders appear on the section (options: none, top, bottom, or both) |
| Column width           | Sets the width of the content column as a percentage (default: 50%)                |
| Enable margin          | Applies horizontal margin from global theme settings (default: enabled)            |
| Enable swapped columns | Reverses the position of the titles and content columns (default: disabled)        |
| Visibility             | Controls whether the section appears on all devices, mobile only, or desktop only  |

### Block settings

#### Content

The Content block represents each individual item in the reveal section, consisting of a title that triggers the display of its associated content.

* Block limit: 50 blocks

| Setting                  | Description                                                                  |
| ------------------------ | ---------------------------------------------------------------------------- |
| Title                    | The title text shown in the list of clickable/hoverable items                |
| Heading                  | The heading text displayed in the content area                               |
| Content                  | Rich text content to display when this block is selected                     |
| Button label             | Text for the optional button                                                 |
| Url                      | Link destination for the button                                              |
| Image                    | Optional image to display with the content                                   |
| Show image as background | Displays the image as a background instead of inline                         |
| Video                    | Optional video to display with the content                                   |
| Enable autoplay          | Automatically plays the video when the block is revealed (default: enabled)  |
| Enable mute toggle       | Shows a mute/unmute button for videos (default: enabled)                     |
| Enable loop              | Continuously loops the video playback (default: enabled)                     |
| Minimum height           | Sets the minimum height for the content area in pixels (default: 250px)      |
| Enable padding           | Adds padding inside the content block (default: enabled)                     |
| Color scheme             | Controls the background color of the content block                           |
| Border color             | Controls the color of the content block border                               |
| Text color               | Forces text to be light or dark, or uses the default based on the background |
| Button color             | Selects from various button styles (primary, secondary, outline, etc.)       |
| Enable gradient          | Applies a gradient effect to the block background                            |
| Title size               | Controls the font size of the title in the list                              |
| Text position            | Positions text above or below media (image/video)                            |
| Vertical alignment       | Aligns content vertically (top, middle, bottom)                              |
| Horizontal alignment     | Aligns content horizontally (left, center, justify, right)                   |
