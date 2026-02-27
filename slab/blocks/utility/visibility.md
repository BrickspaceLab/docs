# Visibility


## Overview

A container block that controls content visibility based on screen size, customer status, and cart state. Conditionally renders child blocks based on customer authentication state, approved customer status, and screen size requirements. Uses liquid conditionals for complete block hiding rather than CSS display properties, making it ideal for sensitive content that needs to be completely hidden from certain user groups.


## Common use cases

- Show or hide content based on customer login status
- Display content only to approved or B2B customers
- Control visibility based on cart state (empty or not empty)
- Use for content that needs to be completely hidden from certain user groups
- Prefer this over CSS display:none for sensitive content
- Control device-specific visibility for mobile or desktop only


## Compatible blocks

The following blocks can be nested within this block:

- All theme blocks
- App blocks


## Block settings

### Display

| Setting | Description | Options |
|---------|-------------|---------|
| Device visibility | Controls when the block is visible based on screen size | • All (default)<br>• Mobile only<br>• Desktop only |
| Customer visibility | Controls when the block is visible based on customer status | • All (default)<br>• Logged out<br>• Any account<br>• Approved account<br>• B2B account |
| Cart visibility | Controls when the block is visible based on cart state | • All (default)<br>• Empty<br>• Not empty |
| Scroll animation | Animation effect when the block scrolls into view | • None (default)<br>• Fade<br>• Slide up<br>• Slide down<br>• Slide left<br>• Slide right<br>• Zoom |
