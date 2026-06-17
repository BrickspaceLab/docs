# Changelog

{% updates format="full" %}
{% update date="2026-06-17" tags="0.3.0" %}
## 0.3.2

* This release improves admin reliability and cleanup, with fixes for missing images, archived-item visibility, and dark mode polish in the table of contents.

<details>

<summary>Notes</summary>

* Version information in the "..." menu was updated for 0.3.2.

</details>

<details>

<summary>Features and improvements</summary>

* Archived resources are now hidden from the admin list by default, with a way to switch between active and archived items.

</details>

<details>

<summary>Bugs</summary>

* Missing image thumbnails in admin were fixed.
* The table of contents now shows a solid hover background in dark mode.

</details>
{% endupdate %}

{% update date="2026-06-17" tags="0.3.0" %}
## 0.3.1

* Small fixes improve mobile polish, search accuracy, page speed, and release-version details.

<details>

<summary>Notes</summary>

* Hotfix release focused on a handful of targeted cleanup and reliability fixes.

</details>

<details>

<summary>Features and improvements</summary>

* Faster homepage image loading.
* More accurate section search that only matches exact tagged locations.
* Better spacing between sticky buttons on mobile.

</details>

<details>

<summary>Bugs</summary>

* Version information in the "..." menu was updated for 0.3.1.
* Mobile border radius rendering was fixed.

</details>
{% endupdate %}

{% update date="2026-06-15" tags="0.3.0" %}
## 0.3.0

* Smarter section indexing, and refreshed admin controls make catalog content easier to organize and discover.
* Search and filtering got a cleaner, more focused experience with better result organization and less UI clutter.
* Brand content handling is more polished across capture, screenshots, submissions, metadata, and sharing surfaces.

<details>

<summary>Notes</summary>

* Changelog link from the “…” menu.
* `llms.txt` support for better crawling by AI agents.
* Better access limits and tier messaging for brand content, including gallery/search/bookmark limits and claim-handle messaging.
* Homepage design and slider presentation were refreshed.
* The “Reshoot” label now says “Refresh” in user-facing copy.

</details>

<details>

<summary>Features and improvements</summary>

* SEO landing pages for filtered brand lists, including shareable filter URLs, sitemap entries, and page titles/H1s.
* Automatic section indexing for brand images, with clearer section labels and better section matching.
* Admin section-indexing controls with a simpler “Index sections” action, table of contents, and drag-and-drop updates.
* Search and filter experience updates, including a redesigned dropdown, clearer result sections, and removed upsell/info elements.
* Brand image capture now starts from the first collection linked on the homepage, then uses the first product in that collection.
* Draft brand screenshots now generate more reliably.
* Carousel navigation works on the brand preset page, and homepage carousel clicks behave normally in Firefox.
* Google account emails are included with preset and brand submissions.
* Loading state for GitHub connection stays inside the button, reducing layout shifts.
* Brand tagline and description formatting is standardized, and size labels now read Small/Medium/Large inventory.
* Typography tags now use the shared styles list instead of a separate typography-specific set.
* OG image templates now apply across all resource detail pages and support multiple images.
* The catalog cards’ gradient is smaller, making the image and text easier to see together.

</details>

<details>

<summary>Bugs</summary>

* Clicking pause on a card now stops scrolling in place.
* Bulk brand upload now reports asset failures correctly and keeps later brands in the run processing.
* Stripe webhook delivery for the account was fixed.
* Delete actions for themes, presets, and brands from admin drawers and quick actions.

</details>
{% endupdate %}
{% endupdates %}
