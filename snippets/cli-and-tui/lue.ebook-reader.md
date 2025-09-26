# LUE

A TUI ebook reader with Text-to-Speech (TTS).

Terminal eBook Reader with Text-to-Speech.

## Usage

### Basic Commands

```bash
# start with default tts
lue path/to/your/book.epub
lue ~/Downloads/kindle-shared-reading.md

# launch without arguments to open the last book you were reading
lue

# use specific tts model (edge/kokoro/none) 
lue --tts kokoro path/to/your/book.epub

# use a specific voice (full list at voices.md)
lue --voice "en-US-AriaNeural" path/to/your/book.epub

# set the speech speed (e.g., 1.5x)
lue --speed 1.5 path/to/your/book.epub

# specify a language code if needed
lue --lang a path/to/your/book.epub

# seconds of overlap between sentences
lue --over 0.2 path/to/your/book.epub

# enable pdf cleaning filter (removes page numbers, headers and footnotes, default: 10% (0.1) from both bottom and top of the page)
lue --filter path/to/your/book.pdf

# set custom pdf filter margins (0.0-1.0, where 0.1 = 10% of page)
lue --filter 0.15 path/to/your/book.pdf          # Both margins to 15%
lue --filter 0.12 0.20 path/to/your/book.pdf     # Header 12%, footnote 20%

# practice using lue with the navigation guide
lue --guide

# view available options
lue --help
```

### Keyboard Controls

| **Key Binding**                         | **Action Description**                                                                         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `q`                                     | Quit the application and save current reading progress automatically                           |
| `p`                                     | Pause or resume the text-to-speech audio playback                                              |
| `a`                                     | Toggle auto-scroll mode to automatically advance during TTS playback                           |
| `t`                                     | Select and highlight the top sentence of the current visible page                              |
| `h` / `l`                               | Move the reading line to the previous or next paragraph in the document                        |
| `j` / `k`                               | Move the reading line to the previous or next sentence in the document                         |
| `i` / `m`                               | Jump up or down by full pages for rapid navigation through longer documents                    |
| `u` / `n`                               | Scroll up or down by smaller increments for fine-grained position control                      |
| `y` / `b`                               | Jump directly to the beginning or end of the document for quick navigation                     |
| `,` / `.`                               | Decrease or increase text-to-speech playback speed (1x to 3x)                                  |
| `s` / `w`                               | Toggle sentence highlighting or word highlighting on/off                                       |

## Installation

```sh
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
# pip3 install git+https://github.com/superstarryeyes/lue.git@8ff13674376fce811b2b59dad92f9f6ab45ce67f
# pip3 install git+https://github.com/superstarryeyes/lue.git
pip3 install -U lue==0.1.0
pip3 install -U kokoro==0.9.4
pip3 install -U soundfile==0.13.1
pip3 install -U huggingface-hub==0.35.1
pip3 install -U torch==2.8.0
pip3 install -U torchvision==0.23.0
pip3 install -U torchaudio==2.8.0
pip3 install --upgrade --force-reinstall lue
pip3 list
pip3 show lue
pip3 index versions lue
```

### Dependencies

```sh
# Install FFmpeg (required for audio processing)
brew install ffmpeg
# Optional
#  `espeak` - Kokoro TTS support
#  `antiword` - .doc file support
brew install espeak antiword
```
