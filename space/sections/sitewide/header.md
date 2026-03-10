# Header

### Section overview

The theme header section is responsible for rendering the site header, including the logo, navigation, cart, and other interactive elements that appear at the top of every page.

#### Common use cases

* Primary navigation for the entire store
* Displaying brand identity through logo and color scheme
* Providing quick access to cart, search, and account functionality
* Supporting dropdown menus with additional content blocks

#### Usage tips

* Choose the appropriate layout (left or center aligned) based on your brand's aesthetic
* Configure color schemes that complement your site's design, especially when using transparent headers over banners
* Test dropdown navigation on mobile to ensure it's easily accessible
* Consider using both default and overlay logos to improve visibility when the header overlaps with image banners

### Section settings

| Setting               | Description                                                                         |
| --------------------- | ----------------------------------------------------------------------------------- |
| Logo default          | The primary logo image displayed in the header                                      |
| Logo overlay          | Alternative logo displayed when the header overlaps with a banner                   |
| Desktop logo height   | Height of the logo in pixels on desktop devices                                     |
| Mobile logo height    | Height of the logo in pixels on mobile devices                                      |
| Desktop layout        | Alignment of header elements (left or center)                                       |
| Default color scheme  | Color scheme applied to the header in its default state                             |
| Overlay color scheme  | Color scheme applied when the header overlaps with a banner                         |
| Default color border  | Border color in the header's default state                                          |
| Overlay color border  | Border color when the header overlaps with a banner                                 |
| Cart button           | Display options for the cart button (none, icon and text, icon, or text)            |
| Search button         | Display options for the search button (none, icon and text, icon, or text)          |
| Login button          | Display options for the login button (none, icon and text, icon, or text)           |
| Menu button           | Display options for the menu button (none, icon and text, icon, or text)            |
| Text capitalization   | Text case style for header elements (standard, uppercase, or lowercase)             |
| Font family           | Font choice for header text (standard, heading, or navigation)                      |
| Link as button        | Determines if parent links with dropdown menus behave as buttons                    |
| Show localization     | Option to display language/currency selector                                        |
| Enable margin         | Adds horizontal margin to the header container                                      |
| Dropdown color scheme | Color scheme for dropdown navigation menus                                          |
| Dropdown color border | Border color for dropdown navigation menus                                          |
| Visibility            | Controls whether the header is visible on all devices, mobile only, or desktop only |

### Block settings

#### Button

This block adds a featured call-to-action button to the header, helping highlight important pages or promotions.

Block limit: 1

| Setting      | Description                                     |
| ------------ | ----------------------------------------------- |
| Button label | Text displayed on the button                    |
| Button url   | The destination page when the button is clicked |
| Color button | Style and color scheme applied to the button    |

#### Content

This block creates rich content areas within dropdown navigation menus, allowing for promotional content, images, or videos.

Block limit: 10

| Setting                  | Description                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| Linked menu              | Menu handle to associate this content with a specific dropdown    |
| Heading                  | Title text displayed at the top of the content block              |
| Content                  | Rich text content for the block                                   |
| Button label             | Text displayed on the call-to-action button                       |
| Url                      | Destination page when the button is clicked                       |
| Image                    | Optional image to display in the content block                    |
| Show image as background | Option to use the image as a background instead of inline         |
| Video                    | Optional video to display in the content block                    |
| Enable autoplay          | Automatically plays the video when visible                        |
| Enable mute toggle       | Shows a button to toggle video sound                              |
| Enable loop              | Continuously loops the video playback                             |
| Minimum height           | Minimum height of the content block in pixels                     |
| Enable padding           | Adds internal padding to the content block                        |
| Color scheme             | Color scheme applied to the content block                         |
| Color border             | Border style for the content block                                |
| Color button             | Style and color scheme for the button                             |
| Enable gradient          | Applies a gradient effect to the background                       |
| Text position            | Places text either above or below the media content               |
| Y alignment              | Vertical alignment of content (top, middle, or bottom)            |
| X alignment              | Horizontal alignment of content (left, center, justify, or right) |
