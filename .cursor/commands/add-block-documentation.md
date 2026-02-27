# Add block documentation

Produce `slab/blocks/<category-folder>/<title-slug>.md` in the `BrickspaceLab/docs` repository for any Liquid block so designers/devs understand how to configure it.


## Output rules

1. **File path** — `slab/blocks/{category-folder}/{title-slug}.md` inside the `BrickspaceLab/docs` repository.
   - Read `presets[0].category` from the schema. If it starts with `t:`, resolve it from `locales/en.default.schema.json`.
   - Convert the category key to a folder using this strict mapping:
     - `1_basics -> basics/`
     - `1_cards -> cards/`
     - `1_containers -> containers/`
     - `1_forms -> forms/`
     - `2_all_pagination -> all-pagination/`
     - `2_blog -> blog/`
     - `2_cart -> cart/`
     - `2_collections -> collections/`
     - `2_products -> products/`
     - `2_search -> search/`
     - `3_layout -> layout/`
     - `3_navigation -> navigation/`
     - `3_overlays -> overlays/`
     - `4_custom -> custom/`
     - `4_utility -> utility/`
   - Build `{title-slug}` from the block's English title (schema `name` translated via locale if `t:`), using lowercase kebab-case (e.g., `Menu item` -> `menu-item.md`).
   - Fallbacks:
     - If category is missing or unmapped, use `utility/`.
     - If title cannot be resolved, fallback to handle-based slug from the block filename.
2. **Heading case** — Sentence case for every `##` heading; leave two blank lines before each heading (except the H1 title).
3. **PR delivery** — Always deliver changes as a single pull request to `BrickspaceLab/docs`:
   1. Check if the repo is already cloned locally; if not, clone it: `gh repo clone BrickspaceLab/docs`.
   2. Determine the current slab branch name: `git -C <slab-repo> rev-parse --abbrev-ref HEAD`. Use it as `{source-branch}`.
   3. Create or check out a single branch in the docs repo: `docs/slab-{source-branch}` (e.g. `docs/slab-feat-slider`). If the branch already exists, check it out; otherwise create it from `main`.
   4. Write (or overwrite) each block's file at `slab/blocks/{category-folder}/{title-slug}.md`.
   5. Stage all changed files and commit: `docs(slab): update block docs for {source-branch}`.
   6. Push the branch and open one PR targeting `main` (or update the existing one if a PR for that branch already exists): `gh pr create --repo BrickspaceLab/docs --base main --title "docs(slab): update block docs for {source-branch}" --body "Updates documentation for blocks changed in \`{source-branch}\`: {comma-separated list of handles}."`.


## Sections

1. **Title**
   - Read from the block schema `name`. If it starts with `t:`, look up the English text in `locales/en.default.schema.json`.
   - This resolved English title is also the source for `{title-slug}` in the filepath rule.

2. **Category**
   - Read `presets[0].category` from the block schema.
   - If it starts with `t:`, look up the English text in `locales/en.default.schema.json` using the same translation lookup rules.
   - Use this category key to determine `{category-folder}` via the mapping in Output rules.

3. **Overview**
   - Two sentences max describing the block's purpose.
   - Prefer the `{% comment %}`/`{% doc %}` content; otherwise infer from schema + markup.

4. **Common use cases**
   - One plain-English sentence describing what a merchant can do with this block. Keep it simple and practical — no implementation details. Example for the rich text block: "Add text to your online store and adjust settings to control font size, color, and alignment."

5. **Block limitations** (only for private blocks that start with `_`)
   - Only include this section if the block filename starts with `_`. Skip it entirely for public blocks.
   - Document: where this block can be used (which sections or parent blocks), any specific requirements or dependencies, and why it's private rather than public.

### 6. Compatible blocks (conditional)

**Only include this section if the block can accept nested blocks. Check for:**
- `{% content_for 'blocks' %}` in the Liquid file
- `{% content_for 'block', type: ... %}` in the Liquid file
- `"blocks"` array in the schema with `"type": "@theme"` or `"type": "@app"`

**Determining compatible blocks:**

1. **If schema contains `"blocks": [{ "type": "@theme" }]`**:
   - Use: "The following blocks can be nested within this block:"
   - List: "All theme blocks"

2. **If schema contains `"blocks": [{ "type": "@app" }]`**:
   - Use: "The following blocks can be nested within this block:"
   - List: "App blocks"

