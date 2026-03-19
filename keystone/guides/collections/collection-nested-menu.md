# Add a nested menu

Each collection can be set up with nested navigation. This is useful if you have a large collection with multiple sub-groupings within. For example, you may have a collection titled Accessories using nested navigation you could then set up links to Wallets, Phone Cases, and Bags.

In this example clicking "Elastic" would navigate to a new page loading the "Elastic" collection page.

***

### Create metafields definitions <a href="#h_8713c28b98" id="h_8713c28b98"></a>

1. Go to **Settings** > **Metafields**
2. Click **Collections** then click **Add definition**
3. Set **Namespace** and key to `custom.subcollections`
4. Click **Select content type** and choose **Single line text**
5. Click **Save**

***

### Add data to Collection metafield <a href="#h_6bebd429e6" id="h_6bebd429e6"></a>

1. Open the collection you'd like to add a tag filtering too
2. Scroll to the bottom **Metafields** area
3. Enter a text value for each tag filter
   * There's no need to include "All" as that will be the first link within tag filtering
   * Each entry should match a tag that is present within your collection
   * This text must be formatted in a specific way. Please ensure each menu item is separated by "&" then ensure each title and url for each item is separated by a ",".
   * It should look something like this:
     * `Tops,/collections/tops&Bags,/collections/bags&Shorts,/collections/short`
4. Click **Save**

\
**Further explanation:**&#x20;

Enter your sub-collection links in this format:

`Label,/collections/handle&Label,/collections/handle&Label,/collections/handle`

* `Label` = the text shown to customers (example: `Tops`)

_Example:_ **Sibling Products,/**

* `/collections/handle` = the link destination. You can find your collection handle within the collection your trying to link to. Reference the screen shot below.&#x20;

_Example:_ **Collections/sibling-products**

<details>

<summary>S<em>creen shot of where to find your collection handle</em></summary>

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>



</details>

* `&` = separates each menu item

_Full example:_ **Sibling Products,/collections/sibling-products**

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>
