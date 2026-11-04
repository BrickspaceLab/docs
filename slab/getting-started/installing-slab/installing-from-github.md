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
**Fork the repository**

After purchasing the theme, you'll have GitHub access. On GitHub, fork [`BrickspaceLab/slab`](https://github.com/BrickspaceLab/slab) to your account. Then clone **your fork** (not the upstream repo directly) and add the original repo as `upstream` so you can merge new releases later—see [Pull upstream updates](../../advanced-customizations/getting-started/pulling-upstream-updates.md).

```sh
git clone https://github.com/<your-github-username>/slab.git
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

Set `STORE_DOMAIN` to your development store domain:

```sh
STORE_DOMAIN=your-store.myshopify.com
```

Optional values:

* Add `STORE_PASSWORD` if the storefront is password-protected.
* Add `SHOPIFY_CLI_THEME_TOKEN` if you want Shopify CLI to authenticate without prompting.
* Add `CORS_ORIGINS` if you preview the theme on a custom domain.&#x20;
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
{% endstep %}

{% step %}
**Activate your license**

When the theme loads in your store for the first time, it will prompt you to enter your license key. Enter the key from your order confirmation or customer portal. This activates and assigns the license to this store.
{% endstep %}

{% step %}
**Optional: add repo secrets for GitHub Actions**

Preview deploys use `STORE_DOMAIN` and `SHOPIFY_CLI_THEME_TOKEN`.

Other CI workflows may also need secrets such as `CURSOR_API_KEY`.
{% endstep %}
{% endstepper %}
