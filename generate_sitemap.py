#!/usr/bin/env python3
import os
from urllib.parse import urljoin
from datetime import datetime, timezone

# CONFIG — always use repo root
SITE_DIR = os.path.dirname(__file__)
BASE_URL = "https://jlpavingwv.com/"   # your live domain, trailing slash
SITEMAP_FILE = os.path.join(SITE_DIR, "sitemap.xml")

def get_html_files(root):
    html_files = []
    for fname in os.listdir(root):
        if fname.lower().endswith(".html") and fname.lower() != "sitemap.xml":
            html_files.append(fname)
    return html_files

def generate_sitemap():
    html_files = get_html_files(SITE_DIR)
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for fname in sorted(html_files):
        if fname == "index.html":
            url = BASE_URL
        else:
            url = urljoin(BASE_URL, fname)
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now_iso}</lastmod>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append("    <priority>0.8</priority>")
        lines.append("  </url>")
    
    lines.append("</urlset>")

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Sitemap written to {SITEMAP_FILE}, total {len(html_files)} pages.")

if __name__ == "__main__":
    generate_sitemap()
