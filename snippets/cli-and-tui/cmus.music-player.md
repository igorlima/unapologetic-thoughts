# Audio 

## cmus - music player

cmus is a small, fast and powerful console music player for Unix-like operating systems.

- reference:
  - https://cmus.github.io/
  - https://github.com/cmus/cmus
  - https://man.archlinux.org/man/extra/cmus/cmus-tutorial.7.en

### cmus usage

Press *5* to switch to the file-browser view
Press *c* to pause/unpause
Press right/left to seek by 10 seconds
  Press h/l to seek by 10 seconds
Press *<*/*>* seek by one minute
  Press *,*/*.* seek by one minute
Seek
  :seek [+-](<num>[mh] | [HH:]MM:SS)


type *:q* and press Enter to quit
Press *q* to quit

Press *7* for a quick overview of the current keybindings and settings.
  To change a setting or keybind, just select it (up/down keys) and press enter.
  to custom the seek, search for "seek" and change it
  to search, press */*

t      toggle show_remaining_time
u      update browser/playlist library

:seek
seek [+-](<num>[mh] | [HH:]MM:SS)
	Seeks to an absolute or relative position, which can be given in
	seconds, minutes (m), hours (h) or HH:MM:SS format where HH: is
	optional.
:seek -1m
	Seek 1 minute backward
:seek +5
	Seek 5 seconds forward
:seek 1h
	Seek to absolute position 1h
:seek +1:30
	Seek 90 seconds forward

#### cmus playlist editing

To play a playlist in cmus, press `3` to open the playlist view, navigate to
your desired playlist using the arrow keys, and press `Enter` to start
playback. If the playlist is empty, you can add songs from the library view
(press `1`) by highlighting them and pressing `y`. 

Key Playlist Controls:
- 3: Switch to Playlist View.
- Enter: Play the selected song/playlist.
- c: Pause/Unpause.
- b: Next track.
- z: Previous track.
- s: Toggle shuffle.
- Shift + C: Toggle continue (plays through the playlist).
- r: Toggle repeat.
- D: Remove selected song from the playlist. 

Playlist Management Commands:
`:save <filename>.pls`: Save current playlist.
`:load <filename>.pls`: Load a playlist.
`:clear`: Clear the current playlist. 

To SEARCH your library in the `cmus` console music player:
- Enter Search Mode: Press the `/` key to enter search mode.
  - You will see a `/` prompt appear at the bottom of the screen.
- Type Your Query: Type the artist name, album name, or track title you are looking for and press `Enter`.
  - `cmus` will search for tracks that match all the words in your query.
- Navigate Results:
  - Press `n` to jump to the next match.
  - Press `N` (`shift` + `n`) to jump to the previous match. 

#### cmus track Management

- a      copy tracks to the library (1-2)
- y      copy tracks to the playlist (3)
- e      append tracks to the play queue (4)
- E      prepend tracks to the play queue (4)

- p / P  if there are no marked tracks then the selected track is moved down (p) or up (P).
         move tracks works on queue view (4)
- D      press D or delete to remove marked or selected tracks in the current view (1-4).

Selecting Tracks
  Mark selected track by pressing SPACE.
  Marked tracks appear with a gray background.
  You can only mark tracks in the list views (2-4)

Clear playlist
  `vi ~/.cmus/playlists/default`

Queue view
   to save: `save -q filename`
   to edit: `vi ~/.cmus/vi ~/.cmus/vi ~/.cmus/queue.pl`
   to save queue on exit: `:set resume=true`

Status Line
Pressing m, o, M, C, r and s keys should make it easier to understand what all those fields mean.

b      player-next
c      player-pause
x      player-play
z      player-prev
v      player-stop
-      -----------------
t      toggle show_remaining_time
C      toggle continue

### Install cmus

```sh
# OS X
# https://cmus.github.io/#documentation
brew install cmus
```

## Podcast

### castero

- commands
  - h           - show this help screen
  - q           - exit the client
  - a           - add a feed
  - d           - delete the selected feed
  - r           - reload/refresh feeds
  - s           - save episode for offline playback

```bash
# run
castero
# help
castero --help
# import OPML file
castero --import other/podcast-list.opml
```

- reference:
  - about castero:
    - https://github.com/xgi/castero
    - https://terminaltrove.com/castero/

### podliner

```bash
# run
~/bin/podliner --version
~/bin/podliner --help
# import OPML file
~/bin/podliner --opml-import other/podcast-list.opml
# install macOS
bash <(curl -fsSL https://github.com/timkicker/podliner/releases/latest/download/install-macos.sh)
```

- reference
  - about podliner:
    - https://github.com/timkicker/podliner
    - https://terminaltrove.com/podliner/

### podcast feed

```bash
./scripts/extract-rss-podcast-feeds.py --help
./scripts/extract-rss-podcast-feeds.py https://feeds.megaphone.fm/ADL5417720568 --end-episode 5
./scripts/extract-rss-podcast-feeds.py "other/2026-02-20 headspace-podcast-feed.xml" --end-episode 5
./scripts/extract-rss-podcast-feeds.sh --episodes 3 --selector "enclosure url" "https://feeds.megaphone.fm/ADL5417720568"

# extract the podcast feed and save it to a file
curl -fsSL "https://feeds.megaphone.fm/ADL5417720568" -o "other/$(date +%Y-%m-%d) headspace-podcast-feed.xml"
```

- Radio Headspace
  - https://feeds.megaphone.fm/ADL5417720568
    - https://www.headspace.com/podcasts
    - https://cms.megaphone.fm/channel/ADL5417720568

## How-to session

### How to set up yt-dlp to download audio from YouTube

```sh
python3 -m venv my-env
source my-env/bin/activate

pip3 install yt-dlp
```

```sh
mkdir -p ~/Downloads/yt-dlp
cd ~/Downloads/yt-dlp

python3 -m venv my-env
source my-env/bin/activate
# pip3 show yt-dlp
# pip3 index versions yt-dlp
# pip3 install -U yt-dlp==2026.1.31
# pip3 install --upgrade --force-reinstall yt-dlp

pip3 install --no-cache --upgrade-strategy eager -I yt-dlp==2026.1.31
```

```sh
cat << EOF > script.sh
#!/bin/bash
#!/usr/bin/env bash

# chmod +x script.sh

for VIDEO_ID in Riub5ycByCY e2wBXUEz_sQ; do
  LINK="https://www.youtube.com/watch?v=$VIDEO_ID"
  yt-dlp --js node --cookies-from-browser chrome --extract-audio --audio-format mp3 "$LINK" -P ~/Downloads/yt-dlp/
done
EOF

chmod +x script.sh
```

### How to use yt-dlp to download video from YouTube

```sh
( VIDEO_ID=rBdhqBGqiMc && \
  yt-dlp --js node \
  --remote-components ejs:github \
  --cookies-from-browser chrome \
  -t mp4 \
  "https://www.youtube.com/watch?v=$VIDEO_ID" -P ~/Downloads/ \
)
```

- Other references:
  - Instagram downloader:
    - https://snapinsta.to/en2
    - https://fastdl.app/en2


## Other

```tmux
# <ctrl-a>q to see the tmux pane numbers
:swap-pane -s unapologetic:audio.2 -t unapologetic:audio.1
:resize-pane -x 50% -y 50% -t unapologetic:audio.1
:resize-pane -x 50% -y 50% -t unapologetic:audio.2
```

```sh
# cmus is already listening on socket
# kill -9 "$(pidof cmus)"
# pkill -9 cmus
# https://github.com/cmus/cmus/issues/306
ps ax | grep cmus
sudo kill -9 PID
```
