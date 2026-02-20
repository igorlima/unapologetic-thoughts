#!/usr/bin/env python3
"""Script to convert PDF files to markdown and then to EPUB using Google Gemini API."""

# How I use Gemini on my PDF files using Python
"""
See requirements to set up a virtual environment and install the necessary packages:
- `./requirements/gemini-pdf2md.requirements.txt`
"""

import argparse
parser = argparse.ArgumentParser(
  description=("""
  A script to convert PDF files to markdown and then to EPUB using Google Gemini API.
  If the markdown file already exists, it will be reused to generate the EPUB.
  """
  ),
  epilog=(
    "Before running the script, make sure to set your Gemini API key in the environment variable:\n"
    f'  export GEMINI_API_KEY="your_api_key_here"'
  ),
)
parser.add_argument(
  "-i", "--input-file",
  type=str,
  required=True,
  help="The path to the input file."
)
parser.add_argument(
  "-f", "--force-ai-extraction",
  action=argparse.BooleanOptionalAction,
  default=False,
  help="Force AI extraction even if markdown file exists."
)
parser.add_argument(
  "-o", "--output",
  type=str,
  required=True,
  help="The output folder where the markdown and EPUB file will be saved."
)
args = parser.parse_args()
print(f"Input File: {args.input_file}")
print(f"Output Folder: {args.output}")


# https://github.com/googleapis/python-genai
# https://ai.google.dev/gemini-api/docs/libraries
from google import genai
from google.genai import types
import pathlib
# import pudb; pu.db
# import pudb;

client = genai.Client()

# retrieve and encode the PDF byte
PDF_FILEPATH = pathlib.Path(args.input_file)
if not PDF_FILEPATH.exists():
  print(f"ERROR: File not found: {PDF_FILEPATH}")
  exit(1)
if not PDF_FILEPATH.is_file():
  print(f"ERROR: Not a file: {PDF_FILEPATH}")
  exit(1)

FILENAME = PDF_FILEPATH.stem
FILEEXT = PDF_FILEPATH.suffix
OUTPUT_FOLDER_PATH = pathlib.Path(args.output)
MD_FILEPATH = OUTPUT_FOLDER_PATH / pathlib.Path(FILENAME + '.md')

if not OUTPUT_FOLDER_PATH.exists():
  OUTPUT_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

if args.force_ai_extraction or not MD_FILEPATH.exists():
  PROMPT = """
  You will be given PDF file that you need to process in three steps: extract it in markdown format, organize it for better readability, and provide a summary.

  Your task has three parts:

  **Part 1: Extract to Markdown Format**
  Convert the PDF content into clean markdown format. Ensure that:
  - Text formatting is preserved (bold, italics, etc.)
  - Any special characters or symbols are properly rendered
  - The content is presented exactly as it appears in the PDF, but in markdown syntax and **structure in a readable way**

  **Part 2: Organize the Content**
  Take the markdown content and reorganize it for improved readability:
  - Identify and properly separate distinct paragraphs or sections
  - Make headings and subheadings stand out using appropriate markdown heading levels (## for main headings, ### for subheadings, etc.)
  - Correct any obvious formatting issues such as:
    - Line breaks that occur in the middle of sentences
    - Inconsistent spacing between sections
    - Improperly formatted text
  - Format lists and bullet points properly using markdown list syntax (-, or numbered lists)
  - Clearly delineate tables or figures from the main text using appropriate markdown table syntax or code blocks
  - Ensure logical flow and visual hierarchy in the document structure

  **Part 3: Summarize the Content**
  Create a concise summary that captures the essence of the text:
  - Identify and state the main topic or theme
  - Highlight the key points or arguments presented
  - Note any important data, statistics, or examples that support the main ideas
  - Capture the overall conclusion or message
  - Keep your summary concise, aiming for approximately 10-15% of the original text length
  - Ensure the summary is coherent and can stand alone as a brief overview

  **Output Format:**
  Present your complete response using the following structure:

  # Markdown PDF Content
  [Write the extracted PDF content in markdown format here]

  # Organized Context
  [Write your organized and reformatted version here]

  # Summary
  [Write your concise summary here]

  **Important reminders:**
  - Maintain the original meaning and intent of the text throughout all three parts
  - Respond in the same language as the provided PDF content
  - Do not add information that wasn't in the original content
  - Focus on clarity and readability in your organization
  """
  # https://ai.google.dev/gemini-api/docs/document-processing#python
  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(
          data=PDF_FILEPATH.read_bytes(),
          mime_type='application/pdf',
        ),
        PROMPT])
  MARKDOWN_TEXT = response.text
  # print(MARKDOWN_TEXT)
  with open(MD_FILEPATH, 'w', encoding='utf-8') as file:
    file.write(MARKDOWN_TEXT)
  print(f"Markdown file saved to: {MD_FILEPATH}")
