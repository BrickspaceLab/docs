# Build grid layouts

Slab offers two main layout blocks for arranging content: **Default grid** and **Flex grid**. Each suits different layout needs. This guide covers both blocks and when to use them.



## Default grid

The Default grid block creates a responsive grid of equal-width columns. Use it for product grids, image galleries, card layouts, or any content that benefits from a uniform grid structure.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section=template--18647337730099__section_eLU93j&#x26;block=template--18647337730099__section_eLU93j__layout_grid_PnDfC3(Theme 3).png" alt=""><figcaption></figcaption></figure>

**When to use Default grid**

* When you want to display a uniform grid where each row and column are the same width and height



## Flex grid

The Flex grid block arranges child blocks in a row or column with flexible alignment and spacing. Use it for side-by-side layouts, stacked sections, hero layouts, or any content that needs flexible widths and alignment.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section=template--18647337730099__section_eLU93j&#x26;block=template--18647337730099__section_eLU93j__layout_grid_PnDfC3(Theme 3) (1).png" alt=""><figcaption></figcaption></figure>

**When to use Flex grid**

* Create row or column layouts with configurable alignment
* Use horizontal direction for side-by-side content
* Use vertical direction for stacked content
* Control item widths with percentage-based or fill options



## Common layouts

Using the Flex grid you can create many unique layouts. Here are a few examples to help illustrate how to achieve different grid configurations.&#x20;



#### **Grid with sticky position**

Use this layout for content on one side that stays visible while scrolling.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_section=template--18647337730099__section_eLU93j&#x26;category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FHeader%3Ftheme_id%3D141866205235%26first_setting_id%3Dheade.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Vertical alignment** to **Stretch**
* On a child **Flex item** toggle **Enable sticky layout**
* Set **Sticky position** to **Top**



#### **Grid with centered three columns**

Use this layout for a navigation or header bar.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FHeader%3Ftheme_id%3D141866205235%26first_setting_id%3Dheader_position&#x26;section=template--18647337730099__sect.png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** disable **Enable block wrap**
* On the first **Flex item** toggle **Enable width fill** — this will force the block to fill available space in the row
* On the second **Flex item** set a specific width like 20%
* On the third **Flex item** toggle **Enable width fill**
* With this layout the first and last columns will automatically fill the remaining 80% of the row equally



#### **Grid where two columns are pushed to either edge**

Use this layout for editorial-style layouts.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FHeader%3Ftheme_id%3D141866205235%26first_setting_id%3Dheader_position&#x26;section=template--18647337730099__ (1).png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Horizontal alignment** to **Between**
* Add two child **Flex item** blocks
* The child blocks will now be pushed to the edges of the container



#### **Grid with content aligned to bottom**

Use this layout for editorial-style layouts.

<figure><img src="../../.gitbook/assets/admin.shopify.com_store_slabdemostore4_themes_141866205235_editor_category=gid%3A%2F%2Fshopify%2FOnlineStoreThemeSettingsCategory%2FHeader%3Ftheme_id%3D141866205235%26first_setting_id%3Dheader_position&#x26;section=template--18647337730099__ (2).png" alt=""><figcaption></figcaption></figure>

* Use a **Flex grid** block
* On the parent **Flex grid** set **Vertical alignment** to **End**
* All child blocks will now be pushed to the bottom of the container

