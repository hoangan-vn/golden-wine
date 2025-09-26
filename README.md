# Golden Wine Shopify Theme

This repository contains the Golden Wine storefront theme for Shopify. It is a customizable, production-ready theme using Shopify Online Store 2.0 features (sections everywhere, JSON templates, app blocks, and internationalization).

## Highlights

- Modern Shopify theme structure (`layout/`, `sections/`, `snippets/`, `templates/`, `assets/`, `locales/`)
- Multi-language support via JSON files in `locales/`
- Ready for local development with Shopify CLI (`shopify theme dev`)
- CI-friendly (includes GitHub workflow for theme preview deployments)

## Quick Start

### 1. Install Shopify CLI and authenticate

```bash
shopify version
shopify auth login --store <your-store>.myshopify.com
```

### 2. Run local dev server

```bash
shopify theme dev --store <your-store>.myshopify.com
```

### 3. Push changes to your store (Draft theme)

```bash
shopify theme push --store <your-store>.myshopify.com
```

See `GUIDE.md` for full setup, workflow, and troubleshooting.

## Repository Layout

- `layout/` – Theme wrappers and entry templates
- `sections/` – Page sections used across templates
- `snippets/` – Reusable Liquid partials
- `templates/` – JSON templates for pages, products, collections, etc.
- `assets/` – Theme JS, CSS, images, and static assets
- `locales/` – Translation files
- `config/` – Theme settings schema and data

## Requirements

- Shopify CLI v3+
- A Shopify store with a staff or collaborator account
- Optional: GitHub Actions (see `.github/workflows/theme-preview.yml`)

## Development Scripts

For convenience on Unix-like shells, use:

```bash
./scripts/dev.sh help
```

This wrapper provides shortcuts for `dev`, `push`, `pull`, `check`, and `package`.

## License

Proprietary. All rights reserved by Golden Wine.
