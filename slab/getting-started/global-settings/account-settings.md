# Account

Account settings in **Theme settings > Account** help limit catalog or blog visibility to approved customers, optionally treat B2B customers as approved, and choose how restricted content appears.



## How to change theme account

{% stepper %}
{% step %}
### Set approved customers

* Open **Theme settings > Account**.
* Under **Approved customers**, enter **Matching tags** for customers who may view restricted content.
* Optional: turn on **Enable B2B customers** so logged-in B2B customers count as approved.
{% endstep %}

{% step %}
### Set restricted content rules

* Under **Restricted content**, enter **Hide products with tag** and **Hide blog posts with tag** to hide those items from customers who are not approved.
* Optional: turn on **Enable full restriction** so only approved logged-in customers can use the site when your policy requires it.
{% endstep %}

{% step %}
### Choose restricted style

* Under **Styles**, set **Restricted style** to **Hidden** or **Placeholder**.
{% endstep %}

{% step %}
### Test with accounts

* Sign in as tagged and untagged test customers and confirm behavior before publishing.
{% endstep %}
{% endstepper %}



### Notes on account restrictions

* Tags must match how you tag customers and content in Shopify.
* **Enable full restriction** is a strong gate—confirm essential pages remain reachable for support.
* **Placeholder** keeps layout; **Hidden** removes items from view for unapproved customers.



## Account settings



### Approved customers

| Setting                 | What it controls                                                                 |
| ----------------------- | -------------------------------------------------------------------------------- |
| Matching tags           | Customers with these tags count as approved for restricted content.              |
| Enable B2B customers    | Logged-in B2B customers count as approved when enabled.                          |



### Restricted content

| Setting                    | What it controls                                                                 |
| -------------------------- | -------------------------------------------------------------------------------- |
| Hide products with tag     | Products with this tag are hidden unless the customer is approved.               |
| Hide blog posts with tag   | Posts with this tag are hidden unless the customer is approved.                  |
| Enable full restriction    | When on, customers must be logged in to an approved account to view the site.    |



### Styles

| Setting            | What it controls                                                                 |
| ------------------ | -------------------------------------------------------------------------------- |
| Restricted style   | **Hidden** or **Placeholder** for restricted products and posts. Default **Placeholder**. |
