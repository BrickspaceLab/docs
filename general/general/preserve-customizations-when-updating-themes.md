# Preserve customizations when updating themes

Updating to a new Brickspace Lab theme version brings bug fixes and features, but not every customization moves automatically. Use this guide to understand what survives an update and what you need to transfer manually.

For install steps, see your theme’s **Update your theme** guide ([Paper](../../paper/guides/basics/update-your-theme.md), [Space](../../space/guides/basics/update-your-theme.md), [Keystone](../../keystone/guides/basics/update-your-theme.md), [Slab](../../slab/guides/basics/update-your-theme.md)).

## What is usually preserved

These customizations live in Shopify’s theme configuration and can be copied to a new theme copy:

| Customization | How it is stored | Transfer method |
| ------------- | ---------------- | --------------- |
| **Theme settings** (colors, typography, toggles) | `config/settings_data.json` | Copy file contents to the new theme (see update guide) |
| **Section and block layout** on customized templates | Template JSON files (blue dot in **Edit code**) | Copy each customized template file |
| **Custom CSS** from theme editor fields | Stored in `settings_data.json` | Included when you copy `settings_data.json` |
| **Navigation and menus** | Shopify admin (**Content** > **Menus**) | Unchanged—menus are store-level, not theme files |
| **Products, collections, metafields** | Shopify admin | Unchanged |

{% hint style="info" %}
Copying `settings_data.json` brings over theme settings and custom CSS from the editor. It does **not** copy hand-edited Liquid, JavaScript, or snippet files.
{% endhint %}

## What is not preserved automatically

| Customization | Why |
| ------------- | --- |
| Edits in **Edit code** (Liquid, JS, CSS files) | New theme versions ship fresh code files |
| Changes made by apps in theme files | May reference old file paths or conflict with new markup |
| AI-generated code (Sidekick, etc.) | Treated as custom code—you must merge manually |
| Deprecated settings from very old versions | New schemas may rename or remove settings |

If a developer edited theme files, assume those edits must be reviewed file-by-file on the updated theme. See [Migrate custom changes](../../paper/guides/sitewide/migrating-custom-changes.md) for merge practices.

## Recommended update workflow

{% stepper %}
{% step %}
**Duplicate and back up**

Duplicate your live theme before installing an update. Keep at least one copy of the pre-update theme in your library.
{% endstep %}

{% step %}
**Add the latest version to your library**

From **Online Store** > **Themes**, add the newest theme version from the Shopify Theme Store or your purchase flow. Do not publish yet.
{% endstep %}

{% step %}
**Transfer settings and templates**

Follow the **How to transfer settings after updating** steps in your theme’s [Update your theme](../../keystone/guides/basics/update-your-theme.md) guide: copy `settings_data.json`, then copy customized template JSON files (blue indicator in the templates folder).
{% endstep %}

{% step %}
**Reapply code changes (if any)**

Compare **Edit code** between old and new themes. Reapply only the custom snippets or sections you still need—or hire a developer for a clean merge.
{% endstep %}

{% step %}
**Preview, then publish**

Customize the new theme, test critical templates (home, collection, product, cart, wholesale login flows), then publish when satisfied.
{% endstep %}
{% endstepper %}

## Custom code and support

Installing an update does not remove custom code from your **old** theme duplicate, but Brickspace Lab support covers defects in **unmodified** current theme files only. If custom or AI-generated code causes issues after an update, see [Support policy for modified theme code](support-policy-for-modified-theme-code.md).

## Related reading

* [Update your theme — Keystone](../../keystone/guides/basics/update-your-theme.md)
* [Migrate custom changes — Paper](../../paper/guides/sitewide/migrating-custom-changes.md)
* [Recover from third-party theme code changes](recover-from-third-party-theme-code.md)
