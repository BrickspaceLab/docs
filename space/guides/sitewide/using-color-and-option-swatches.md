# Using color and option swatches

## Space: Using color and option swatches

## Summary <a href="#h_c9f7a3a18b" id="h_c9f7a3a18b"></a>

***

Swatches are used to make variant selections easier and more intuitive for customers when they are selecting an option with color. Swatches appear throughout your theme in various places and can be used with custom images or hex code colors.

[![](https://downloads.intercomcdn.com/i/o/1200188733/46c1428813b9c2fbdcc65d4e/CleanShot+2024-10-01+at+11_20_26%402x.png?expires=1744834500\&signature=3a4c32e16ea4bc7136d621f14ecba6992325b88c6728bf3605723b4110f925fe\&req=dSInFsh2lYZcWvMW1HO4zbdRtJu5ajOk%2FRbXQPw4Q4f%2FT2%2FfkrqyTVf1xevP%0AHTDRfD%2Ft9dFEyg1ZEv8%3D%0A)](https://downloads.intercomcdn.com/i/o/1200188733/46c1428813b9c2fbdcc65d4e/CleanShot+2024-10-01+at+11_20_26%402x.png?expires=1744834500\&signature=3a4c32e16ea4bc7136d621f14ecba6992325b88c6728bf3605723b4110f925fe\&req=dSInFsh2lYZcWvMW1HO4zbdRtJu5ajOk%2FRbXQPw4Q4f%2FT2%2FfkrqyTVf1xevP%0AHTDRfD%2Ft9dFEyg1ZEv8%3D%0A)

## Using swatch options <a href="#h_7b48b3b2e7" id="h_7b48b3b2e7"></a>

***

In order to display swatches on a product page or within a product card we can use metafield connected variant options. This might sound complicated but it's super easy to setup and works great out of the box.

1. Find a product you want to update.
2. Update the "Category" field to match your product.
3. Add a new option like "Color" or "Material".
4. Ensure the option is connected to a metafield.

From here you'll be able to change the hexcode or image of each swatch by clicking into it.

[![](https://downloads.intercomcdn.com/i/o/fnubgeik/1227086630/3648d8b932cd0f26926fb046b038/CleanShot-2B2024-09-30-2Bat-2B15_59_06.png?expires=1744834500\&signature=c1be0fefb7fdf5b4f81680f6472d554f14d3de324a0a408d3dd2f99513f21ed0\&req=dSIlEcl2m4dcWfMW1HO4zXUc5IuEUeMHdZOdHKH3i3ww%2BPEJy1XEEWnx4Tf3%0A3rjRKnpvjXd0aPODbRE%3D%0A)](https://downloads.intercomcdn.com/i/o/fnubgeik/1227086630/3648d8b932cd0f26926fb046b038/CleanShot-2B2024-09-30-2Bat-2B15_59_06.png?expires=1744834500\&signature=c1be0fefb7fdf5b4f81680f6472d554f14d3de324a0a408d3dd2f99513f21ed0\&req=dSIlEcl2m4dcWfMW1HO4zXUc5IuEUeMHdZOdHKH3i3ww%2BPEJy1XEEWnx4Tf3%0A3rjRKnpvjXd0aPODbRE%3D%0A)

## Using swatch filtering <a href="#h_cd5e5bf18a" id="h_cd5e5bf18a"></a>

***

Your collection page filtering can be customized from the [Shopify Search and Discovery app](https://apps.shopify.com/search-and-discovery). Using this app you can add new filters and customize how they appear on your theme.

### Add swatch filter from metafield <a href="#h_f6538f3037" id="h_f6538f3037"></a>

Shopify has recently made a number of improvements to metafields and how they work with swatches. This is great news for us because now swatches are much easier to manage and update.

Create metaobject for your swatch

1. Navigate to your Shopify settings page then click "Custom data".
2. Scroll down to Metaobject definitions then click "Add definition".
3. Add a name and description to your metaobject.
   * You can use any name or description. E.g. "Swatch"
4. Add three fields to your metaobject.
   * Label, color and image.
   * Label should be a required field using "Single line text" - Make sure to select "List of values" after clicking single line text.
   * Color is not required and uses "Color".
   * Image is not required and uses "File" with "Accepts specific file types - Images" selected.

[![](https://downloads.intercomcdn.com/i/o/1200182812/a254c3b77387f764219206fd/CleanShot%2B2024-09-30%2Bat%2B15_02_09.png?expires=1744834500\&signature=123fb765f098a71d41d9d54c7319c206364df50e0903aa1deb49d80dbca271a9\&req=dSInFsh2n4leW%2FMW1HO4ze%2F2GDPxO0pnNjjcRLDOb1HN0mDz4QqQPyX80S8G%0AsAmdLFQnVFqJZhfbQeg%3D%0A)](https://downloads.intercomcdn.com/i/o/1200182812/a254c3b77387f764219206fd/CleanShot%2B2024-09-30%2Bat%2B15_02_09.png?expires=1744834500\&signature=123fb765f098a71d41d9d54c7319c206364df50e0903aa1deb49d80dbca271a9\&req=dSInFsh2n4leW%2FMW1HO4ze%2F2GDPxO0pnNjjcRLDOb1HN0mDz4QqQPyX80S8G%0AsAmdLFQnVFqJZhfbQeg%3D%0A)

Create metafield to link to metaobject

We now have to assign values so data is populated for our new metafields.

1. Navigate to your Shopify settings page then click "Custom data".
2. Find and click "Product".
3. Click "Add definition".
4. Add a name and description to your new metafield.
   * You can use any name or description. E.g. "Swatch"
5. Click "Select type" then pick "Metaobject". Make sure to select "List of values" after clicking Metaobject.
6. In the reference field enter the Metaobject you have just created.

[![](https://downloads.intercomcdn.com/i/o/1200182817/fc0daddf8eb1bb99da8b0160/CleanShot%2B2024-09-30%2Bat%2B15_08_08.png?expires=1744834500\&signature=8ce46fe5511fd46f3a02bad85ea9344a4c181c76e989e4239ef3bfdbe3239129\&req=dSInFsh2n4leXvMW1HO4zY60SKpBruWLTKXDXx9IBnqTQoIFTCitgFl26YZu%0Agh%2FlNUvASvGx4NbTUxc%3D%0A)](https://downloads.intercomcdn.com/i/o/1200182817/fc0daddf8eb1bb99da8b0160/CleanShot%2B2024-09-30%2Bat%2B15_08_08.png?expires=1744834500\&signature=8ce46fe5511fd46f3a02bad85ea9344a4c181c76e989e4239ef3bfdbe3239129\&req=dSInFsh2n4leXvMW1HO4zY60SKpBruWLTKXDXx9IBnqTQoIFTCitgFl26YZu%0Agh%2FlNUvASvGx4NbTUxc%3D%0A)

Assign values to each product

From here you can click into each product and make sure the new metafield is updated to correspond to the relevant options.

1. Find a product you want to update.
2. Scroll down to "Product metafields" and add all the colors you'd like to highlight for this product.

[![](https://downloads.intercomcdn.com/i/o/1200182814/8876405a63051412b846fcaf/CleanShot%2B2024-09-30%2Bat%2B15_11_13.png?expires=1744834500\&signature=e033593039a96c65e8e9302a536a8e0173dc789b966a0bd8800162a81c52fa21\&req=dSInFsh2n4leXfMW1HO4zf5M%2BiWITpWdTOuV1QZBV5BgplrUVA81CMnhkmdB%0ATH1upvnt8nShbcD%2FUng%3D%0A)](https://downloads.intercomcdn.com/i/o/1200182814/8876405a63051412b846fcaf/CleanShot%2B2024-09-30%2Bat%2B15_11_13.png?expires=1744834500\&signature=e033593039a96c65e8e9302a536a8e0173dc789b966a0bd8800162a81c52fa21\&req=dSInFsh2n4leXfMW1HO4zf5M%2BiWITpWdTOuV1QZBV5BgplrUVA81CMnhkmdB%0ATH1upvnt8nShbcD%2FUng%3D%0A)

Connect to filter

Once all your data is place the only thing left is to connect this to your filters.

1. Open the Search and discovery app.
2. Navigate to filters and click "Add filter".
3. Click "Select source" then look for the new product metafield you just created
4. Add a label .
   * You can use any name or description. E.g. "Color" or "Material"
5. Click save.

Caveats of metafield filtering

If you use metafield swatch filtering you'll have to ensure you update your metafields for all products that you want to appear on this filter - this will NOT happen automatically even if category metafields and variant options are displaying swatches.

### Add swatch filter from 'color' option <a href="#h_8b81e9e28e" id="h_8b81e9e28e"></a>

You can add filters using color product options. This is a easy way to add filters but will require swatch files to be uploaded in a specific format. Swatches will only appear using this approach when the product option matches "color" - or a translation of color.

Add filter using Search and discovery

1. Open the Search and discovery app.
2. Navigate to filters and click "Add filter".
3. Click "Select source" then look for the product option "Color".
   * This is the same approach you would take if you wanted to filter by any other product option like size.
4. Add a label.
   * You can use any name or description. E.g. "Color"
5. Click save.

Upload missing swatch files

You may notice that not all of your color filters are appearing with swatches. If this is the case you may have to upload custom swatch files.

Swatches will only appear automatically if the color name matches a default [CSS color](https://intercom.help/brickspacelab/en/articles/9939903-paper-using-color-and-option-swatches).

1. Identify all swatches that are missing
2. Upload a 64x64 jpg file for each swatch you want to replace.
   * Swatches must be named all lowercase and prepended with “swatch-”. For example, if your color variant is “Electric blue” you would name your file “swatch-electric-blue.jpg”

[![](https://downloads.intercomcdn.com/i/o/1200182818/4135f90586ea6d0221a62bc0/CleanShot%2B2024-09-30%2Bat%2B15_44_05-402x.png?expires=1744834500\&signature=bc57b9ce1f6a131e244a9391e79c9294b6817c069732ab4b9232abe3d30cb52a\&req=dSInFsh2n4leUfMW1HO4zZqWLd%2BCmXoA3%2BHyfsuKzmHPygruZfaKbaV2gdvu%0AueruJrqpG5E5GI97qyQ%3D%0A)](https://downloads.intercomcdn.com/i/o/1200182818/4135f90586ea6d0221a62bc0/CleanShot%2B2024-09-30%2Bat%2B15_44_05-402x.png?expires=1744834500\&signature=bc57b9ce1f6a131e244a9391e79c9294b6817c069732ab4b9232abe3d30cb52a\&req=dSInFsh2n4leUfMW1HO4zZqWLd%2BCmXoA3%2BHyfsuKzmHPygruZfaKbaV2gdvu%0AueruJrqpG5E5GI97qyQ%3D%0A)<br>
