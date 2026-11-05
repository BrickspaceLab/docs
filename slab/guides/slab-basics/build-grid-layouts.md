---
index: 0
---

# Grid layouts

Slab offers two main layout blocks for arranging content: **Default grid** and **Flex grid**. Each suits different layout needs. This guide covers both blocks and when to use them.

## Default grid

The Default grid block creates a responsive grid of equal-width columns. Use it for product grids, image galleries, card layouts, or any content that benefits from a uniform grid structure.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section%3Dtemplate--18647337730099__section_eLU93j%26block%3Dtemplate--18647337730099__section_eLU93j__layout_grid_PnDfC3%28Theme%203%29.png" alt=""><figcaption></figcaption></figure>

**When to use Default grid**

* When you want to display a uniform grid where each row and column are the same width and height

## Flex grid

The Flex grid block arranges child blocks in a row or column with flexible alignment and spacing. Use it for side-by-side layouts, stacked sections, hero layouts, or any content that needs flexible widths and alignment.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section%3Dtemplate--18647337730099__section_eLU93j%26block%3Dtemplate--18647337730099__section_eLU93j__layout_grid_PnDfC3%28Theme%203%29%20%281%29.png" alt=""><figcaption></figcaption></figure>

**When to use Flex grid**

* Create row or column layouts with configurable alignment
* Use horizontal direction for side-by-side content
* Use vertical direction for stacked content
* Control item widths with percentage-based or fill options

## Common layouts

Using the Flex grid you can create many unique layouts. Here are a few examples to help illustrate how to achieve different grid configurations.

#### **Grid with sticky position**

Use this layout for content on one side that stays visible while scrolling.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section%3Dtemplate--18647337730099__section_eLU93j%26category%3Dgid%253A%252F%252Fshopify%252FOnlineStoreThemeSettingsCategory%252FHeader%253Ftheme_id%253D141866205235%2526first_setting_id%253Dheade.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Vertical alignment** to **Stretch**
* On a child **Flex item** turn on **Show advanced settings**, then enable **Enable sticky layout**
* Set **Sticky position** to **Top**

#### **Grid with centered three columns**

Use this layout for a navigation or header bar.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category%3Dgid%253A%252F%252Fshopify%252FOnlineStoreThemeSettingsCategory%252FHeader%253Ftheme_id%253D141866205235%2526first_setting_id%253Dheader_position%26section%3Dtemplate--18647337730099__sect%20%281%29.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** disable **Enable block wrap**
* On the first **Flex item** set **Width** to **Fill** so it grows and uses free space in the row
* On the second **Flex item** set **Width** to **Custom** and set a specific width such as 20% (mobile and desktop as needed)
* On the third **Flex item** set **Width** to **Fill**
* With this layout the first and last columns will automatically fill the remaining 80% of the row equally

#### **Grid where two columns are pushed to either edge**

Use this layout for editorial-style layouts.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category%3Dgid%253A%252F%252Fshopify%252FOnlineStoreThemeSettingsCategory%252FHeader%253Ftheme_id%253D141866205235%2526first_setting_id%253Dheader_position%26section%3Dtemplate--18647337730099__%20%281%29%20%281%29.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Horizontal alignment** to **Between**
* Add two child **Flex item** blocks
* The child blocks will now be pushed to the edges of the container

#### **Grid with content aligned to bottom**

Use this layout for editorial-style layouts.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category%3Dgid%253A%252F%252Fshopify%252FOnlineStoreThemeSettingsCategory%252FHeader%253Ftheme_id%253D141866205235%2526first_setting_id%253Dheader_position%26section%3Dtemplate--18647337730099__%20%282%29%20%281%29.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Vertical alignment** to **End**
* All child blocks will now be pushed to the bottom of the container
