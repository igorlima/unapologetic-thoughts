# Discordo - Terminal Discord Client

A lightweight, secure, and feature-rich Discord terminal (TUI) client.

Download binary:
- https://github.com/ayn2op/discordo
- https://nightly.link/ayn2op/discordo/workflows/ci/main

## KEY BINDINGS

```toml
focus_guilds_tree = "Ctrl+R"
focus_messages_list = "Ctrl+T"
focus_message_input = "Ctrl+Space"
toggle_guilds_tree = "Ctrl+B"        # hide/show the guilds tree
quit = "Ctrl+C"

logout = "Ctrl+D"                    # log out and remove the authentication token from keyring.
                                     # requires re-login upon restart.
 
select_previous = "Rune[k]"
select_next = "Rune[j]"
select_first = "Rune[g]"
select_last = "Rune[G]"
select_current = "Enter"             # select the currently highlighted text-based channel or expand a guild or channel
``` 


## HOW TO DOWNLOAD DISCORDO ON MACOS

```sh
git clone https://github.com/ayn2op/discordo
cd discordo
sudo xcodebuild -license
go build .
```

```sh
uname -a
curl -L -X GET https://nightly.link/ayn2op/discordo/workflows/ci/main/discordo_macOS_ARM64.zip -o discordo.zip
unzip discordo.zip
# mkdir $(date +%Ya%mm%dd-%Hh%M%S)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
```

```sh 
# HOW TO RUN DISCORDO ON MACOS
./discordo -token "xxxxxxxxxxxxxxxxxxxxxxxx"
security add-generic-password -s discordo -a token -w "xxxxxxxxxxxxxxxxxxxxxxxx"
# setup config file
mkdir $HOME/.config/discordo
vi $HOME/.config/discordo/config.toml
# sample config file
# https://raw.githubusercontent.com/ayn2op/discordo/refs/heads/main/internal/config/config.toml
# https://github.com/ayn2op/discordo/blob/b3f9a2f6faff8ad008433cc07a65016cb08c478f/internal/config/config.toml
./discordo --config-path $HOME/.config/discordo/config.toml
./discordo --config-path $HOME/.config/discordo/config.toml --token "xxxxxxxxxxxxxxxxxxxxxxxx"
```

### RUNNING DISCORDO IN A DOCKER CONTAINER

```sh
# a docker for playing with new linux tools
# https://hub.docker.com/_/linux-x64
# $> docker image ls
#
# Automatically REMOVE THE CONTAINER when it exits
# $> mkdir -p ~/Downloads/temp
docker run \
  --name linux-discordo --rm \
  -it dockcross/linux-x64:latest bash
# dockcross/linux-x64:20250913-6ea98ba
# ...
# DETACH
# $> mkdir -p ~/Downloads/temp
docker run \
  --detach \
  --name linux-discordo \
  -it dockcross/linux-x64:latest bash
# dockcross/linux-x64:20250913-6ea98ba
# ...
docker exec -it linux-discordo bash
docker stop linux-discordo
docker start linux-discordo
docker rm linux-discordo
```

```sh
apt-get update --allow-unauthenticated --allow-insecure-repositories
apt-get upgrade --allow-unauthenticated --fix-missing
apt-get install -y curl wget git vim unzip libx11-dev

uname -a
curl -L -X GET https://nightly.link/ayn2op/discordo/workflows/ci/main/discordo_Linux_X64.zip -o discordo.zip
unzip discordo.zip

cat /root/.cache/discordo/logs.txt
./discordo --token "xxxxxxxxxxxxxxxxxxxxxxxx"
```

```sh
export TZ="America/Sao_Paulo"
export TZ="America/Los_Angeles"
```

## MANUALLY GET TOKEN

- https://github.com/terminal-discord/weechat-discord

With the discord app open in your browser:
1. Open Devtools (`ctrl+shift+i` or `cmd+opt+i`)
2. Navigate to the Network tab
3. View only WebSockets by clicking "WS" in the inspector bar
4. Reload the page and select the `gateway.discord.gg` connection
5. Navigate to the "Response" tab of the request
6. The first or second message should begin with `{"op":2,"d":{"token":"<your token here>"...`

## CONFIG FILE

- https://raw.githubusercontent.com/ayn2op/discordo/refs/heads/main/internal/config/config.toml 
- https://github.com/ayn2op/discordo/blob/b3f9a2f6faff8ad008433cc07a65016cb08c478f/internal/config/config.toml

```sh
mkdir $HOME/.config/discordo
vi $HOME/.config/discordo/config.toml
```

