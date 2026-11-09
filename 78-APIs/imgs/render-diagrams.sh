#!/usr/bin/env bash
# Re-render every imgs/*.mmd to an SVG with the shared Mermaid configuration.
# Requires: npm install -g @mermaid-js/mermaid-cli
set -e
cd "$(dirname "$0")"
for f in imgs/*.mmd; do
  mmdc -i "$f" -o "${f%.mmd}.svg" -c mermaid-config.json -p puppeteer-config.json -b transparent
done
