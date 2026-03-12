# Success and error overlays

Success and error overlays let Slab show feedback after a customer submits a form or when the theme encounters an action error. In most storefront templates, this feedback appears in an **Alert** overlay, even if the form itself is inside a **Popup**.

To learn more about overlay types, see [Popups, drawers and overlays](popups-drawers-and-overlays.md).


## How success and error overlays work

Slab uses a shared feedback flow for several built-in forms.

* A customer submits a form such as **Contact form**, **Newsletter form**, **Article comments**, or **Password form**.
* Shopify returns the form result to the theme.
* Slab checks whether the form was successful or whether it returned validation errors.
* Slab updates the feedback message and opens the built-in **Form response** alert overlay.

This means customers can submit a form inside a popup and still see the final feedback message in a separate alert overlay at the edge of the storefront.


## Form response and error blocks

Slab separates form feedback into two different block types: **Form response** and **Error**.

**Form response**

* Use this block for Shopify form submissions.
* It shows a status label such as success or error together with the returned message.
* On successful submission, it uses the form block's **Success message** setting.
* On failed submission, it shows the validation message returned by Shopify.

**Error**

* Use this block for general theme errors that are not coming from a Shopify Liquid form object.
* It is used for JavaScript and AJAX failures such as cart or quick action requests.
* It shows the error message returned by the failed action.

In practice, if you are comparing "form response" and "error response" behavior in Slab, the matching blocks are **Form response** and **Error**.


## Forms that use this feedback flow

The shared form response flow is used by these Slab form blocks:

* **Contact form**
* **Newsletter form**
* **Article comments**
* **Password form**

These forms all pass their submit result through the same helper, so merchants get a consistent feedback pattern across the storefront.


## What can trigger these overlays

Here are some common examples.

**Form response examples**

* A customer enters an invalid email address in a newsletter form.
* A customer leaves a required contact field blank.
* A contact form returns a field-specific validation message.
* A customer submits an article comment with missing or invalid author, email, or comment content.
* A customer enters the wrong storefront password.

**Error examples**

* An add-to-cart request fails.
* A quick buy or quick edit request fails.
* A cart quantity change fails.
* A cart note update fails.
* A discount code request fails.

For these error overlays, the exact message usually comes from Shopify's response, so the wording can vary depending on the failure.


## Important behavior to know

Use this pattern when you want customers to receive clear feedback without interrupting the rest of the storefront too heavily.

* A form can live inside a **Popup**, but the success or error message usually opens in the global **Alert** overlay instead of inside the popup body.
* The standard theme layout includes the global overlay group that contains the built-in **Form response** and **Error** alerts.
* The password page uses the minimal layout, which does not include the global overlay group by default, so its visible feedback behavior may not match other storefront templates exactly.

