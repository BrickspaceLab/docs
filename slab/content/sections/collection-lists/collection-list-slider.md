# Collection list: slider

### Section overview

Collection list: slider is a `section.liquid` preset for horizontally scrolling collection cards. It uses `layout__slider` and `_slider-collections` to render a swipeable or arrow-controlled collection list.

#### Common use cases

* Featured collections carousels on the homepage.
* Mobile-friendly collection browsing sections.
* Promotional collection showcases with horizontal navigation.
* Compact collection navigation above product content.

#### Usage tips

* Use slider controls (arrows and indicators) appropriate for your audience and device mix.
* Start with default card widths, then adjust desktop/mobile widths gradually.
* Keep collection card content simple for better slide scannability.
* Verify control placement and card widths on small screens.

### Section settings

This preset inherits shared `section.liquid` settings (spacing, media, colors, borders, alignment, and visibility).

### Block settings

The slider preset uses this structure:

* `layout__slider` (preset container)
  * Controls arrows, indicators, control placement, and transition behavior.
* `_slider-collections` (data source + slide sizing)
  * Uses `collection_list` and width settings for desktop/mobile slide sizing.
* `g__collection-card` (inside each slide)
  * Renders collection visuals and title content.

Key preset characteristics from source:

* Slider controls are enabled by default in the preset.
* Mobile and desktop slide widths are configurable.
* Collection cards are rendered through the slider collection data source.
