# Set up mobile-specific images

Several Keystone sections support a separate **Mobile background image** so you can show a cropped or simplified asset on phones while keeping a wide desktop hero. Uploading a mobile image alone is not enough—you must enable the background image and understand the fallback rules.

Sections that support mobile background images include **Banner**, **Slideshow**, **Split banner**, and **Search banner**. Settings names match across these sections.

## Configure a mobile background image

{% stepper %}
{% step %}
**Open the section**

In **Customize**, select the section (for example **Banner** on your homepage).
{% endstep %}

{% step %}
**Upload desktop and mobile images**

* **Image background desktop** — wide hero for tablet and desktop (`md` breakpoint and up)
* **Mobile background image** — portrait-friendly asset (760 × 1010 px recommended)

Enable **Show image** so the background image layer renders.
{% endstep %}

{% step %}
**Save and preview mobile**

Use the theme editor device preview or a real phone. Mobile images use the `block md:hidden` layer; desktop images use `hidden md:block`.
{% endstep %}
{% endstepper %}

| Setting | Purpose |
| ------- | ------- |
| Image background desktop | Background on desktop/tablet |
| Mobile background image | Background on mobile when uploaded |
| Show image | Must be on for either image to display |
| Show video background mobile | Separate toggle if a video background should play on mobile |

## Fallback behavior

If **Mobile background image** is **empty**, Keystone **reuses the desktop image** on mobile (scaled for the smaller viewport). You do not need a separate mobile file unless you want different art direction.

If **Show image** is off, neither desktop nor mobile background images render regardless of uploads.

Video backgrounds follow their own mobile toggle (**Show video background mobile**). A mobile image does not replace video unless video is disabled or hidden on mobile.

## Verify the setup

1. Confirm **Show image** is enabled in the section settings.
2. Confirm the mobile file appears in **Mobile background image** (not only in a content block **Image** field—block images are separate from the section background).
3. Preview at mobile width. Desktop-only sections hidden via **Device visibility** will not show on phones at all.
4. Clear browser cache or use a private window if a previous hero image appears stuck.

## Common mistakes

| Mistake | Result |
| ------- | ------ |
| Image uploaded to a block, not **Mobile background image** | Background unchanged; block image may show in content area only |
| **Show image** disabled | No background on any device |
| Section set to **Show on desktop only** | Section (and its mobile image) never appears on phones |
| Only mobile image uploaded, desktop empty | Mobile shows; desktop may show placeholder SVG |

## Related reading

* [Banner section reference](../../sections/content-and-media/banner.md)
* [Device specific visibility](device-specific-visibility.md)
* [Test responsive layouts without publishing the theme](../../../general/general/test-responsive-layouts-without-publishing.md)
