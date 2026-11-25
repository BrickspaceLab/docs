---
index: 4
---

# Customer approval

The customer approval system determines which customers can view restricted content, products, and pricing. Keystone supports two approval methods: tag-based approval and B2B customer accounts.

***

### Tag-based customer approval

Use a customer tag to give individual customers access to restricted content in Keystone. A customer can use this method without belonging to a Shopify B2B company.

#### Set the approval tag

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Account**
4. In **Matching tags**, enter one customer tag, such as `approved`
5. Click **Save**

#### Approve customers

1. In your Shopify admin, go to **Customers**
2. Find and select the customer you want to approve
3. In the **Tags** section, add the exact tag you configured (e.g., `approved`)
4. Click **Save**

Once tagged, the customer will see all restricted content when logged in.

***

### B2B customer approval

Shopify B2B supports companies and company locations on Basic, Grow, Advanced, and Plus. In **Settings > Customer accounts**, [activate customer accounts for B2B](https://help.shopify.com/en/manual/b2b/customer-login-and-accounts). Legacy accounts support retail sign-in only. Then create a company in **Customers > Companies**, add a location, and give the buyer permission to order for it. [Set up a company in Shopify](https://help.shopify.com/en/manual/b2b/companies-and-customers/creating-companies).

#### Enable B2B customers

1. Open the **Theme Editor** by clicking **Customize** next to your theme
2. Click **Theme Settings** (gear icon near the top left)
3. Scroll down and click **Account**
4. Check **Enable B2B customers**
5. Click **Save**

Sign in through customer accounts as the company buyer. If the buyer can order for multiple locations, select the location to test. With **Enable B2B customers** selected, Keystone shows the buyer restricted content even without the approval tag.

***

### Using both methods together

To admit both groups, enter an approval tag in **Matching tags** and select **Enable B2B customers**. Test one restricted product in each account.

* A signed-in customer with the matching tag can see the product.
* A signed-in B2B buyer can see it without the tag.
* A signed-in retail customer without the tag and a signed-out visitor should see the restriction.

Leaving **Matching tags** blank lets any signed-in customer pass Keystone’s approval check. To restrict access to company buyers only, enter a tag that you don’t assign to retail customers and enable the B2B setting.

***

### Important notes

{% hint style="warning" %}
**Approval tags are case sensitive!**

Tags must match exactly between the theme settings and customer tags. For example, if you set `Approved` in theme settings, the customer tag must also be `Approved`—`approved` or `APPROVED` won't work.
{% endhint %}

Keystone approval controls visibility. To give approved buyers a different price, [set up wholesale pricing](wholesale-pricing-apps.md).
