# Nested menu

***

Each collection can be set up with nested navigation. This is useful if you have a large collection with multiple sub-groupings within. For example, you may have a collection titled Accessories using nested navigation you could then set up links to Wallets, Phone Cases, and Bags.

## Create metafield definitions

1. Open up Settings and click Metafields.
2. Click Collections then click Add definition.
3. Set Name to Subcollections.
4. Set Namespace and key to `my_fields.subcollections`.
5. Click Select content type and select Single line text.
6. Click Save.

## Add data to collection metafield

1. Open the collection you'd like to add a nested menu to
2. Scroll to the bottom Metafields area.
3.  Enter a text value.

    * This text must be formatted in a specific way. Please ensure each menu item is separated by "&" then ensure each title and url for each item is separated by a ",".
    * This should look something like the below

    ```
    Tops,/collections/tops&
    Bags,/collections/bags&
    Shorts,/collections/shorts
    ```
4. Click Save.
