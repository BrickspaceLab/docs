---
published: false
---

# Brickspace Lab documentation migration

Prepared on October 31, 2026 for [BL-852](https://linear.app/brickspacelab/issue/BL-852/reconcile-brickspace-lab-help-docs-and-prepare-knowing-migration).

## Sources and scope

- Live help center: https://help.brickspacelab.com/.
- Live page inventory: https://help.brickspacelab.com/llms.txt.
- Knowing destination: https://knowing.fyi/sites/1e18c725-d1cd-4a8a-a8c9-2630ec564fca.
- Products: general support and services, Paper, Space, Keystone, Slab, and Pallet.

All 598 live pages in scope have source counterparts. `live-pages.json` maps each public Markdown URL to its repository path and records the SHA-256 of its downloaded export. No missing article needed to be invented to reach live page coverage. GitBook exports rewrite links, add folder listings, normalize Markdown, and append platform-specific instructions; those export additions are not imported as article content.

The existing article bodies and tracked assets remain the source. Page titles now match the live inventory. Intentional differences are the Brickspace Lab homepage, General and services landing page, explicit folder navigation, repaired links, corrected labels, and removal of references to absent standalone articles. Live instructions, release settings, prices, legal terms, feature defaults, and support policies have not been rewritten.

Catalog product docs are handled separately in `catalog-docs` and [BL-853](https://linear.app/brickspacelab/issue/BL-853/create-independent-catalog-docs-repository-for-helpcatalogcool). Shared company legal policies, including Catalog's software license, remain here. The unrelated Catalog changelog formerly at the repository root is preserved verbatim as `catalog-root-changelog.txt` so the separate migration can recover it.

## Knowing formatting

- The root README is the support homepage. Folder READMEs supply navigation names and landing pages.
- Flat integer `index` metadata follows the existing GitBook summaries. Top-level order is General and services, Paper, Space, Keystone, Slab, Pallet.
- Contributor instructions, migration notes, GitBook SUMMARY pages, and two GitBook include snippets use `published: false`.
- GitBook layout frontmatter and nonfunctional assistant action buttons have been removed. The four existing `hidden: true` pages retain their intent through `navigation: hidden`.
- Existing hints, steppers, content references, update blocks, HTML cards, tables, figures, and details remain supported Markdown. Code examples are preserved, including literal Liquid.
- Internal destinations use relative source paths with explicit `.md` files or `README.md`. Encoded image filenames retain their literal percent characters.
- Legacy empty heading anchors have been removed; Knowing supplies heading navigation.

The homepage's Pallet entry now opens Pallet rather than Paper. Old GitBook space links and broken page IDs have been replaced where a matching current destination exists. The Slab Button reference now uses the editor label **Simple subtotal** for `cart-price`, verified from the block schema and English schema locale. Recovery and app-style references point to existing support-policy sections and app guides. Missing mobile-preview and Paper-newcomer references were removed from navigation and are proposed below.

## Verification

`npm run sync` completed for all four themes. Source snapshots report Paper 8.1.3, Space 2.2.3, Keystone 2.2.0, and Slab 0.4.0. Schema labels were resolved through each theme's English schema locale. This migration preserves existing settings descriptions; it is not a fresh audit of every historical feature claim against those versions.

`npm run check` validates publication metadata, one H1 outside examples, block balance, local page and asset destinations, exclusion of contributor pages, live-page coverage, and Knowing size limits. It runs offline with Python 3.9 or later. Its small parser self-checks run with every invocation.

The actual metadata and Markdown parsers from the local Knowing checkout also accepted every published page. Root folder ordering was checked with Knowing's own comparator. The publication contains 624 pages: all 598 mapped live pages, an additional General and services landing page, and 25 folder landing pages. Eleven existing contributor/navigation/include Markdown files are excluded; this report is also excluded.

Live Knowing rendering remains an acceptance check. The destination did not load through web retrieval, and browser tooling could not start because the workspace's configured writable root is a symlink. No Knowing release, deployment, or DNS change was performed.

## Suggested follow-ups

| Priority | Suggestion | Evidence and existing work |
| --- | --- | --- |
| High | Replace signed Intercom image URLs with durable repository assets or approved stable media URLs. | Nineteen published pages retain image URLs containing an expiration parameter. See `content-gaps.json`. Local asset validation passes; remote media availability is not asserted. |
| High | Write a reusable guide for testing responsive layouts without publishing. | Missing article references existed in the support-intake and Keystone mobile-image guides. Removed dangling references; the relevant theme guides remain. |
| Medium | Write a Paper introduction for developers new to Shopify. | Paper's Theme basics linked to an absent standalone article. The dangling hint has been removed. |
| Medium | Finish the empty Paper color FAQ. | `paper/getting-started/theme-settings/colors.md` contains an unanswered “How can I change the accent colors in my theme settings?” entry. Preserve it pending a verified answer. |
| Medium | Expand customization and update-maintenance guidance. | The Space sticky-buy guide pointed at a missing customization-preservation article. It now links to the existing update guide. Continue [BL-649](https://linear.app/brickspacelab/issue/BL-649/write-docs-for-customizations-and-update-maintenance). |
| Medium | Complete the Slab buy/install/update walkthrough. | Continue [BL-684](https://linear.app/brickspacelab/issue/BL-684/write-better-setup-guides-for-slab), rather than opening a duplicate. |
| Medium | Review the outstanding support-derived gaps before writing more articles. | [BL-687](https://linear.app/brickspacelab/issue/BL-687/docs-gap-report-week-of-may-26-2026) remains open. Check what is still missing against the current docs. |
| Low | Refresh the product comparison to cover Slab alongside the other themes. | The current comparison excludes Slab and links to its feature list. Coordinate with [BL-464](https://linear.app/brickspacelab/issue/BL-464/highlight-key-aspectselling-points-on-the-differences-between-slab-and). |

## Release acceptance

Before replacing the existing help center, preview the candidate content in Knowing and check the homepage, folder order, cross-product links, image access, search, mobile layout, cards, steps, expandable FAQs, and changelogs. Confirm that the deployed Knowing version supports the same repository metadata and Markdown features as the checked source.

The existing source paths are preserved. GitBook's published routes still differ from some repository paths: the live General space is served at the domain root; custom CSS and utility-class pages have additional public URL aliases. `live-pages.json` is the starting point for a page-by-page redirect map, not an installed redirect configuration. Map both clean page URLs and `.md` endpoints when preparing a future domain cutover. Keep Catalog redirects coordinated with its independent migration. Publishing a release and changing DNS/redirects require separate authorization.
