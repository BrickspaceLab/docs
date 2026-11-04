# Customer approval

The customer approval system determines which customers can view restricted content, products, and pricing. Keystone supports two approval methods: tag-based approval and B2B customer accounts.

***

### Tag-based customer approval <a href="#tag-based" id="tag-based"></a>

Tag-based approval is the most flexible option and works on all Shopify plans.

#### Setup approval tag

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Account**
4. In the **Matching tag** field, enter a tag (e.g., `approved`)
5. Click **Save**

#### Approve customers

1. In your Shopify admin, go to **Customers**
2. Find and select the customer you want to approve
3. In the **Tags** section, add the exact tag you configured (e.g., `approved`)
4. Click **Save**

Once tagged, the customer will see all restricted content when logged in.

***

### B2B customer approval <a href="#b2b" id="b2b"></a>

B2B customer accounts are available on **Shopify Plus** plans and provide enterprise-level wholesale features.

#### Enable B2B customers

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Account**
4. Check **Enable B2B customers**
5. Click **Save**

All B2B customers will automatically see restricted content when logged in.

For more information on setting up B2B accounts, visit [Shopify B2B Help](https://help.shopify.com/en/manual/b2b).

***

### Using both methods together <a href="#combined" id="combined"></a>

You can enable both tag-based and B2B approval simultaneously:

* Customers with the matching tag will see restricted content
* B2B customers will also see restricted content
* Regular customers without tags won't see restricted content

This gives you flexibility to manage both B2B accounts and individual wholesale customers.

***

### Important notes <a href="#notes" id="notes"></a>

{% hint style="warning" %}
**Approval tags are case sensitive!**

Tags must match exactly between the theme settings and customer tags. For example, if you set `Approved` in theme settings, the customer tag must also be `Approved`—`approved` or `APPROVED` won't work.
{% endhint %}

* Customers must be logged in to see restricted content
* Changes to customer tags take effect immediately
* B2B accounts require Shopify Plus