else:
  print(f"Reusing existing markdown file: {MD_FILEPATH}")
  with open(MD_FILEPATH, 'r', encoding='utf-8') as file:
    MARKDOWN_TEXT = file.read()


import re
import markdown
import xml2epub

# https://github.com/Python-Markdown/markdown
# https://pypi.org/project/Markdown/
# https://python-markdown.github.io/reference/
# https://python-markdown.github.io/extensions/
# https://python-markdown.github.io/extensions/tables/
# https://python-markdown.github.io/changelog/#the-tables-extension-now-uses-a-style-attribute-instead-of-an-align-attribute-for-alignment
# https://python-markdown.github.io/reference/markdown/extensions/tables/#markdown.extensions.tables
def convert_markdown_to_html(html_text, extensions=[]):
  print("converting markdown to html...")
  output = markdown.markdown(html_text, extensions=extensions)
  print("converted md to html.")
  return output

def split_markdown_in_chapters(md_text):
  # to test Regex
  # - https://pythex.org/
  # - https://regex101.com/
  #
  # python regex split multiline
  # https://stackoverflow.com/questions/13871893/python-regex-split-multiline-inclusive-of-pattern
  #
  # split text into chapters
  chapters = re.split(r'^-{5,}$', md_text, flags=re.MULTILINE)
  # remove leading and trailing whitespaces
  chapters = [c.strip() for c in chapters]
  # remove empty chapter
  # https://sparkbyexamples.com/python/python-remove-empty-strings-from-list/
  chapters = [c for c in chapters if c]
  return chapters

def generate_epub(html_text='', title=None, output_directory=None, filename=None, chapters=None):
  # Basic Usage of xml2epub
  # https://pypi.org/project/xml2epub/#basic-usage
  book = xml2epub.Epub(title, creator="Igor Lima", publisher="Journaling, notes, and ideas...", toc_location="beginning")
  if chapters:
    for chapter_num, chapter_text in enumerate(chapters):
      chapter = xml2epub.create_chapter_from_string(chapter_text, title=f"Chapter {chapter_num+1}")
      book.add_chapter(chapter)
  else:
    chapter = xml2epub.create_chapter_from_string(html_text)
    book.add_chapter(chapter)
  book.create_epub(output_directory, filename)

generate_epub(
  chapters = [
    convert_markdown_to_html(chapter_text, extensions=['fenced_code', 'tables'])
      for chapter_text in split_markdown_in_chapters(MARKDOWN_TEXT)
  ],
  title = 'Code Sample',
  # output_directory = '/tmp/'
  output_directory = OUTPUT_FOLDER_PATH,
  filename = FILENAME,
)



