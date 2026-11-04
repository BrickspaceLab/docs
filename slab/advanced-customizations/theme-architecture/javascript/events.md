# Events

The theme dispatches custom events on `document` using `dispatchEvent()` from `src/javascript/core/utils.ts`. Listen for these events to react to cart changes or dynamic content updates without modifying theme source files.



## cart:change

Fired after every successful cart mutation — adding, editing, removing, or updating items, applying a discount code, or updating the cart note.

The `detail` object contains:

- `source` — the operation that triggered the update: `"add"`, `"change"`, `"edit"`, `"note"`, `"discount"`, `"add-multiple"`, or `"update"`.
- `cart` — the full array of current cart line items.
- `itemCount` — total number of items in the cart.
- `totalPrice` — cart total in cents.
- `variantId` _(optional)_ — the variant ID involved, included for `"add"`, `"edit"`, and `"change"` operations.
- `quantity` _(optional)_ — the quantity involved, included for `"add"`, `"edit"`, and `"change"` operations.

```javascript
document.addEventListener('cart:change', (event) => {
  const { source, cart, itemCount, totalPrice } = event.detail;
  console.log(`Cart updated via "${source}". Items: ${itemCount}, Total: ${totalPrice}`);
});
```



## cart:error

Fired when a cart API request fails. Use this to handle errors from cart operations in custom code without polling for state.

The `detail` object contains:

- `source` — the operation that failed: `"add"`, `"change"`, `"edit"`, `"note"`, `"discount"`, `"add-multiple"`, or `"update"`.

```javascript
document.addEventListener('cart:error', (event) => {
  const { source } = event.detail;
  console.warn(`Cart error during "${source}" operation.`);
});
```



## slider:updated

Fired by the recommendations and recently-viewed slider blocks after they finish fetching and injecting new slide content into a dynamic slider. Use this to re-initialize any third-party scripts that need to run after new slides are in the DOM.

No `detail` properties are included with this event.

```javascript
document.addEventListener('slider:updated', () => {
  // Re-initialize anything that depends on slider DOM content
});
```
