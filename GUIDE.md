# Developer Guide – Golden Wine Shopify Theme

This guide covers local setup, development workflow, deployment, and troubleshooting for the Golden Wine Shopify theme.

## 1. Prerequisites

- A Shopify store (development or live) where you have access
- Shopify CLI v3+ installed
  - macOS: `brew tap shopify/shopify && brew install shopify-cli`
  - Windows: Install from `https://shopify.dev/docs/api/shopify-cli#install` (Microsoft Store or MSI)
  - Verify: `shopify version`
- Git installed and access to this repository

Optional but recommended:

- Node.js 18+ if you plan to work with tooling in `assets/` (minifiers, bundlers, etc.)

## 2. Authentication

Login once for your store:

```bash
shopify auth login --store <your-store>.myshopify.com
```

You can list stores you’re authenticated against with:

```bash
shopify stores list
```

## 3. Environment Setup

No .env file is required for Liquid-only development. The Shopify CLI reads your auth session from the OS keychain.

If you want a default store to avoid repeating `--store`:

```bash
shopify config set store=<your-store>.myshopify.com
```

## 4. Local Development

From the repository root:

```bash
shopify theme dev
```

- Opens a local server and a preview URL
- Watches changes in `layout/`, `sections/`, `snippets/`, `templates/`, `assets/`, `locales/`, `config/`

If you prefer an explicit store flag:

```bash
shopify theme dev --store <your-store>.myshopify.com
```

## 5. Pushing and Pulling Theme Code

- Push current directory to a draft theme on your store:

```bash
shopify theme push --theme <THEME_ID_OR_NAME>
```

If omitted, CLI may prompt to create/select a theme. Use `--unpublished` to ensure a draft theme.

- Pull remote theme code into your local working directory:

```bash
shopify theme pull --theme <THEME_ID_OR_NAME>
```

List themes and find IDs:

```bash
shopify theme list
```

## 6. Recommended Workflow

1. Create or select a draft theme to avoid affecting live customers
2. Run local dev: `shopify theme dev`
3. Commit early and often in Git
4. Push to draft theme for stakeholder QA: `shopify theme push --unpublished`
5. After approval, publish via Admin or CLI:

```bash
shopify theme publish --theme <THEME_ID>
```

## 7. Scripts

Use helper script on macOS/Linux:

```bash
./scripts/dev.sh help
```

Commands: `dev`, `push`, `pull`, `list`, `check`, `package`.

On Windows PowerShell, run raw Shopify CLI equivalents shown above, or use Git Bash/WSL to run `scripts/dev.sh`.

## 8. Linting and Checks

The Shopify CLI provides a check command:

```bash
shopify theme check
```

This will run validations against Liquid and theme structure.

## 9. CI / Theme Preview

A GitHub workflow exists at `.github/workflows/theme-preview.yml` for preview deployments. It may require repository secrets (e.g., `SHOPIFY_STORE`, `SHOPIFY_CLI_AUTH_TOKEN`, `THEME_ID`). Consult your DevOps maintainer to configure secrets.

## 10. Troubleshooting

- Auth problems: Re-run `shopify auth logout` then `shopify auth login --store <store>`
- Missing permissions: Ensure your staff/collaborator account has Theme access
- Dev port blocked: Try `shopify theme dev --port 9292` or close conflicting processes
- Push blocked: Confirm you’re targeting a draft theme (`--unpublished`), or use a specific `--theme` ID
- Slow preview: Large assets in `assets/` may delay uploads; optimize images and minify CSS/JS where possible

## 11. Project Structure (recap)

- `layout/` — Base Liquid layouts
- `sections/` — Configurable sections
- `snippets/` — Reusable partials
- `templates/` — JSON/Liquid templates
- `assets/` — JS, CSS, images, static files
- `locales/` — Translations
- `config/` — Theme settings schema/data
