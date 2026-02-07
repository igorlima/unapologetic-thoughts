#!/bin/bash
#!/usr/bin/env bash

# chmod +x script.sh


# The command below lists all files in the current directory, extracts YouTube video IDs from filenames enclosed in square brackets, and excludes specific video IDs from the output.
# $> ls -1 | grep -Eo '\[[A-Za-z0-9_-]{11}\]' | grep -Eo '[A-Za-z0-9_-]{11}' | grep -v 'QfRYlpyzb30|Hid-ezc80Mk|bsr3o9ezw0A'
# • `ls -1` lists one entry per line
# • the option `-o` stands for "only matching". It prints only the non-empty parts of a matching line that match the pattern.
# • the option `-v` (or `--invert-match`), which inverts the match, showing non-matching lines.

for VIDEO_ID in Riub5ycByCY e2wBXUEz_sQ; do
  LINK="https://www.youtube.com/watch?v=$VIDEO_ID"
  yt-dlp --js node --cookies-from-browser chrome --extract-audio --audio-format mp3 "$LINK" -P ~/Downloads/yt-dlp/
done

# pip3 install --no-cache --upgrade-strategy eager -I yt-dlp
# (VIDEO_ID=E42TfodDzUk && yt-dlp --js node --remote-components ejs:npm --cookies-from-browser chrome --extract-audio --audio-format mp3 "https://www.youtube.com/watch?v=$VIDEO_ID" -P ~/Downloads/yt-dlp/)