"""
REFERENCE:
  How I use Gemini on my PDF files using Python
    https://medium.com/@woyera/how-i-use-gemini-on-my-pdf-files-using-python-50f4eaba4f0b
  Gemini API Documentation
    https://ai.google.dev/gemini-api/docs/
  Migrate to the Google GenAI SDK
    https://ai.google.dev/gemini-api/docs/migrate
  Convert a PDF to Markdown Online: everything happens right in your browser
    https://www.pdftomarkdown.co/
    https://pdf2md.morethan.io/
  Convert a Markdown file to EPUB: 
    - https://workflowy.com/#/1f4d050fae3d
    $> brew install pandoc
    $> pandoc -s -r markdown index.md -o index.epub
    $> pandoc -s -r markdown index.md -o index.epub --metadata title="My Book Title" --metadata author="Author Name"
    # to specifically claim the README.md is in Github-Flavored Markdown:
    $> pandoc -s -r gfm README.md -o README.epub
    $> pandoc --from=gfm --to=epub -o README.md README.epub
  A terminal EPUB Book Reader
    https://github.com/bugzmanov/bookokrat
    https://terminaltrove.com/bookokrat/
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ GLOBAL COMMANDS                                                             │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ q        Quit application                                                   │
     │ Tab      Switch focus between library/TOC and content panels                │
     │ Esc      Clear selection/search or dismiss popups                           │
     │ Ctrl+z   Toggle zen mode (hide sidebar/status bar)                          │
     │ ?        Show help screen                                                   │
     │ Space+t  Open theme selector                                                │
     │ + / -    Increase/decrease content margins                                  │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ NAVIGATION (Vim-style)                                                      │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ j/k               Move down/up (works in all lists and reader)              │
     │ h/l               Collapse/expand in TOC; previous/next chapter in reader   │
     │ Ctrl+d / Ctrl+u   Scroll half-page down/up                                  │
     │ gg                Jump to top                                               │
     │ G                 Jump to bottom                                            │
     │ Ctrl+o / Ctrl+i   Jump backward/forward in history                          │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ SEARCH                                                                      │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ /         Start search (filter in library/TOC; search in reader)            │
     │ n / N     Jump to next/previous match                                       │
     │ Space+f   Reopen last book-wide search                                      │
     │ Space+F   Start fresh book-wide search                                      │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ LIBRARY & TOC PANEL                                                         │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ Enter   Open highlighted book or heading                                    │
     │ h / l   Collapse/expand entry                                               │
     │ H / L   Collapse/expand all                                                 │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ READER PANEL                                                                │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ h / l                 Previous/next chapter                                 │
     │ Space+s               Toggle raw HTML view                                  │
     │ Space+c               Copy entire chapter                                   │
     │ Space+z               Copy debug transcript                                 │
     │ c or Ctrl+C           Copy selection                                        │
     │ p                     Toggle profiler overlay                               │
     │ n                     Toggle normal mode                                    │
     │                       (Vim motions, visual selection, yanking)              │
     │ v / V (normal mode)   Enter visual character/line selection;                │
     │                       y to yank, Esc to exit                                │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ COMMENTS & ANNOTATIONS                                                      │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ a         Create or edit comment on selection                               │
     │ d         Delete comment under cursor                                       │
     │ Space+a   Open comments/annotations viewer                                  │
     │ dd        Delete highlighted comment (in comments viewer)                   │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ POPUPS & EXTERNAL ACTIONS                                                   │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ Space+h   Toggle reading history popup                                      │
     │ Space+d   Show book statistics popup                                        │
     │ Space+a   Open comments/annotations viewer                                  │
     │ Space+o   Open current book in OS viewer                                    │
     │ Enter     Open image popup (when on image) or activate popup selection      │
     └─────────────────────────────────────────────────────────────────────────────┘

  GITHUB CLI
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ LIST OF PRS INVOLVING ME                                                    │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ PAGER=less gh pr view 13992                                                 │
     │   view PR using a pager                                                     │
     │ gh search prs --state=open --involves=@me                                   │
     │   list of prs involving me                                                  │
     │ gh pr list -S "state:open type:pr in:name IPM"                              │
     │   search by PR title                                                        │
     │ gh pr list -S "is:open type:pr involves:@me"                                │
     │   looking for things related to me                                          │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ COMMANDS                                                                    │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ gh auth login                                                               │
     │ gh repo --help                                                              │
     │ gh pr view [<number> | <url> | <branch>] [flags]                            │
     │    -c, --comments   View pull request comments                              │
     │ gh pr list [flags]                                                          │
     │    https://cli.github.com/manual/gh_pr_list                                 │
     │    -a, --assignee <string>                                                  │
     │    -A, --author <string>                                                    │
     │    -L, --limit <int>                                                        │
     │    -S, --search <query>                                                     │
     │    -s, --state <string>                                                     │
     │      filter by state: {open|closed|merged|all}                              │
     └─────────────────────────────────────────────────────────────────────────────┘

  MARKDOWN VIEWER TERMINAL
     Terminal Markdown Viewer
     https://github.com/axiros/terminal_markdown_viewer
     $> mkdir -p ~/Downloads/terminal-reading/md
     $> vi ~/Downloads/terminal-reading/md/$(date +%Ya%mm%dd-%Hh%Mm%Ss).md
     ┌─────────────────────────────────────────────────────────────────────────────┐
     │ MDV CLI USAGE                                                               │
     ├─────────────────────────────────────────────────────────────────────────────┤
     │ mdv - << EOF                                                                │
     │ This is a longer text                                                       │
     │ that spans multiple lines.                                                  │
     │ It is being provided via a here-document.                                   │
     │ EOF                                                                         │
     │                                                                             │
     │ cat << EOF | mdv -                                                          │
     │ This is line one.                                                           │
     │ This is line two with a pattern.                                            │
     │ This is line three.                                                         │
     │ EOF                                                                         │
     └─────────────────────────────────────────────────────────────────────────────┘
     ┌────────────────────────────────────────────────────────────────────────────────────────┐
     │ GLOW                                                                                   │
     ├────────────────────────────────────────────────────────────────────────────────────────┤
     │ brew install glow                                                                      │
     │                                                                                        │
     │ glow README.md                                                                         │
     │ # to use pager                                                                         │
     │ glow -p README.md                                                                      │
     │ glow README.md -p                                                                      │
     │                                                                                        │
     │ glow 'http://wiki.ilima.xyz/index.md'                                                  │
     │ curl -X GET 'http://wiki.ilima.xyz/index.md' | glow -                                  │
     │ glow 'https://ilima-reading.s3.us-east-2.amazonaws.com/how-to-vim.md'                  │
     │ curl -X GET 'https://ilima-reading.s3.us-east-2.amazonaws.com/how-to-vim.md' | glow -  │
     │                                                                                        │
     │ glow - << EOF                                                                          │
     │ This is a longer text                                                                  │
     │ EOF                                                                                    │
     │                                                                                        │
     │ cat << EOF | glow -                                                                    │
     │ This is line one.                                                                      │
     │ EOF                                                                                    │
     └────────────────────────────────────────────────────────────────────────────────────────┘



HOW TO RUN THIS SCRIPT:
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
python3 gemini-pdf2md.py --help
python3 gemini-pdf2md.py --input-file="~/Downloads/terminal-reading/pdf/" --output="~/Downloads/terminal-reading/epub/"
python3 gemini-pdf2md.py --input-file ~/Downloads/terminal-reading/pdf/2026a01m05d.pdf --output ~/Downloads/terminal-reading/epub/
({
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
python3 gemini-pdf2md.py --input-file="./data/vision-pdf-test.pdf" --output="./output/"
})

GENERATE AN API KEY
Follow these steps:
- In Google AI Studio, click Get API key in the left navigation panel.
  - https://aistudio.google.com/
- On the next page, click Create API key.
  - https://aistudio.google.com/apikey
- Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.

# vi "$HOME/Library/Application Support/aichat/config.yaml"


```bash
# The script processes all PDF files in a specified folder by converting each
# to markdown format using the `gemini-pdf2md.py` script and saves the results
# in an output directory.
({
#!/bin/bash

PDF_DIR=~/Downloads/terminal-reading/pdf
OUTPUT_DIR=~/Downloads/terminal-reading/epub

for pdf_file in "$PDF_DIR"/*.pdf; do
  filename=$(basename "$pdf_file" .pdf)
  ./gemini-pdf2md.py -i "$pdf_file" -o "$OUTPUT_DIR"
  sleep 5  # waits 5 seconds before processing the next file
done
})
```
"""

