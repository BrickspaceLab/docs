# Video

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

## Overview

A customizable video block component that supports both native and custom video controls. Provides flexible styling options including color schemes, button styles, and layout controls. Supports responsive design with mobile/desktop visibility options and customizable width and alignment.

## Common use cases

* Embed promotional videos on homepage
* Showcase product demonstrations
* Display brand storytelling content
* Create engaging video backgrounds
* Add instructional or educational videos

## Compatible blocks

The following blocks can be nested within this block:

* [Container](../layout/container.md)

## Block settings

### General

| Setting | Description | Options |
| --- | --- | --- |
| Show advanced settings | Reveals visibility settings | Checkbox (default: false) |

### Content

| Setting                | Description                               | Options                   |
| ---------------------- | ----------------------------------------- | ------------------------- |
| Video                  | The video file to display                 | Video picker              |
| Autoplay video         | Automatically plays the video when loaded | Checkbox (default: true)  |
| Loop video             | Restarts video when it ends               | Checkbox (default: true)  |
| Default video controls | Shows native browser video controls       | Checkbox (default: false) |
| Custom video controls  | Shows custom branded play/pause controls  | Checkbox (default: true)  |

### Spacing

| Setting                   | Description                                  | Options                   |
| ------------------------- | -------------------------------------------- | ------------------------- |
| Enable horizontal padding | Adds horizontal padding inside the container | Checkbox (default: false) |
| Enable top padding        | Adds top padding                             | Checkbox (default: false) |
| Enable bottom padding     | Adds bottom padding                          | Checkbox (default: false) |

### Color

| Setting | Description | Options |
| --- | --- | --- |
| Type | Selects color mode | <p>• Custom<br>• Base (default)</p><br><br>Visible when **Enable inheritance** is off |
| Scheme | Custom color scheme picker | <p>Color scheme picker</p><br><br>Visible when **Type** is **Custom** and **Enable inheritance** is off |
| Color scheme | Controls the background color scheme | <p>• Body background<br>• Body foreground<br>• Accent 1 (default)<br>• Accent 2<br>• Accent 3<br>• Shade 1<br>• Shade 2<br>• Shade 3<br>• Blur<br>• Transparent</p><br><br>Visible when **Type** is **Base** and **Enable inheritance** is off |
| Border color | Controls the border color | <p>• None (default)<br>• Subtle<br>• Strong</p><br><br>Visible when **Border position** is not **None**, **Type** is **Base**, and **Enable inheritance** is off |
| Enable inheritance | Inherits color settings from parent block | Checkbox (default: false) |

### Style

| Setting         | Description                               | Options                                                                                                            |
| --------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Width           | Controls the width of the video container | 5 - 100 % (default: 100)                                                                                           |
| Minimum width   | Minimum width of the video container      | <p>5 - 500 px (default: 500)</p><br><br>Visible when **Width** is less than 100 |
| Border position | Controls where borders appear on the video | <p>• None (default)<br>• Top<br>• Bottom<br>• Left<br>• Right<br>• Top and bottom<br>• Left and right<br>• All</p> |
| Radius          | Controls the border radius                | <p>• None<br>• Default (default)<br>• Sm<br>• Md<br>• Lg<br>• Xl<br>• 2xl<br>• Full</p>                            |

### Layout

| Setting              | Description                                | Options                                        |
| -------------------- | ------------------------------------------ | ---------------------------------------------- |
| Horizontal alignment | Controls horizontal alignment of the video | <p>• Left (default)<br>• Center<br>• Right</p><br><br>Visible when **Width** is less than 100 |

### Display

| Setting    | Description                        | Options                                                   |
| ---------- | ---------------------------------- | --------------------------------------------------------- |
| Visibility | Controls when the block is visible | <p>• All (default)<br>• Mobile only<br>• Desktop only</p><br><br>Visible when **Show advanced settings** is on|
