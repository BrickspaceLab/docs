# Static chat

### Section overview

The Static chat section creates a simulated chat interface for your Shopify store, allowing you to display conversations with animated typing indicators, timed message reveals, and support for text, avatars, images, and videos.

#### Common use cases

* Creating interactive customer support demonstrations
* Showcasing product Q\&A in a conversational format
* Displaying testimonials or customer experiences in a chat-like interface
* Creating guided tutorials or onboarding flows in a friendly chat format

#### Usage tips

* Use the delay settings to create a natural conversation flow by timing message appearances
* Alternate between left and right alignment to create the appearance of a two-person conversation
* For best readability, keep your column width between 50-70% on desktop
* Add avatar blocks after text blocks to create a more personalized conversation experience

Mobile responsiveness considerations:

* The chat interface automatically adapts to smaller screens, with content reflow
* Consider using shorter messages for better mobile readability
* Test your chat section on mobile to ensure the timing feels natural on smaller screens

### Section settings

| Setting              | Description                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------- |
| Top spacing          | Controls the amount of padding above the chat section (in pixels)                         |
| Bottom spacing       | Controls the amount of padding below the chat section (in pixels)                         |
| Color scheme         | Sets the background color for the entire chat section                                     |
| Custom color         | Allows choosing a custom background color when "Custom" is selected as the color scheme   |
| Text color           | Controls the text color for the entire section (default, light, or dark)                  |
| Border color         | Sets the color for any borders (subtle or strong)                                         |
| Enable color fade    | Makes the background and text color fade in when the section enters the viewport          |
| Border position      | Controls where borders appear (none, top, bottom, or both)                                |
| Horizontal alignment | Sets the horizontal alignment of the chat column (left, center, or right)                 |
| Column width         | Controls the width of the chat content column as a percentage of the container on desktop |
| Enable margin        | When enabled, adds horizontal margin to the section                                       |
| Visibility           | Controls when the section is visible (all devices, mobile only, or desktop only)          |

### Block settings

#### Text

Text blocks display chat messages with typing indicators and timed reveals. Each text block can be styled and positioned independently.

Limit: 50 blocks

| Setting              | Description                                                         |
| -------------------- | ------------------------------------------------------------------- |
| Content              | Rich text editor for the message content                            |
| Color scheme         | Sets the background and text color for this message bubble          |
| Horizontal alignment | Controls whether the message appears on the left or right side      |
| Delay                | Sets how many seconds to wait before revealing this message (0-10s) |

#### Avatar

Avatar blocks display a profile image with a timestamp, typically used to indicate who is speaking in the conversation.

Limit: 50 blocks

| Setting              | Description                                                                   |
| -------------------- | ----------------------------------------------------------------------------- |
| Image                | The profile image to display (shows a placeholder if none selected)           |
| Time                 | Text displayed next to the avatar (typically shows when the message was sent) |
| Horizontal alignment | Controls whether the avatar appears on the left or right side                 |

#### Image

Image blocks display an image within the chat interface, with typing indicators and timed reveals.

Limit: 50 blocks

| Setting              | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| Image                | The image to display in the chat (shows a placeholder if none selected) |
| Horizontal alignment | Controls whether the image appears on the left or right side            |
| Delay                | Sets how many seconds to wait before revealing this image (0-10s)       |

#### Video

Video blocks embed videos in the chat interface, with typing indicators and timed reveals.

| Setting              | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| Video                | The video to display in the chat                                  |
| Enable autoplay      | When enabled, the video plays automatically when revealed         |
| Enable mute toggle   | When enabled, displays a button to toggle sound on/off            |
| Enable loop          | When enabled, the video will repeat continuously                  |
| Horizontal alignment | Controls whether the video appears on the left or right side      |
| Delay                | Sets how many seconds to wait before revealing this video (0-10s) |
