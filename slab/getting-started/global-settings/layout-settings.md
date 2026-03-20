# Layout

Layout settings in Slab control storefront spacing and section-level scroll snapping behavior. Use **Theme settings > Layout**.

## Set up layout settings

Use this order so global layout decisions are in place before section-level tuning.

{% stepper %}
{% step %}
#### Set global layout spacing

1. Open **Theme settings > Layout**.
2. Set **Horizontal margin** to control overall storefront width.
3. Set **Gap size** to control default spacing rhythm between elements.
{% endstep %}

{% step %}
#### Enable vertical scroll snapping globally

1. In **Theme settings > Layout**, enable **Enable scroll snapping**.
2. Save your changes.

After this is enabled, supported sections can use **Scroll snap alignment**.
{% endstep %}

{% step %}
#### Configure section scroll snap alignment

1. Open each section you want to participate in vertical snapping.
2. Set **Scroll snap alignment** for that section.
3. Leave sections on **None** when they should scroll normally.
4. Preview full-page scrolling on desktop and mobile before publishing.
{% endstep %}
{% endstepper %}

## Suggested defaults for most stores

* Start with **Horizontal margin** set to the standard option, then widen or narrow based on content density.
* Keep **Gap size** near default unless your brand style needs tighter or looser spacing.
* Enable scroll snapping only on templates where section-by-section browsing improves storytelling or conversion.
* Use section-level alignment selectively, not on every section, to avoid a rigid scroll experience.

## Layout settings reference

| Setting                | What it controls                                      | Options or range             | Default  |
| ---------------------- | ----------------------------------------------------- | ---------------------------- | -------- |
| Horizontal margin      | Controls how wide the storefront content area is.     | Narrow, Standard, Wide, Full | Standard |
| Gap size               | Controls default spacing rhythm in supported layouts. | 1 to 20 px                   | 8 px     |
| Enable scroll snapping | Enables section snapping while customers scroll.      | Enabled, Disabled            | Disabled |
