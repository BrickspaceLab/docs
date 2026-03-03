# Collection list: grid

### Section overview

Collection list: grid is a `section.liquid` preset designed for displaying multiple collections in a static grid. It uses a `layout__grid` container with collection cards as the primary visual unit.

#### Common use cases

* Featured collections on the homepage.
* Collection discovery sections in landing pages.
* Category overviews with equal card emphasis.
* Navigation to top-level collection groups.

#### Usage tips

* Use consistent card image ratios for a cleaner grid.
* Tune desktop and mobile row counts for readability before changing card content.
* Keep text concise to avoid card height inconsistency.
* Combine with subtle section spacing and borders for visual separation.

### Section settings

This preset inherits shared `section.liquid` settings (spacing, media, colors, borders, alignment, and visibility).

### Block settings

The grid preset uses this structure:

* `layout__grid` (preset container)
  * Controls row layout and grid spacing.
* `g__collection-card` (inside grid items)
  * Renders each collection card from the current collection source.
* Typical card children:
  * `image` (collection image)
  * `richtext` (collection title)

Key preset characteristics from source:

* Grid rows default to multiple columns on desktop and fewer on mobile.
* Card content is designed for image + title collection presentation.
