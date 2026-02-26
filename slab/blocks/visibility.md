# Visibility


## Overview

A container block that controls content visibility based on screen size and customer status. Conditionally renders child blocks based on customer authentication state and screen size requirements.


## Common use cases

* Show or hide content based on customer login status
* Display content only to approved or B2B customers
* Control visibility based on cart state (empty or not empty)
* Control device-specific visibility for mobile or desktop only


## Compatible blocks

The following blocks can be nested within this block:

* All theme blocks
* App blocks


## Block settings

### Display

| Setting | Description | Options |
|---------|-------------|----------|
| Device | Controls when the block is visible based on screen size | <p>• Always show (default)<br>• Show on mobile<br>• Show on desktop</p> |
| Customer | Controls when the block is visible based on customer status | <p>• Show to all visitors (default)<br>• Show to logged out visitors<br>• Show to any account<br>• Show to approved accounts<br>• Show to B2B accounts</p> |
| Cart | Controls when the block is visible based on cart state | <p>• Always show (default)<br>• Show when cart is empty<br>• Show when cart has items</p> |
| Scroll animation | Controls how the block appears when scrolled into view. | <p>• None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom</p> |
