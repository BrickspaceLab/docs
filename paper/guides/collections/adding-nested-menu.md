# Adding Nested Menu

Each collection can be set up with nested navigation. This is useful if you have a large collection with multiple sub-groupings within. For example, you may have a collection titled Accessories using nested navigation you could then set up links to Wallets, Phone Cases, and Bags.

In this example clicking "Elastic" would navigate to a new page loading the "Elastic" collection page.

<figure><img src="../../.gitbook/assets/right.png" alt=""><figcaption></figcaption></figure>

{% stepper %}
{% step %}
### Create metafields definitions

1. Go to **Settings** > **Metafields**
2. Click **Collections** then click **Add definition**
3. Set **Name** to **Subcollections**
4. Set **Namespace** and key to `my_fields.subcollections`.
5. Click **Select content type** and choose **Single line text**
6. Click **Save**
{% endstep %}

{% step %}
### Add data to Collection metafield

1. Open the collection you’d like to add a tag filtering too
2. Scroll to the bottom **Metafields** area
3. Enter a text value for each tag filter
   * There's no need to include "All" as that will be the first link within tag filtering
   * Each entry should match a tag that is present within your collection
   * This text must be formatted in a specific way. Please ensure each menu item is separated by “&” then ensure each title and url for each item is separated by a “,”.
   * It should look something like this:
     * <pre><code><strong>Tops,/collections/tops&#x26;Bags,/collections/bags&#x26;Shorts,/collections/short
       </strong></code></pre>
4. Click **Save**
{% endstep %}
{% endstepper %}
