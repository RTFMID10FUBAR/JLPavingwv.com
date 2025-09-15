#!/usr/bin/env bash
set -euo pipefail

mkdir -p assets/images/{hero,gallery,misc}

# Move a couple into hero manually (pick best truck/paving shots)
mv images/109076003_733786294064175_6877898834608841159_n.jpg assets/images/hero/hero-truck.jpg
mv images/110301342_733786354064169_815007763370855060_n.jpg assets/images/hero/hero-paving.jpg

# Auto-move the rest into gallery with sequential renaming
i=1
for img in images/*.jpg; do
  new="assets/images/gallery/gallery-$(printf '%02d' $i).jpg"
  mv "$img" "$new"
  ((i++))
done

# Clean up old dir
rmdir images || true

echo "✅ Images organized into assets/images/{hero,gallery,misc}"
