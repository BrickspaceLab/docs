# Account drawer

### Section overview

This section is responsible for rendering and managing the account drawer functionality which includes login forms, customer account information, orders, addresses, and customizable content blocks.

#### Common use cases

* Providing customers with access to their account information, orders, and addresses
* Creating personalized login/signup experiences for different user states
* Adding custom content and announcements visible only to specific customer segments
* Integrating B2B functionality with company locations and permissions

#### Usage tips

* Customize the color schemes to match your store's branding
* Use content blocks with different visibility settings to create personalized experiences
* Consider mobile responsiveness as the account drawer adapts differently on mobile (bottom drawer) vs desktop (right drawer)
* Avoid adding too many content blocks as this can make the account drawer feel cluttered

### Section settings

| Setting                   | Description                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------- |
| Top bar color scheme      | Sets the background and text color for the top bar of the account drawer           |
| Top bar border color      | Controls the border color for the top section of the account drawer                |
| Main section color scheme | Sets the background and text color for the main content area of the account drawer |
| Main section border color | Controls the border color for the main content area of the account drawer          |

### Theme settings

{% hint style="info" %}
**Version requirement:** Custom account and login URLs are available in Keystone theme version 2.0.1 or later.
{% endhint %}

#### Custom account URL

You can specify a custom URL for account pages in **Theme Settings > Account**. This is helpful if you want to create a custom page with a legacy signup form and force users to go to that page when accessing their account.

**Setup:**

1. Navigate to **Theme Settings** (gear icon in the theme editor)
2. Open the **Account** section
3. Set **Account icon behavior** to **"Redirect"** (this setting only appears when redirect is selected)
4. Enter your custom URL in the **Custom account URL** field

**Note:** The Custom account URL setting only appears when "Account icon behavior" is set to "Redirect".

#### Custom login URL

You can specify a custom URL for login and signup pages in **Theme Settings > Account**. This is helpful if you want to create a custom page with the legacy signup form and force users to go to that page when signing up.

**Setup:**

1. Navigate to **Theme Settings** (gear icon in the theme editor)
2. Open the **Account** section
3. Enter your custom URL in the **Custom login URL** field

**Important:** This URL will override the default login and signup forms throughout the theme, including in the header, footer, menu, product pages, blog items, and product grids.

### Block settings

#### Announcement

This block allows you to add a prominent announcement message at the top of the account drawer.

Block limit: 1

| Setting              | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| Content              | The text content of the announcement message               |
| Color scheme         | The background and text color for the announcement message |
| Horizontal alignment | Controls the alignment of the text (left, center, right)   |

#### Content

This block adds customizable content sections to the account drawer that can be configured to display based on customer login status.

Block limit: 15

| Setting              | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| Visibility           | Controls when this content appears (always, logged out, logged in not approved, logged in and approved) |
| Heading              | The title text for the content block                                                                    |
| Content              | The main text content for the block                                                                     |
| Button label         | Text to display on the block's call-to-action button                                                    |
| URL                  | The destination link for the button                                                                     |
| Image                | The main image to display in the content block                                                          |
| Image background     | A background image to display behind the content                                                        |
| Video                | A video to display in the content block                                                                 |
| Enable autoplay      | Controls whether the video plays automatically                                                          |
| Enable mute toggle   | Adds a button to toggle video sound on/off                                                              |
| Enable loop          | Controls whether the video repeats after finishing                                                      |
| Minimum height       | Sets the minimum height for the content block in pixels                                                 |
| Enable padding       | Adds padding around the content block when enabled                                                      |
| Color scheme         | Sets the background and text color for the content block                                                |
| Text color           | Controls whether to use default, light, or dark text regardless of background                           |
| Border color         | Sets the border style around the content block                                                          |
| Button color         | Controls the appearance and style of the button                                                         |
| Enable gradient      | Adds a gradient effect to the background when enabled                                                   |
| Vertical alignment   | Controls the vertical positioning of content (top, middle, bottom)                                      |
| Horizontal alignment | Controls the horizontal positioning of content (left, center, justify, right)                           |
| Text position        | Controls whether text appears above or below the image/video                                            |
