# Cookies and consent banner

**Priority:** secondary operational/legal UX — implement with a consent management platform (CMP) such as Cookiebot, Osano, OneTrust, or similar if you use non-essential cookies or trackers.

**Last updated:** April 29, 2026

This page supports implementation of a **cookie banner** consistent with **PIPEDA** (meaningful consent for non-essential tracking where required) and **GDPR** for visitors from the EEA/UK. It is **not** a substitute for configuring your CMP correctly or listing every cookie your stack sets.

---

## 1. Suggested banner copy (English)

Use variants as needed (short vs. detailed link).

### Short notice

> We use cookies and similar technologies to run our site, remember preferences, and measure traffic. By clicking **Accept all**, you agree to non-essential analytics as described in our Cookie notice and [Privacy policy](./privacy-policy.md). You can change your choices anytime via **Cookie settings**.

Buttons: **Accept all** · **Reject non-essential** · **Cookie settings**

### Longer notice (expandable)

> **Cookies.** We use cookies that are essential for security and basic functionality. With your consent, we also use analytics and marketing pixels to understand how our Site is used. Third-party providers may process data per their policies—for example **Google Analytics**, **Meta** (Facebook pixel), and tools loaded via **Shopify Web Pixels**.  
> **Your choices.** Essential cookies cannot be turned off here. You may accept or reject non-essential cookies. You can withdraw consent later.  
> See our [Privacy policy](./privacy-policy.md) for retention and rights.

---

## 2. Categories to disclose in “Cookie settings”

| Category | Purpose | Typical examples |
| --- | --- | --- |
| **Strictly necessary** | Security, load balancing, consent storage, session | Auth cookies, CSRF, CMP consent string |
| **Functional** | Remember preferences (language, region) | Preference cookies |
| **Analytics** | Measure visits, funnels, errors | GA4, Plausible, etc. |
| **Marketing** | Attribution, remarketing | Ads pixels — **only if used** |

---

## 3. Implementation checklist

- [ ] Inventory scripts (tag manager, embedded chat, analytics, video embeds).
- [ ] Block non-essential scripts until consent (CMP default **deny** where required).
- [ ] Link to **[Privacy policy](./privacy-policy.md)** and optional dedicated cookie list page at https://brickspacelab.com/cookies.
- [ ] Log consent versions for GDPR accountability if EU traffic is realistic.
- [ ] Refresh inventory when adding tools (new analytics, heatmaps, CRM embeds).

---

## 4. Do Not Track

Browsers’ “Do Not Track” signals are **not** uniformly standardized. Describe your approach in the Privacy Policy (many sites state they **do not respond** to DNT but offer CMP controls).

---

## 5. Shopify storefront vs marketing site

Cookie rules apply to **your marketing website**. **Shopify storefronts** used by merchants have **their own** merchant obligations (merchant is often controller). Clarify roles: Brickspace Lab’s Site vs merchants’ stores.

---

## Contact

**hello@brickspacelab.com**
