# Add custom JavaScript

Since our themes are built using Alpine it's often best to consider adding functionality through Alpine first. We can use Alpine to add functionality by writing code directly inside the liquid markup.

For more advanced customizations we recommend using our development toolkits.



## Access theme functions and data

If you are integrating your Shopify theme with a third-party app you may want to access some of the globally available functions. Since our themes utilize [Alpine.js](https://alpinejs.dev/) this is done a bit differently than normal.

The first step is to access the app object. This object contains all the exposed functions and is stored in the \_x\_dataStack array of the html element. Here is how to access it:

```javascript
var app = document.querySelectorAll('html')[0]._x_dataStack[0];
```

From here you can call any of the functions available in the . For example if you want to call cart.updateCart() you could do the following.

```javascript
app.updateCart(true);
```
