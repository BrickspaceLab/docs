---
index: 4
---

# Reuse content

Use **Render section** to show the same group of blocks in more than one place. Use **Metaobjects** to repeat a layout for a list of FAQ entries.

## Reuse a section

1. Create an alternate page template and add exactly one **Render source** section.
2. Add the blocks you want to reuse inside **Render source**.
3. Add **Render section** where the content should appear.
4. Select a **Source page** and enter the alternate template's **Template suffix**. For example, enter `size-guide` for `page.size-guide.json`.

Edit the blocks in **Render source** to update the content wherever it is used.

## Display a list of FAQ entries

1. Create a Shopify metaobject definition with the type `faq`, then add your entries.
2. Add **Metaobjects** in the theme editor. In **Metaobject list**, select the entries or connect a list of references using a dynamic source.
3. Add blocks inside **Content** and connect their settings to fields from the FAQ entry, such as its question and answer.

The layout repeats for each selected entry.
