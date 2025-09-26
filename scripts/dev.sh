#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

STORE="${SHOPIFY_STORE:-}"
THEME_ID="${SHOPIFY_THEME_ID:-}"

usage() {
  cat <<'USAGE'
Usage: scripts/dev.sh <command> [options]

Commands:
  dev [--store <store>]          Start local development server
  push [--theme <id>] [--unpublished]  Push current theme to store
  pull [--theme <id>]            Pull remote theme into local directory
  list                           List themes on the configured store
  check                          Run Shopify theme checks/validation
  package                        Bundle theme into a zip archive
  help                           Show this help

Environment variables:
  SHOPIFY_STORE       Default store (e.g., my-shop.myshopify.com)
  SHOPIFY_THEME_ID    Default theme ID for push/pull
USAGE
}

require_shopify() {
  if ! command -v shopify >/dev/null 2>&1; then
    echo "Error: Shopify CLI not found. Install from https://shopify.dev/docs/api/shopify-cli" >&2
    exit 1
  fi
}

cmd="$1" || { usage; exit 1; }
shift || true

require_shopify

case "$cmd" in
  dev)
    EXTRA_ARGS=("$@")
    if [[ -n "$STORE" ]]; then
      shopify theme dev --store "$STORE" "${EXTRA_ARGS[@]}"
    else
      shopify theme dev "${EXTRA_ARGS[@]}"
    fi
    ;;

  push)
    EXTRA_ARGS=()
    THEME="$THEME_ID"
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --theme)
          THEME="$2"; shift 2 ;;
        --unpublished)
          EXTRA_ARGS+=("--unpublished"); shift ;;
        --store)
          STORE="$2"; shift 2 ;;
        *) EXTRA_ARGS+=("$1"); shift ;;
      esac
    done
    if [[ -n "$STORE" ]]; then EXTRA_ARGS+=(--store "$STORE"); fi
    if [[ -n "$THEME" ]]; then EXTRA_ARGS+=(--theme "$THEME"); fi
    shopify theme push "${EXTRA_ARGS[@]}"
    ;;

  pull)
    EXTRA_ARGS=()
    THEME="$THEME_ID"
    while [[ $# -gt 0 ]]; do
      case "$1" in
        --theme)
          THEME="$2"; shift 2 ;;
        --store)
          STORE="$2"; shift 2 ;;
        *) EXTRA_ARGS+=("$1"); shift ;;
      esac
    done
    if [[ -n "$STORE" ]]; then EXTRA_ARGS+=(--store "$STORE"); fi
    if [[ -n "$THEME" ]]; then EXTRA_ARGS+=(--theme "$THEME"); fi
    shopify theme pull "${EXTRA_ARGS[@]}"
    ;;

  list)
    if [[ -n "$STORE" ]]; then
      shopify theme list --store "$STORE"
    else
      shopify theme list
    fi
    ;;

  check)
    shopify theme check
    ;;

  package)
    OUT_DIR="$REPO_ROOT/dist"
    mkdir -p "$OUT_DIR"
    TS="$(date +%Y%m%d-%H%M%S)"
    ZIP_NAME="golden-wine-theme-$TS.zip"
    # Exclude git, node_modules, dist, tmp, and dotfiles often not needed
    zip -r "$OUT_DIR/$ZIP_NAME" . \
      -x "**/.git/**" "**/node_modules/**" "dist/**" "**/.DS_Store" "**/.idea/**" "**/.vscode/**"
    echo "Packaged: $OUT_DIR/$ZIP_NAME"
    ;;

  help|--help|-h|*)
    usage
    ;;
esac
