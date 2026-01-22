# UP - the Ultimate Plumber

The tool `up` helps interactively and incrementally explore textual data, by making it easier to quickly build complex pipelines. It boosts any typical text-processing utils such as `grep`, `sort`, `cut`, `paste`, `awk`, `wc`, `perl`, etc etc, by providing a quick, interactive, scrollable preview of their results.

For slowly trickling input, use `ctrl-s` **(pause)** and `ctrl-q` **(unpause)**. Observe indicator in top-left corner:
- tilde `~` indicates _"still reading"_
- hash `#` indicates _"paused/frozen"_ **(with `ctrl-s`; unfreese with `ctrl-q`)**
- space ` ` indicates _"all input read, got EOF"_

```sh
# macOS install
brew install up
```

## Usage

```sh
echo 'This is my 1st index.1.2.md file' | grep -w "index" | awk '{ print $5 }' | sed 's/.[0-9]//g'

echo 'This is my 1st index.1.2.md file' | up
```

## Reference

- https://terminaltrove.com/up
- https://github.com/akavel/up
