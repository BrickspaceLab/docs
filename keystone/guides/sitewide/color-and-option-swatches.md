# Color and option swatches

Swatches help customers select variants (colors/materials) more easily. Customize them using:

* Images
* Hex color codes

#### Using Swatch Options

To show swatches on product pages/cards:

1. Update product's "Category" field
2. Add new option (Color/Material)
3. Connect option to a metafield
4. Customize each swatch:
   * Change hex code
   * Upload custom image

#### Using Swatch Filtering

Customize filters with Shopify Search & Discovery:

**Create Swatch Filter from Metafield**

1. Go to Shopify Settings > Custom Data
2. Create Metaobject Definition:
   * Name: "Swatch"
   * Add fields:
     1. Label (required): Single line text
     2. Color (optional): Color field
     3. Image (optional): Image file
3. Create Product Metafield:
   * Type: Metaobject (List of values)
   * Reference your Swatch metaobject
4. Assign values to products:
   * Edit product > Product Metafields
   * Add color/material options
5. Connect to filter:
   * Open Search & Discovery app
   * Add new filter using your metafield
   * Label it (e.g., "Color") and save

#### Important Notes

* You must manually update metafields for all products
* Changes don't happen automatically

**Filter by Color Option**

1. In Search & Discovery:
   * Add new filter
   * Select "Color" option
   * Save
2. For missing swatches:
   * Upload 64x64 JPG files
   * Name format: swatch-\[color].jpg (lowercase)
   * Only works with default CSS color names