3. **If schema contains both `"type": "@theme"` and `"type": "@app"`**:
   - Use: "The following blocks can be nested within this block:"
   - List: "All theme blocks" and "App blocks" on separate lines

4. **If Liquid file contains `{% content_for 'blocks' %}`** (without type restriction):
   - Use: "The following blocks can be nested within this block:"
   - List: "All theme blocks"

5. **If Liquid file contains `{% content_for 'block', type: 'g__container' %}`**:
   - Use: "The following blocks can be nested within this block:"
   - List: `[Container](../containers/container.md)`

6. **If Liquid file contains `{% content_for 'block', type: 'specific_block_type' %}`**:
   - Use: "The following blocks can be nested within this block:"
   - List the specific block type as a clickable markdown link using friendly translated names
   - Format: `[Block Name](relative/path/to/title-slug.md)` where the filename is derived from the block's translated English title in lowercase kebab-case (e.g., `[Container](../containers/container.md)`, `[Product card](../cards/product-card.md)`, `[Spot](../basics/spot.md)`).
   - Derive the destination folder from the nested block's category key using the same category mapping in **Output rules**.

**Use friendly translated block names** (e.g., "Container" not "g__container", "Product card" not "g__product-card"). Look up block names in `locales/en.default.schema.json` under the `blocks` key.

**Make compatible blocks clickable**: Always format specific block types as markdown links to their documentation files using category + title-slug paths (e.g., `[Container](../containers/container.md)`). For generic categories like "All theme blocks" or "App blocks", keep them as plain text (not links).

7. **Block settings**
   - Emit `## Block settings` as the section heading.
   - Scan the schema `settings` array for `"type": "header"` entries. Translate their `content` value (e.g. `t:general.headers.content` → "Content") and emit each as a `### <label>` subheading.
   - Collect all non-header settings that follow a header into a table under that `### subheading`.
   - Settings that appear **before** the first header (if any) go into a table with no `###` subheading, placed directly under `## Block settings`.
   - Each table has columns: Setting | Description | Options.
   - Translate every label/option using `locales/en.default.schema.json` when prefixed with `t:`.
   - Option formatting:
     - `select`/`radio`: one bullet per option using `•` and `<br>` separators inside the table cell, mark the default with `(default)`. If a "Visible when …" note applies, append it after the last bullet on its own line: `<br>_Visible when …_`.
     - `range`: `{min} – {max} {unit} (default: {default})`.
     - `checkbox`: `Checkbox (default: true/false)`.
     - Text inputs: `<type> input`.
     - `image_picker`, `color`, etc. use descriptive text ("Image picker", "Color picker").
   - Note conditional visibility with "Visible when …".

   Example output structure:
   ```markdown
   ## Block settings

   ### Content

   | Setting | Description | Options |
   |---------|-------------|---------|
   | Text    | …           | …       |

   ### Spacing

   | Setting | Description | Options |
   |---------|-------------|---------|
   | …       | …           | …       |
   ```


## Translation lookup

- `t:blocks.rich_text` → look up `blocks.rich_text` key path inside `locales/en.default.schema.json`.
- For nested keys, follow the dot path (e.g., `t:general.settings.font_size.label`).
- Category example: `t:general.categories.3_navigation` → look up `general.categories.3_navigation`.


## Batch mode

When asked to document all blocks changed on the current branch (e.g. "update docs for all changed blocks"):

1. Run the following in the slab repo root to discover changed block files:
   ```
   git diff --name-only main...HEAD -- 'blocks/*.liquid'
   ```
2. For each file in the resulting list, apply the full content generation logic (all sections above) to produce `slab/blocks/{category-folder}/{title-slug}.md`.
3. Write all generated files into the cloned `BrickspaceLab/docs` repo under `slab/blocks/` using category subfolders.
4. Stage every changed file, then commit once:
   ```
   docs(slab): update block docs for {source-branch}
   ```
5. Push and open a single PR (or update the existing PR for `docs/slab-{source-branch}`) using:
   ```
   gh pr create --repo BrickspaceLab/docs --base main \
     --title "docs(slab): update block docs for {source-branch}" \
     --body "Updates documentation for blocks changed in \`{source-branch}\`: {comma-separated list of handles}."
   ```


## References

- [Schema standards](mdc:.cursor/rules/schemas.mdc)
- [Localization](mdc:.cursor/rules/localization.mdc)
