# Countdown

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

## Overview

A dynamic countdown timer block that displays days, hours, minutes, and seconds until a specified date and time. Uses Alpine.js for real-time updates and supports customizable styling options.

## Common use cases

* Create urgency for limited-time promotions or sales
* Display event countdown timers
* Show time remaining for product launches or announcements
* Automatically hide when countdown expires

## Block settings

### Content

| Setting        | Description                                                      | Options                     |
| -------------- | ---------------------------------------------------------------- | --------------------------- |
| Countdown date | Target date for the countdown                                    | Text input                  |
| Countdown time | Target time for the countdown                                    | Text input (default: 00:00) |
| Show labels    | Displays labels (Days, Hours, Minutes, Seconds) above each value | Checkbox (default: true)    |

### Spacing

| Setting                   | Description                                | Options                   |
| ------------------------- | ------------------------------------------ | ------------------------- |
| Enable horizontal padding | Adds horizontal padding around the content | Checkbox (default: false) |
| Enable top padding        | Adds top padding around the content        | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding around the content     | Checkbox (default: false) |

### Color

| Setting      | Description                                      | Options                                                                                                                                                                                    |
| ------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Color scheme | Controls the background color scheme             | <p>• Body<br>• Neutral<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Primary<br>• Secondary<br>• Tertiary<br>• Blur<br>• Transparent</p> |
| Border color | Controls the border color between timer segments | <p>• Subtle (default)<br>• Strong<br>• None</p>                                                                                                                                            |

### Style

| Setting     | Description                                         | Options                                                                                                                                                           |
| ----------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Font family | Controls the font family used for the timer numbers | <p>• Standard<br>• Heading (default)<br>• Subheading<br>• Accent<br><br>Visible when font size contains 'type--'</p>                                              |
| Font size   | Controls the font size of the timer numbers         | <p>• Smaller<br>• Small<br>• Default<br>• Big<br>• Bigger<br>• Heading 1 (default)<br>• Heading 2<br>• Heading 3<br>• Heading 4<br>• Heading 5<br>• Heading 6</p> |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p> |
