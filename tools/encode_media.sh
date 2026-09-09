#!/usr/bin/env bash
# One-shot media pipeline: explainer MP4s -> small web MP4s + posters; site GIFs -> MP4; photos -> resized JPEG/PNG.
set -euo pipefail
FF=/opt/homebrew/bin/ffmpeg
SRC="/Users/rafa/Claude_projects/scietific figures/LiB_operation"
HERE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$HERE/assets/video"; RAW="$HERE/tools/raw"; IMG="$HERE/assets/img"
mkdir -p "$OUT/posters"
for n in lib_battery lis_battery rdf_explainer edl_explainer md_explainer dft_explainer tddft_explainer; do
  $FF -y -loglevel error -i "$SRC/$n.mp4" -an \
    -vf "scale=1080:-2:flags=lanczos,format=yuv420p" \
    -c:v libx264 -preset slow -crf 27 -tune animation -profile:v high -level 4.0 \
    -g 60 -movflags +faststart "$OUT/$n.mp4"
  $FF -y -loglevel error -ss 2 -i "$OUT/$n.mp4" -frames:v 1 -q:v 3 "$OUT/posters/$n.jpg"
done
for g in lis_speciation cei_reaxff edl_negative edl_positive; do
  $FF -y -loglevel error -i "$RAW/$g.gif" -an \
    -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2,format=yuv420p" \
    -c:v libx264 -preset slow -crf 30 -movflags +faststart "$OUT/$g.mp4"
  $FF -y -loglevel error -ss 1 -i "$OUT/$g.mp4" -frames:v 1 -q:v 3 "$OUT/posters/$g.jpg"
done
# stills
magick "$RAW/headshot.jpg" -auto-orient -resize 800x800\> -strip -quality 85 "$IMG/headshot.jpg"
for t in hardcarbon edl lis cei; do magick "$RAW/${t}_thumb.png" -resize 900x900\> -strip -quality 85 "$IMG/research/${t}_thumb.jpg"; done
magick "$RAW/hardcarbon_anneal.png" -resize 1400x1400\> -strip "$IMG/research/hardcarbon_anneal.png"
for k in 3 4 5 6 7 8 9; do magick "$RAW/outreach_$k.jpg" -auto-orient -resize 1400x1400\> -strip -quality 82 "$IMG/outreach/outreach_$k.jpg"; done
magick "$RAW/group_photo_a.jpg" -resize 1400x1400\> -strip -quality 82 "$IMG/groups/group_photo_a.jpg"
magick "$RAW/group_photo_b.png" -resize 1400x1400\> -strip -quality 82 "$IMG/groups/group_photo_b.jpg"
magick "$RAW/toney_logo.png" -resize 600x600\> -strip "$IMG/groups/toney_logo.png"
magick "$RAW/rdi_logo.png" -resize 600x600\> -strip "$IMG/groups/rdi_logo.png"
echo done
