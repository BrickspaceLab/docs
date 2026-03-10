# Adding Tag Filtering

Using Paper you can update collection template to use tag based filtering. This is an easy way to surface sub-categories within a collection. For example, you may have a collection titled Accessories using nested navigation you could then set up links to Wallets, Phone Cases, and Bags.

In this example clicking "Wallets" would filter the current collection to only show products that contain the tag "wallets".

<figure><img src="../../.gitbook/assets/tag filter.png" alt=""><figcaption></figcaption></figure>

{% stepper %}
{% step %}
### Create metafield definitions

1. Click **Collections** then click **Add** **definition**
2. Set **Name** to **Subtags**
3. Set **Namespace** and key to `custom.subtags`
4. Click **Select content type** and select **Single line text**
5. Click **List of values**
6. Hit **Save**
{% endstep %}

{% step %}
### Add data to collection metafield

1. Open the collection you’d like to add a tag filtering too
2. Scroll to the bottom **Metafields** area.
3. Enter a text value for each tag filter
   * There's no need to include "All" as that will be the first link within tag filtering
   * Each entry should match a tag that is present within your collection
{% endstep %}
{% endstepper %}
