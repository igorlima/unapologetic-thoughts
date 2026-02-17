#!/bin/bash
#!/usr/bin/env bash

# chmod +x scripts/cmus.sh
# ./scripts/cmus.sh
FOLDER=~/Downloads/yt-dlp/

# The command below lists all files in the current directory, extracts YouTube video IDs from filenames enclosed in square brackets, and excludes specific video IDs from the output.
# $> ls -1 | grep -Eo '\[[A-Za-z0-9_-]{11}\]' | grep -Eo '[A-Za-z0-9_-]{11}' | grep -v 'QfRYlpyzb30|Hid-ezc80Mk|bsr3o9ezw0A'
# • `ls -1` lists one entry per line
# • the option `-o` stands for "only matching". It prints only the non-empty parts of a matching line that match the pattern.
# • the option `-v` (or `--invert-match`), which inverts the match, showing non-matching lines.
#
# Commands to remove files with a specific extension interactively:
# $> rm -i -- *.webm.part
# $> find . -maxdepth 1 -name "*.webm.part" -print0 | xargs -0 -p -n1 rm -f
# $> rm -i -- ~/Downloads/yt-dlp/*.webm.part
# $> find ~/Downloads/yt-dlp/ -maxdepth 1 -name "*.webm.part" -print0 | xargs -0 -p -n1 rm -f
#
whatIsMissingInTheList() {
  # This function takes a list of YouTube video IDs as input, checks which of
  # those IDs are already downloaded (based on the filenames in the current
  # directory), and then outputs the wish list, the downloaded IDs, and the
  # missing IDs.
  LIST=$1
  RGX_OR=$(sed "s/ /|/g" <(echo $LIST))
  DOWNLOADED=$(ls -1 $FOLDER | grep -Eo '\[[A-Za-z0-9_-]{11}\]' | grep -Eo '[A-Za-z0-9_-]{11}' | grep -E $RGX_OR)
  RGX_OR_DOWNLOADED=$(echo -e $DOWNLOADED | tr ' ' '|' | sed 's/|$//')
  MISSING=$(echo $LIST | tr ' ' '\n' | grep -v -E '('"$RGX_OR_DOWNLOADED"')' | tr '\n' ' ')
  echo "WISH LIST : $LIST"
  echo "DOWNLOADED: $(echo $DOWNLOADED | tr '\n' ' ' | sed 's/|$//')"
  echo "MISSING   : $MISSING"
  # • tr: used to translate or delete characters. In this case, it is used to replace spaces with newlines and vice versa.
}
# whatIsMissingInTheList "QRqLg5Iq4bA L3joz294TVw YxqKvFtWZKc LrRmAQx5TVw Y9mRoCerrpY dp1qULxCIGg --h6buReAvw"
# exit

# for VIDEO_ID in Riub5ycByCY e2wBXUEz_sQ; do
for VIDEO_ID in QRqLg5Iq4bA L3joz294TVw LrRmAQx5TVw Y9mRoCerrpY; do
  LINK="https://www.youtube.com/watch?v=$VIDEO_ID"
  yt-dlp --js node --cookies-from-browser chrome --extract-audio --audio-format mp3 "$LINK" -P ${FOLDER}
done

# UPDATE yt-dlp:
# pip3 install --no-cache --upgrade-strategy eager -I yt-dlp
# DOWNLOAD the audio in mp3 format:
# (VIDEO_ID=E42TfodDzUk && yt-dlp --js node --remote-components ejs:npm --cookies-from-browser chrome --extract-audio --audio-format mp3 "https://www.youtube.com/watch?v=$VIDEO_ID" -P ~/Downloads/yt-dlp/)
# DOWNLOAD the video in mp4 format (instead of audio only):
# (VIDEO_ID=rBdhqBGqiMc && yt-dlp --js node --remote-components ejs:github --cookies-from-browser chrome -t mp4 "https://www.youtube.com/watch?v=$VIDEO_ID" -P ~/Downloads/)
