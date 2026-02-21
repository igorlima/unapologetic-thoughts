#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./extract-rss-podcast-feeds.sh [url]
#   ./extract-rss-podcast-feeds.sh --episodes [count] [url]
#   ./extract-rss-podcast-feeds.sh --selector "xmlUrl" [url]
#   ./extract-rss-podcast-feeds.sh --selector "enclosure url" [url]
#
# Default mode:
#   Outputs one URL per line based on URL_SELECTOR.
#   URL_SELECTOR can be:
#     - Single attribute: "xmlUrl"
#     - Tag + attribute: "enclosure url"
#
# Episodes mode:
#   Prints the latest N episodes (title, publication date, description) from an RSS feed.
#   If the input is XML, the first xmlUrl feed is used.

SOURCE_URL="https://feeds.megaphone.fm/ADL5417720568"
MODE="feeds"
EPISODE_COUNT=10
URL_SELECTOR="${URL_SELECTOR:-xmlUrl}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --episodes)
      MODE="episodes"
      if [[ "${2:-}" =~ ^[0-9]+$ ]]; then
        EPISODE_COUNT="$2"
        shift 2
      else
        shift 1
      fi
      ;;
    --selector)
      if [[ -z "${2:-}" ]]; then
        echo "Missing value for --selector" >&2
        exit 1
      fi
      URL_SELECTOR="$2"
      shift 2
      ;;
    *)
      SOURCE_URL="$1"
      shift 1
      ;;
  esac
done

# Silence curl stderr:
#  curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" 2>/dev/null | awk ...
#  curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" -o "other/$(date +%Y-%m-%d) headspace-podcast-feed.xml"

# curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" | tr '\n' ' ' | grep -oE "xmlUrl=('([^']*)'|\"([^\"]*)\")" | sed -E "s/^xmlUrl=['\"](.*)['\"]$/\1/" | awk '!seen[$0]++'
# curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" | tr '\n' ' ' | grep -oE "enclosure url=('([^']*)'|\"([^\"]*)\")" | sed -E "s/^enclosure url=['\"](.*)['\"]$/\1/"

curl -fsSL $SOURCE_URL \
  | awk -v max=$EPISODE_COUNT '
  BEGIN { RS="</item>"; ORS=""; n=0 }
  $0 ~ /<item[ >]/ {
    s = $0
    gsub(/\n/, " ", s)

    item_start = index(s, "<item")
    if (!item_start) next
    s = substr(s, item_start)

    title = pub = url = ""

    if (match(s, /<title>[^<]*<\/title>/)) {
      title = substr(s, RSTART, RLENGTH)
      sub(/^<title>/, "", title)
      sub(/<\/title>$/, "", title)
    }
    if (match(s, /<pubDate>[^<]*<\/pubDate>/)) {
      pub = substr(s, RSTART, RLENGTH)
      sub(/^<pubDate>/, "", pub)
      sub(/<\/pubDate>$/, "", pub)
    }
    if (match(s, /<enclosure[^>]*url=["'\''"][^"'\''"]+["'\''"]/)) {
      u = substr(s, RSTART, RLENGTH)
      sub(/^.*url=["'\''"]/, "", u)
      sub(/["'\''"]$/, "", u)
      url = u
    }

    if (url != "" && n < max) {
      n++
      printf "Episode %d\nTitle: %s\nPublished: %s\nURL: %s\n\n", n, title, pub, url
      # if (n >= max) exit
    }
  }'

echo '
to download episodes:
  curl -fL "PASTE_URL_HERE" -o ~/Downloads/yt-dlp/podcast/"$(basename "${URL%%\?*}")"
  curl -fL "PASTE_URL_HERE" -o ~/Downloads/yt-dlp/podcast/episode.mp3
  curl -fL "PASTE_URL_HERE" -o ~/Downloads/yt-dlp/podcast/$(date +%Ya%mm%dd-%Hh%Mm%Ss).mp3
'
