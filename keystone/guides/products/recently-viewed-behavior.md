---
title: Recently Viewed — Behavior with Hidden and Out-of-Stock Products
description: Auto-generated stub — needs content
status: draft
created: 2026-05-11
source: weekly-gap-analysis
---

## Overview

> ⚠️ This page was auto-generated from support ticket analysis. It needs to be written.

**Why this doc is needed:**
A customer discovered that products hidden using the "hidden" tag still appear in the Recently Viewed section with the Add to Cart button and price visible. The existing recently-viewed.md section doc does not address this behavior. A related question about customizing out-of-stock variant text ("Sold Out") was also raised.

**Topics to cover:**
- How the Recently Viewed section stores and displays browsed products (browser session/localStorage)
- Known limitation: the "hidden" tag hides products from collections/search but NOT from the Recently Viewed component
- How to suppress hidden products from appearing in Recently Viewed (custom Liquid or CSS workaround)
- How to configure out-of-stock variant display text (e.g., changing "Unavailable" to "Sold Out")
- Where to find the sold-out label setting in theme settings vs section settings
- Limitations of the Recently Viewed section (no server-side filtering)

**Related tickets (Week of May 11, 2026):**
- #81841952 — Anurag Jayasawal (Keystone): "Hidden product still appears in Recently Viewed with Add to Cart and price visible"
- #81841952 — Anurag Jayasawal: "Can we change out-of-stock variant text to 'Sold Out'?"
