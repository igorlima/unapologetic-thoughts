#!/usr/bin/env python3
"""Extract podcast feeds from an RSS XML file and optionally download episodes."""

from __future__ import annotations

import argparse
from datetime import datetime
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "yt-dlp" / "podcast"
EXAMPLE_FEED_URL = "https://feeds.megaphone.fm/ADL5417720568"

# import pdb
# pdb.set_trace()

# Silence curl stderr:
#  curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" 2>/dev/null | awk ...
#  curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" -o "other/$(date +%Y-%m-%d) headspace-podcast-feed.xml"

# curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" | tr '\n' ' ' | grep -oE "xmlUrl=('([^']*)'|\"([^\"]*)\")" | sed -E "s/^xmlUrl=['\"](.*)['\"]$/\1/" | awk '!seen[$0]++'
# curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" | tr '\n' ' ' | grep -oE "enclosure url=('([^']*)'|\"([^\"]*)\")" | sed -E "s/^enclosure url=['\"](.*)['\"]$/\1/"


@dataclass
class PodcastFeed:
    title: str
    description: str
    publication_date: str
    url: str


def parse_xml_root(root: ET.Element) -> list[PodcastFeed]:
    """Return unique podcast feeds from an RSS XML root."""

    feeds: list[PodcastFeed] = []
    seen: set[str] = set()

    for channel_item in root.findall(".//item"):
        xml_url = channel_item.find('enclosure').attrib.get("url") if channel_item.find('enclosure') is not None else None
        if not xml_url:
            continue
        if xml_url in seen:
            continue
        seen.add(xml_url)

        title = channel_item.find('title').text
        pub_date = channel_item.find('pubDate').text if channel_item.find('pubDate') is not None else None
        description = channel_item.find('description').text if channel_item.find('description') is not None else ""
        feeds.append(PodcastFeed(
            title=title.strip(),
            url=xml_url.strip(),
            publication_date=pub_date.strip() if pub_date else None,
            description=description.strip(),
        ))
    return feeds


def parse_xml_source(xml_source: str) -> list[PodcastFeed]:
    """Parse RSS XML from either a local file path or an http(s) URL."""
    parsed = urllib.parse.urlparse(xml_source)

    if parsed.scheme in {"http", "https"}:
        try:
            xml_bytes = fetch_bytes(xml_source)
        except urllib.error.URLError as exc:
            raise ValueError(f"could not fetch RSS XML URL {xml_source}: {exc}") from exc
        try:
            root = ET.fromstring(xml_bytes)
        except ET.ParseError as exc:
            raise ValueError(f"invalid RSS XML from URL: {exc}") from exc
        return parse_xml_root(root)

    if parsed.scheme == "file":
        xml_source = urllib.request.url2pathname(parsed.path)

    xml_path = Path(xml_source)
    if not xml_path.exists():
        raise ValueError(f"RSS XML file not found: {xml_path}")
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as exc:
        raise ValueError(f"invalid RSS XML: {exc}") from exc
    return parse_xml_root(tree.getroot())


def sanitize_filename(name: str) -> str:
    """Create a filesystem-safe filename."""
    cleaned = re.sub(r"[^A-Za-z0-9._ -]+", "", name).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    if not cleaned:
        return "podcast"
    return cleaned[:120]


def publication_date_to_filename_prefix(publication_date: str | None) -> str:
    if not publication_date:
        return "unknown-date"
    try:
        return datetime.strptime(publication_date, "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d")
    except ValueError:
        return "unknown-date"


def download_file(url: str, output_path: Path) -> None:
    """Download a URL to the given output path."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, output_path.open("wb") as out:
        while True:
            chunk = response.read(1024 * 64)
            if not chunk:
                break
            out.write(chunk)


def fetch_bytes(url: str) -> bytes:
    with urllib.request.urlopen(url) as response:
        return response.read()


def print_feeds(
    feeds: Iterable[PodcastFeed],
    start_episode: int | None = None,
    end_episode: int | None = None,
) -> None:
    feed_list = list(feeds)
    total = len(feed_list)
    start = start_episode if start_episode is not None else 1
    end = end_episode if end_episode is not None else total
    print("Extracted podcast feeds:")
    for i, feed in enumerate(feed_list[start - 1:end], start=start):
        print(f"{i}.")
        print(f"   Title: {feed.title}")
        print(f"   Published: {feed.publication_date}" if feed.publication_date else "   Publication date: N/A")
        print(f"   Description: {feed.description}" if feed.description else "   Description: N/A")
        print(f"   URL: {feed.url}")
        print("\n")
    print(f"Printed episodes {start} to {end}: {end - start + 1} of {total} feeds.")


def prompt_yes_no(prompt: str) -> bool:
    value = input(prompt).strip().lower()
    return value in {"y", "yes"}


def choose_feed_index(max_index: int) -> int | None:
    try:
        raw = input(f"Select a feed number to download (1-{max_index}): ").strip()
    except EOFError:
        return None

    if not raw.isdigit():
        return None

    value = int(raw)
    if value < 1 or value > max_index:
        return None
    return value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Extract podcast feed URLs from an RSS XML file and optionally download "
            "the episode from a selected feed."
        ),
        epilog=(
            "Example podcast feed URL to read RSS episodes:\n"
            f"  {EXAMPLE_FEED_URL}"
        ),
    )
    parser.add_argument(
        "xml_source",
        help="RSS XML source: local file path or http(s) URL",
    )
    parser.add_argument(
        "--download",
        action="store_true",
        help="Download episode from one selected feed",
    )
    parser.add_argument(
        "--feed-index",
        type=int,
        default=None,
        help="1-based feed index to download (used with --download)",
    )
    parser.add_argument(
        "--start-episode",
        type=int,
        default=1,
        help="Start episode number (1-based) to display",
    )
    parser.add_argument(
        "--end-episode",
        type=int,
        default=10,
        help="End episode number (1-based) to display",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output directory for downloads (default: {DEFAULT_OUTPUT_DIR})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        feeds = parse_xml_source(args.xml_source)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if not feeds:
        print("No podcast feed URLs found in RSS XML file.")
        return 0

    print_feeds(
        feeds,
        start_episode=args.start_episode,
        end_episode=args.end_episode,
    )
    # print(f"\nExample podcast feed URL: {EXAMPLE_FEED_URL}")

    should_download = args.download
    selected_index = args.feed_index

    if not should_download:
        try:
            should_download = prompt_yes_no("\nDownload a podcast episode now? [y/N]: ")
        except EOFError:
            should_download = False

    if not should_download:
        return 0

    if selected_index is None:
        selected_index = choose_feed_index(len(feeds))

    if selected_index is None or not (1 <= selected_index <= len(feeds)):
        print("Error: provide a valid --feed-index or choose a valid feed number.", file=sys.stderr)
        return 1

    feed = feeds[selected_index - 1]
    print(f"\nFetching feed: {feed.title}")

    ext = Path(urllib.parse.urlparse(feed.url).path).suffix or ".mp3"
    date_prefix = publication_date_to_filename_prefix(feed.publication_date)
    filename = f"{date_prefix} {sanitize_filename(feed.title)}{ext}"
    output_path = args.output_dir / filename

    print(f"Downloading episode:\n  {feed.title}\n  {feed.url}\n  {output_path}")
    try:
        download_file(feed.url, output_path)
    except urllib.error.URLError as exc:
        print(f"Error downloading media URL: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error writing file: {exc}", file=sys.stderr)
        return 1

    print("Download complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