```toml
# Whether to enable mouse or not.
mouse = true
# The program to open when the `keys.message_input.editor` keymap is pressed. Set the value to `"default"` to use `$EDITOR`.
editor = "default"

# "default" (unknown), "online", "dnd", "idle", "invisible", "offline"
status = "default"

# Whether to parse and render markdown in messages or not.
markdown = true
hide_blocked_users = true
show_attachment_links = true

# Use autocomplete_limit = 0 to disable autocompleting mentions
# Note: tab completion will still work, but it won't show any list.
autocomplete_limit = 20

# The number of messages to fetch when a text-based channel is selected from guilds tree. The minimum and maximum value is 0 and 100, respectively.
messages_limit = 50

[timestamps]
enabled = true
# https://pkg.go.dev/time#Layout
format = "3:04PM"

[notifications]
enabled = true
# The duration of the sound. Set the value to `0` to use default duration. This is only supported on Unix and Windows.
duration = 0
[notifications.sound]
enabled = true
only_on_ping = true

# Global shortcuts
# Esc: Reset message selection or close the channel selection popup.
[keys]
focus_guilds_tree = "Ctrl+R"
focus_messages_list = "Ctrl+T"
focus_message_input = "Ctrl+Space"
# Hide/show the guilds tree.
toggle_guilds_tree = "Ctrl+B"
quit = "Ctrl+C"
# Log out and remove the authentication token from keyring.
# Requires re-login upon restart.
logout = "Ctrl+D"

# Only while focusing on the guilds tree
[keys.guilds_tree]
select_previous = "Rune[k]"
select_next = "Rune[j]"
select_first = "Rune[g]"
select_last = "Rune[G]"
# select_previous = "Up"
# select_next = "Down"
# select_first = "Home"
# select_last = "End"
# SELECT the currently highlighted text-based channel or expand a guild or channel.
select_current = "Enter"
yank_id = "Rune[i]"
collapse_parent_node = "Rune[-]"
move_to_parent_node = "Rune[p]"

# Only while focusing on sent messages
[keys.messages_list]
select_previous = "Rune[k]"
select_next = "Rune[j]"
select_first = "Rune[g]"
select_last = "Rune[G]"
# select_previous = "Up"
# select_next = "Down"
# select_first = "Home"
# select_last = "End"
# SELECT the message reference (reply) of the selected channel.
select_reply = "Rune[s]"
# Reply to the selected message.
reply = "Rune[r]"
# Reply (with mention) to the selected message.
reply_mention = "Rune[R]"
cancel = "Esc"
delete = "Rune[d]"
# Open the selected message's attachments or hyperlinks in the message
# using the default browser application.
open = "Rune[o]"
# Yank (copy) the selected message's content/url/id.
yank_content = "Rune[y]"
yank_url = "Rune[u]"
yank_id = "Rune[i]"

# Only while typing a message
# Alt+Enter: Insert a new line to the current text.
[keys.message_input]
# paste from clipboard (supports both text and images)
paste = "Ctrl+V"
send = "Enter"
# Remove existing text or cancel reply.
cancel = "Esc"
# Complete usernames when mentioning
tab_complete = "Tab"

open_editor = "Ctrl+E"
open_file_picker = "Ctrl+\\"

[keys.mentions_list]
up = "Ctrl+P"
down = "Ctrl+N"

# style = { foreground = "", background = "", attributes = "" or [""] }
[theme.title]
alignment = "left" # `"left"`, `"center"`, or `"right"`.

normal_style = { attributes = "dim" }
active_style = { foreground = "green", attributes = "bold" }

[theme.border]
enabled = true
padding = [0, 0, 1, 1] # [top, bottom, left, right]

normal_style = { attributes = "dim" }
active_style = { foreground = "green", attributes = "bold" }

# `"hidden"`, `"plain"`, `"round"`, `"thick"`, or `"double"`.
normal_set = "round"
active_set = "round"

[theme.guilds_tree]
auto_expand_folders = true
# Give tree-like shape
graphics = true
graphics_color = "default"

[theme.messages_list]
reply_indicator = ">"
forwarded_indicator = "<"

mention_style = { foreground = "blue" }
emoji_style = { foreground = "green" }
url_style = { foreground = "blue" }
attachment_style = { foreground = "yellow" }

[theme.mentions_list]
# Note: width and height are capped to the avaliable space
# Minimum width
# 0 = make the list as wide as possible
min_width = 20
# Maximum height
# 0 = make the list as tall as needed
max_height = 0
```
