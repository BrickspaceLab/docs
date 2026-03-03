# GitHub Actions

Slab currently includes GitHub Actions workflows for theme checks, Lighthouse checks, PR review automation, and a paused Playwright pipeline.

## Canonical files

- `/Users/thomaskimura/Documents/GitHub/slab/.github/workflows/check-theme.yml`
- `/Users/thomaskimura/Documents/GitHub/slab/.github/workflows/check-lighthouse.yml`
- `/Users/thomaskimura/Documents/GitHub/slab/.github/workflows/review-rules.yml`
- `/Users/thomaskimura/Documents/GitHub/slab/.github/workflows/test-playwright.yml`

## Active workflows

### Theme check

- Trigger: `push`
- Action: `shopify/theme-check-action@v2`
- Purpose: run Shopify Theme Check against repository theme files

### Lighthouse check

- Trigger: `push`
- Action: `shopify/lighthouse-ci-action@v1`
- Purpose: enforce Lighthouse performance/accessibility thresholds
- Uses store credentials from repository secrets

### Review rules

- Trigger: pull requests (`opened`, `synchronize`, `reopened`, `ready_for_review`)
- Purpose: run Cursor-based automated review using `.cursor/rules`
- Skips branches starting with `docs/`

## Paused workflow

### Playwright tests

- Trigger: pull requests
- Current status: paused (`if: false`)
- Behavior when enabled:
  - installs dependencies and Playwright Chromium
  - deploys preview theme
  - runs E2E tests
  - posts PR comment with results
  - cleans up preview theme

## Required secrets

Depending on workflow:

- `GITHUB_TOKEN`
- `CURSOR_API_KEY`
- `SHOP_STORE`
- `SHOP_PASSWORD`
- `SHOP_ACCESS_TOKEN`
- `LHCI_GITHUB_APP_TOKEN`

## Gotchas

- Some repo docs still say there is no GitHub Actions CI. The workflow files above are the source of truth.
- The Playwright workflow exists but is intentionally paused, so `test:e2e` remains a local/manual path unless CI is re-enabled.
