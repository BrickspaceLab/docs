# Install a review app

{% hint style="warning" %}
**We do not provide support for code customizations**

If you are not comfortable making code changes, we highly recommend [hiring an expert developer](../../support/hire-a-shopify-developer.md).
{% endhint %}

{% hint style="info" %}
Most apps support app-block install for reviews widgets.
{% endhint %}

To display ratings and reviews properly in our Shopify themes, a standard metafield is used. If your review app doesn't use this metafield, you'll need to edit the code to integrate review widgets throughout



### Changing review and rating metafields

{% stepper %}
{% step %}
**Find correct metafields**

* Identify the metafields used by your review app - you may have to look through app documentation or contact support.
{% endstep %}

{% step %}
**Edit code**

* Open up `component__rating.liquid`&#x20;
* If you can't find a metafield from your app that points to the max value then you can manually set this. E.g. if your rating system goes from 0-5 you would set max to 5.
* Update lines 29-31 to point to your app metafields. After making changes it should look something like this. The below example uses metafields from Loox.&#x20;

{% code title="component__rating.liquid" %}
```liquid
{% assign rating = product.metafields.loox.avg_rating | times: 1 %}
{% assign rating_count = product.metafields.loox.num_reviews  %}
{% assign max = 5 %}
```
{% endcode %}
{% endstep %}
{% endstepper %}
