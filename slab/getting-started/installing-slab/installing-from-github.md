---
index: 1
---

# Install from GitHub

## Install with your agent

After purchasing Slab and receiving GitHub access, copy this prompt into your agent.

{% prompt description="Install command" %}
```markdown
Fetch and read https://help.brickspacelab.com/slab/getting-started/installing-slab/installing-from-github.md, then follow the instructions to install Slab and open a local preview. Use a fork of the Slab repository, ask me for my Shopify store domain and any missing access, and verify the storefront loads in the browser. Keep the theme unpublished.
```
{% endprompt %}

## How to install

{% hint style="info" %}
Opt for direct GitHub installation if you're planning to build customizations or want full source control of your theme code.
{% endhint %}

{% hint style="info" %}
Install these tools before you start:

* [Node.js](https://nodejs.org/en/download/) (24+, matching Slab CI)
* [npm](https://www.npmjs.com/package/npm)
* [Shopify CLI](https://shopify.dev/docs/themes/tools/cli/install) (4.8.4, for Shopify previews and uploads)
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
npm ci --include=dev
```
{% endstep %}

{% step %}
**Open a local preview**

```sh
npm run build
npx --yes local-storefront@0.1.16 serve --theme . --port 0 --preview liquid-july-26 --live-reload
```

Open the URL printed after `ready:`. This preview uses demo data and needs no Shopify credentials. Rebuild after changes to section source or assets.
{% endstep %}

{% step %}
**Preview with your Shopify catalog**

For the theme editor or real products, copy the example environment file:

```sh
cp .env.example .env
```

* Set `STORE_DOMAIN` to your development store's `myshopify.com` domain.
* Set `STORE_PASSWORD` if the storefront is password protected.
* Set `SHOPIFY_CLI_THEME_TOKEN` for noninteractive Theme Access authentication.

Run `npm run dev`. When it prints `READY`, open the storefront or editor link it provides. The command builds and uploads changes to an unpublished theme for this worktree and store. Refresh the preview after uploads.

For Vite hot reload, use `npm run dev:hmr` with an HTTPS tunnel. If the storefront uses a custom domain, set `CORS_ORIGINS` to the allowed HTTPS origins.
{% endstep %}

{% step %}
**Activate your license**

When the theme loads in your store for the first time, it will prompt you to enter your license key. Enter the key from your order confirmation or customer portal. This activates and assigns the license to this store.
{% endstep %}

{% step %}
**Optional: add repo secrets for GitHub Actions**

The pull request preview workflow uses `STORE_DOMAIN` and `SHOPIFY_CLI_THEME_TOKEN` to deploy an unpublished theme. Use the preview and editor links posted on the pull request. For a password protected store, provide `STORE_PASSWORD` for browser checks.
{% endstep %}
{% endstepper %}
