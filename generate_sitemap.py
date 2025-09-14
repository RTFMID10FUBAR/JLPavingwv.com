#!/usr/bin/env python3

import os
from urllib.parse import urljoin
from datetime import datetime

# CONFIG — change these as needed
SITE_DIR = "site_org"
BASE_URL = "https://jlpavingwv.com/"   # <-- your live domain, with trailing slash
SITEMAP_FILE = os.path.join(SITE_DIR, "sitemap.xml")

def get_html_files(root):
    html_files = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.lower().endswith(".html"):
                # skip sitemap itself if re-run
                if fname.lower() == "sitemap.xml":
                    continue
                fullpath = os.path.join(dirpath, fname)
                # compute URL path
                rel_path = os.path.relpath(fullpath, root)
                html_files.append(rel_path.replace(os.path.sep, "/"))
    return html_files

def generate_sitemap():
    html_files = get_html_files(SITE_DIR)
    now_iso = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    lines.append('<?xml version="1.0" encoding="UTF-8"?>')
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    
    for rel in sorted(html_files):
        # handle index.html at root
        if rel == "index.html":
            url = BASE_URL
        else:
            url = urljoin(BASE_URL, rel)
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
