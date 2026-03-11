# Install from GitHub

## How to install

{% hint style="info" %}
Opt for direct GitHub installation if you're planning to build customizations or want full source control of your theme code.
{% endhint %}

{% hint style="info" %}
Install these tools before you start:

* [Node.js](https://nodejs.org/en/download/) (18+)
* [npm](https://www.npmjs.com/package/npm)
* [Shopify CLI](https://shopify.dev/docs/themes/tools/cli/install) (3+)
{% endhint %}

{% stepper %}
{% step %}
**Fork or clone the repository**

After purchasing the theme you'll have GitHub access, clone the repo directly:

```sh
git clone https://github.com/BrickspaceLab/slab.git
cd slab
```

To maintain your own copy with the ability to pull upstream updates, fork the repo first on GitHub, then clone your fork:

```sh
git clone https://github.com/YOUR_USERNAME/slab.git
cd slab
git remote add upstream https://github.com/BrickspaceLab/slab.git
```
{% endstep %}

{% step %}
**Install dependencies**

```sh
npm install
```
{% endstep %}

{% step %}
**Configure environment variables**

Copy the example env file and fill in your values:

```sh
cp .env.example .env
```

| Variable         | Required | Description                                        |
| ---------------- | -------- | -------------------------------------------------- |
| `STORE_PASSWORD` | Optional | Storefront password, if your store has one enabled |
{% endstep %}

{% step %}
**Point to your store**

Slab licenses are **per-store** — one license covers one storefront. Work directly against the store where the theme will be published. There is no need for a separate development store.

Open `package.json` and update the `config.store` field:

```json
"config": {
  "store": "your-store.myshopify.com"
}
```

Then authenticate Shopify CLI with that store:

```sh
shopify auth login --store your-store.myshopify.com
```
{% endstep %}

{% step %}
**Activate your license**

When the theme loads in your store for the first time, it will prompt you to enter your license key. Enter the key from your order confirmation or customer portal. This activates and assigns the license to this store.
{% endstep %}

{% step %}
**Start local development**

```sh
npm run dev
```

This runs three parallel processes:

* **Vite dev server** — compiles and hot-reloads CSS and JavaScript
* **Shopify theme dev** — pushes your local files to an **unpublished** development preview on your store, served at `http://127.0.0.1:9292`
* **Section watcher** — compiles `src/sections/` preset JSON files into `sections/`

Your live store is unaffected while you work — `shopify theme dev` creates a separate unpublished copy of the theme. Publish it through the Shopify admin when you are ready to go live.

> The Vite dev server shows an informational page at its own port — this is expected. The actual theme preview is at `http://127.0.0.1:9292` via Shopify CLI.
{% endstep %}
{% endstepper %}
