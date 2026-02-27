# Avatar image

## Block limitations

This is a private block and can only be used within specific parent blocks. It is designed to work exclusively within the [Avatars](avatars.md) block.

## Overview

A styled avatar component that creates a circular container for content blocks, primarily designed for displaying profile images or avatars. The component features a circular border and supports responsive visibility options.

## Common use cases

- Best used for profile pictures, user avatars, or circular image elements
- Consider the context where avatars will be displayed when selecting size
- Use the visibility options to create different avatar arrangements on mobile vs desktop

## Compatible blocks

The following blocks can be nested within this block:

- [Image](image.md)

## Block settings

| Setting | Description | Options |
|---------|-------------|---------|
| Size | Size of the avatar | Small (default), Medium, Large |
| Border color | Controls the border color | Body, Subtle, Strong, Primary, Secondary, Tertiary, None. Default: Body |
| Visibility | Controls when the block is visible | All (default), Mobile only, Desktop only |

