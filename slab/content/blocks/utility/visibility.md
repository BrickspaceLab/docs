# Visibility

## Overview

A container block that controls whether nested content is rendered at all (not merely hidden with CSS) based on device, customer, cart, visit session, URL path, and optional viewport rules. Approved-customer logic follows **Theme settings > Account** (matching tags and B2B handling). URL rules are evaluated in Liquid on the server to reduce flashing content. Session-based rules use browser storage and run in the customer’s browser.

## Common use cases

* Show or hide content based on customer login status
* Display content only to approved or B2B customers
* Control visibility based on cart state (empty or not empty)
* Target first-time or returning visitors, or cap how many visits show a message
* Show or hide blocks on specific paths (for example `/collections/*`) or everywhere except chosen paths
* Reveal content when another element (identified by a CSS class) enters or leaves the viewport
* Prefer this over `display: none` when content should not appear in the DOM for some audiences

## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks

## Block settings

### General

| Setting                 | Description                                                                 | Options                                                                                       |
| ----------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Show advanced settings  | Reveals load or scroll animation settings (mutually exclusive)              | Checkbox (default: false)                                                                      |

### Display

| Setting              | Description                                                                 | Options                                                                                                                                                                                                                         |
| -------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device visibility    | Limits visibility to mobile or desktop                                      | <p>• All (default)<br>• Mobile only<br>• Desktop only</p>                                                                                                                                                                        |
| Customer visibility  | Limits visibility by authentication and approval                            | <p>• All (default)<br>• Logged out<br>• Any account<br>• Approved account<br>• B2B account</p>                                                                                                                                   |
| Cart visibility      | Limits visibility by cart item count                                        | <p>• All (default)<br>• Empty<br>• Not empty</p>                                                                                                                                                                                 |
| Session              | Limits visibility by how many store visits the browser has recorded         | <p>• Always show (default)<br>• First visit only<br>• Returning visitors only<br>• Show up to session count<br>• Hide after session count</p>                                                                                    |
| Session count        | Visit count used when session is **Show up to session count** or **Hide after session count** | Number (default: 5)<br><br>Visible when session uses a count-based mode                                                                                                                                                          |
| URL                  | Whether URL patterns are ignored, used to show only on matches, or hide on matches | <p>• Show on all pages (default)<br>• Show only on matching pages<br>• Hide on matching pages</p>                                                                                                                              |
| URL patterns         | Comma-separated paths; `*` is a wildcard (for example `/collections/*`)    | Textarea<br><br>Visible when URL is not **Show on all pages**                                                                                                                                                                  |
| Block                | Whether nested content is always shown or tied to another element’s visibility | <p>• Always show (default)<br>• Show when block enters viewport<br>• Show when block not in viewport</p>                                                                                                                         |
| Block class          | CSS class of the element to observe (for example `buy-button`)              | Text<br><br>Visible when block visibility uses a viewport mode                                                                                                                                                                 |
| Toggle animation     | How content appears or disappears when Alpine.js toggles visibility         | <p>• None (default)<br>• Fade<br>• Fade up<br>• Fade down</p><br><p>Applies when cart, session, URL rules, or block visibility use dynamic show or hide.</p>                                                                      |
| Load animation       | Animation when the block first loads                                        | <p>• None (default)<br>• Fade<br>• Fade up<br>• Offset fade<br>• Offset fade up</p><br><br>Visible when **Show advanced settings** is on and **Scroll animation** is **None**                                                    |
| Scroll animation     | Animation tied to scroll position                                           | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p><br><br>Visible when **Show advanced settings** is on and **Load animation** is **None**                                |
