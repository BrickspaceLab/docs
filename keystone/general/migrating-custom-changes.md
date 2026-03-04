# Migrating custom changes

## Merging custom changes in Shopify themes - challenges and best practices

When working with Shopify themes, updating to a new version can introduce challenges when customizations have been made. Since Shopify does not provide a built-in way to merge custom changes automatically, you must manually merge these changes. This document outlines the key challenges and best practices for managing and transferring custom changes during theme updates.

### Challenges in merging custom changes

#### 1. Manual transfer required

* Custom code changes (HTML, CSS, JavaScript, Liquid) must be manually identified and reapplied to the updated theme.
* Shopify does not support automatic merging of theme modifications.

#### 2. Difficulty tracking changes

* Without proper documentation, locating custom changes can be time-consuming.
* Developers may not always know where modifications were made, leading to potential loss of functionality.

#### 3. Theme updates may overwrite customizations

* If an update is applied without first backing up custom changes, they may be lost.
* Some theme settings may reset, requiring reconfiguration.

#### 4. No control over data transfer (Shopify limitation)

* As theme developers, we cannot control how Shopify handles theme updates.
* The platform does not provide tools for selective merging of custom code.

***

### Best practices for managing custom changes

#### 1. Document all customizations

* Maintain a detailed log of all modifications, including:
  * Modified files (e.g., `theme.liquid`, `product-template.liquid`, `custom.css`).
  * Specific code snippets added or altered.
  * Any third-party apps or scripts integrated.

#### 2. Use a version control system (Git)

* Track changes using Git to easily compare old and new versions.
* Create branches for custom work to avoid conflicts during updates.

#### 3. Test updates in a development environment first

* Duplicate the live theme and apply updates in a development/staging environment.
* Verify that custom changes are preserved before pushing to production.

#### 4. Consider not updating if unnecessary

* If the current theme works as intended, updates may not be required.
* Weigh the benefits of new features against the effort of reapplying customizations.

#### 5. Work closely with developers

* Ensure developers are aware of all custom changes before an update.
* Provide them with documentation to streamline the transfer process.
