# Tag filtering

***

Using Space you can update collection template to use tag based filtering. This is an easy way to surface sub-categories within a collection. For example, you may have a collection titled Accessories using nested navigation you could then set up links to Wallets, Phone Cases, and Bags.

In this example clicking "Shirts" would filter the current collection to only show products that contain the tag "shirts".

[![](https://downloads.intercomcdn.com/i/o/1200219594/adc75869bc7aba6b78b6f53a/CleanShot+2024-10-01+at+11_38_36%402x.png?expires=1744835400\&signature=1e65d517891b7dac07dec069d997b67e6090337d360ff8fded457d40d380e827\&req=dSInFst%2FlIRWXfMW1HO4zWYeriHoyTzt%2BG3pzSmDpF%2FyUhDh2e%2FZBpfVP7nF%0A8YsdRpaQJniaHa0QQ58%3D%0A)](https://downloads.intercomcdn.com/i/o/1200219594/adc75869bc7aba6b78b6f53a/CleanShot+2024-10-01+at+11_38_36%402x.png?expires=1744835400\&signature=1e65d517891b7dac07dec069d997b67e6090337d360ff8fded457d40d380e827\&req=dSInFst%2FlIRWXfMW1HO4zWYeriHoyTzt%2BG3pzSmDpF%2FyUhDh2e%2FZBpfVP7nF%0A8YsdRpaQJniaHa0QQ58%3D%0A)

## Create metafield definitions

1. Open up Settings and click Custom data.
2. Click Collections then click Add definition.
3. Set Name to Subtags.
4. Set Namespace and key to `custom.subtags`.
5. Click Select content type and select Single line text.
6. Click List of values.
7. Click Save.

## Add data to collection metafield

1. Open the collection you'd like to add a tag filtering too
2. Scroll to the bottom Metafields area.
3. Enter a text value for each tag filter
   * There's no need to include "All" as that will be the first link within tag filtering
   * Each entry should match a tag that is present within your collection
4. Click Save.
