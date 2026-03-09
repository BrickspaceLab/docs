# Getting started

Slab is a modular Shopify theme built on theme blocks. It is designed to be developer-friendly and highly customizable out of the box. Slab has a number of helpful features for developers and ai coding agents

* **Modular**: Built entirely on Shopify theme blocks. Mix, match, and extend sections without touching core files.
* **Fast**: Uses progressive enhancement and browser-native features. Core functionality works without JavaScript.
* **Powered by Alpine.js + Tailwind CSS v4**: Lightweight interactivity and utility-first styling without heavy dependencies.
* **AI-ready**: Includes Cursor rules, commands, and skills for AI-assisted development and code review.



## Getting started

#### Installing via ZIP

{% hint style="info" %}
Opt for ZIP installation if you're planning to build your storefront in the theme editor, but note that it won't provide full source code access.
{% endhint %}

{% stepper %}
{% step %}
Download the theme ZIP from your Polar order confirmation or customer portal.
{% endstep %}

{% step %}
In your Shopify admin, go to **Online Store → Themes**.
{% endstep %}

{% step %}
Click **Add theme → Upload zip file** and select the downloaded file.
{% endstep %}

{% step %}
Click **Publish** when ready to go live.
{% endstep %}
{% endstepper %}



#### Installing via GitHub (recommended for developers)

{% hint style="info" %}
Install these tools before you start:

* [Node.js](https://nodejs.org/en/download/) (18+)
* [npm](https://www.npmjs.com/package/npm)
* [Shopify CLI](https://shopify.dev/docs/themes/tools/cli/install) (3+)
{% endhint %}

{% stepper %}
{% step %}
**Fork or clone the repository**

If you have GitHub access from your Polar purchase, clone the repo directly:

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



## Scripts reference

| Script                | Description                                         |
| --------------------- | --------------------------------------------------- |
| `npm run dev`         | Start Vite + Shopify theme dev + section watcher    |
| `npm run build`       | Build sections and Vite assets for production       |
| `npm run theme-check` | Run Shopify theme check (output to `check.md`)      |
| `npm run json-check`  | Run JSON-focused theme check (output to `check.md`) |
| `npm run test`        | Run end-to-end browser tests                        |
| `npm run test:headed` | Run e2e tests with visible browser window           |



## Pulling upstream updates

If you forked the repo, you can pull in new Slab releases at any time:

```sh
git fetch upstream
git merge upstream/main
```

Resolve any conflicts, then run `npm install` to pick up any dependency changes.
