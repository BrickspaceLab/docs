# Tabs

### Section overview

The Tabs section creates horizontal tabs that can display different content blocks when selected. It provides a clean, organized way to present multiple information categories within a single section.

#### Common use cases

* Product information display (specifications, warranty, shipping details)
* FAQ or help sections with categorized information
* Location and contact information with maps and details
* Presenting step-by-step instructions or processes

#### Usage tips

* Use clear, concise tab names that accurately describe the content
* Limit the number of tabs to 3-5 for better usability
* For mobile views, consider using the split layout option for better readability
* Keep content within each tab focused and consistent in structure across tabs

### Section settings

| Setting          | Description                                                                       |
| ---------------- | --------------------------------------------------------------------------------- |
| Tabs             | Comma-separated list of tab names that will be displayed as selectable options    |
| Heading          | Main heading displayed above the tabs                                             |
| Content          | Rich text content displayed below the heading                                     |
| Button label     | Text for the optional button                                                      |
| Button URL       | URL for the optional button                                                       |
| Top spacing      | Amount of padding above the section (0-300px)                                     |
| Bottom spacing   | Amount of padding below the section (0-300px)                                     |
| Color scheme     | Background and text color combination for the section                             |
| Border color     | Color for section borders                                                         |
| Button color     | Color scheme for the section's button                                             |
| Border position  | Where borders appear on the section (none, top, bottom, or both)                  |
| X alignment      | Horizontal alignment of content (left, center, or right)                          |
| Enable margin    | When enabled, applies horizontal margin to the section                            |
| Enable max width | When enabled, restricts content width to improve readability                      |
| Enable split     | When enabled, displays header and content in a side-by-side layout                |
| Visibility       | Controls section visibility on different devices (all, mobile only, desktop only) |

### Block settings

#### Heading

A simple text heading block to create section titles within a tab.

| Setting | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| Tab     | The tab name this block should appear in (must match a tab name from section settings) |
| Content | Heading text to display                                                                |

#### Content

A rich text content block for adding formatted text within a tab.

| Setting | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| Tab     | The tab name this block should appear in (must match a tab name from section settings) |
| Content | Rich text content to display                                                           |

#### Buttons

Adds one or two buttons within a tab.

| Setting                | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| Tab                    | The tab name this block should appear in (must match a tab name from section settings) |
| Button label           | Text for the primary button                                                            |
| Button URL             | URL for the primary button                                                             |
| Color button           | Color scheme for the primary button                                                    |
| Secondary button label | Text for the secondary button                                                          |
| Secondary button URL   | URL for the secondary button                                                           |
| Secondary color button | Color scheme for the secondary button                                                  |

#### Image

Displays an image within a tab.

| Setting | Description                                                                            |
| ------- | -------------------------------------------------------------------------------------- |
| Tab     | The tab name this block should appear in (must match a tab name from section settings) |
| Image   | The image to display                                                                   |

#### Video

Embeds a video within a tab.

| Setting            | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| Tab                | The tab name this block should appear in (must match a tab name from section settings) |
| Video              | The video to display                                                                   |
| Enable autoplay    | When enabled, automatically plays the video when tab is selected                       |
| Enable mute toggle | When enabled, displays a button to toggle video sound                                  |
| Enable loop        | When enabled, the video will continuously repeat                                       |

#### Newsletter

Adds a newsletter subscription form within a tab. Limited to 1 per section.

| Setting         | Description                                                                            |
| --------------- | -------------------------------------------------------------------------------------- |
| Tab             | The tab name this block should appear in (must match a tab name from section settings) |
| Content         | Text content displayed above the email input                                           |
| Button label    | Text for the subscribe button                                                          |
| Disclaimer      | Optional text displayed below the form (privacy policy, etc.)                          |
| Success message | Message shown after successful subscription                                            |
| Color button    | Color scheme for the subscribe button                                                  |

#### Accordion

Creates an expandable/collapsible content section within a tab.

| Setting      | Description                                                                            |
| ------------ | -------------------------------------------------------------------------------------- |
| Tab          | The tab name this block should appear in (must match a tab name from section settings) |
| Heading      | Title for the accordion                                                                |
| Content      | Rich text content revealed when accordion is expanded                                  |
| Icon         | Optional icon displayed before the heading                                             |
| Color scheme | Color styling for the accordion                                                        |
| Enable open  | When enabled, accordion is expanded by default                                         |

#### Discount

Displays a discount code with a copy button within a tab.

| Setting      | Description                                                                            |
| ------------ | -------------------------------------------------------------------------------------- |
| Tab          | The tab name this block should appear in (must match a tab name from section settings) |
| Content      | Text content displayed above the discount code                                         |
| Code         | The discount code customers can copy                                                   |
| Color button | Color scheme for the copy button                                                       |
