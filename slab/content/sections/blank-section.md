# Blank section

### Section overview

The Section component is Slab's general-purpose section container. It supports theme and app blocks, optional full-section linking, background media, and shared spacing, color, and display controls.

#### Common use cases

* Building custom page sections without creating a specialized section file.
* Grouping multiple theme or app blocks inside one configurable wrapper.
* Making an entire section clickable with a single URL setting.
* Applying reusable spacing and visibility behavior across many templates.

#### Usage tips

* Use this section when no specialized template section is required.
* Set a section URL only when every child element should share the same destination.
* Keep spacing and minimum height values consistent with surrounding sections.
* Test hide-on-scroll and overlap behaviors on both desktop and mobile.

### Section settings

| Setting | Description |
| --- | --- |
| URL | Optional link for the entire section wrapper. |
| Enable background image or video | Turns on background media rendering for the section. |
| Image background desktop | Background image used on desktop. |
| Image background mobile | Optional background image override for mobile. |
| Video background | Optional background video source. |
| Show video on mobile | Enables background video playback on mobile devices. |
| Show entire image | Displays full image rather than cropping to fill. |
| Top spacing | Adds top padding to the section container. |
| Bottom spacing | Adds bottom padding to the section container. |
| Minimum height | Sets a minimum section height. |
| Gap size | Controls spacing between child layout elements. |
| Color scheme | Sets section background and text color treatment. |
| Color border | Sets section border color style. |
| Border position | Controls where borders appear. |
| Vertical alignment | Aligns content vertically within the section. |
| Enable margin | Applies global horizontal margin settings. |
| Show above | Raises section stacking order above neighboring sections. |
| Enable hide on scroll | Collapses section after scroll state is triggered. |
| Enable header overlap | Allows section to overlap the header when enabled globally. |
| Scroll snap align | Applies scroll snap alignment when enabled globally. |
| Visibility | Controls device visibility (all, mobile, or desktop). |

### Block settings

This section supports both theme and app blocks:

* `@theme`
* `@app`
