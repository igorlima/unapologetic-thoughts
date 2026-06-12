#!/usr/bin/env python3
"""Script to convert a Markdown file to EPUB format."""

# How I convert Markdown files to EPUB using Python
"""
See requirements to set up a virtual environment and install the necessary packages:
- `./requirements/md2epub.requirements.txt`
"""

import argparse
parser = argparse.ArgumentParser(
  description=("""
  A script to convert a Markdown file to EPUB format.
  Chapters are split by horizontal rules (5 or more dashes on their own line).
  """
  ),
  epilog=("""
  Example usage:
  python3 md2epub.py --input-file ./notes.md --output ./output/
  """
  ),
)
parser.add_argument(
  "-i", "--input-file",
  type=str,
  required=True,
  help="The path to the input markdown file."
)
parser.add_argument(
  "-o", "--output",
  type=str,
  required=True,
  help="The output folder where the EPUB file will be saved."
)
args = parser.parse_args()
print(f"Input File: {args.input_file}")
print(f"Output Folder: {args.output}")


import pathlib

MD_FILEPATH = pathlib.Path(args.input_file)
if not MD_FILEPATH.exists():
  print(f"ERROR: File not found: {MD_FILEPATH}")
  exit(1)
if not MD_FILEPATH.is_file():
  print(f"ERROR: Not a file: {MD_FILEPATH}")
  exit(1)

FILENAME = MD_FILEPATH.stem
OUTPUT_FOLDER_PATH = pathlib.Path(args.output)

if not OUTPUT_FOLDER_PATH.exists():
  OUTPUT_FOLDER_PATH.mkdir(parents=True, exist_ok=True)

with open(MD_FILEPATH, 'r', encoding='utf-8') as file:
  MARKDOWN_TEXT = file.read()
print(f"Markdown file loaded: {MD_FILEPATH}")


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
  title = FILENAME,
  output_directory = OUTPUT_FOLDER_PATH,
  filename = FILENAME,
)



"""
REFERENCE:
  Convert a Markdown file to EPUB:
    - https://pypi.org/project/xml2epub/
    - https://pypi.org/project/xml2epub/#basic-usage
    - https://pypi.org/project/Markdown/
    - https://python-markdown.github.io/reference/
    - https://python-markdown.github.io/extensions/
    - https://python-markdown.github.io/extensions/fenced_code_blocks/
    - https://python-markdown.github.io/extensions/tables/

HOW TO RUN THIS SCRIPT:
python3 md2epub.py --help
python3 md2epub.py --input-file ./notes.md --output ./output/
({
python3 md2epub.py -i ./notes.md -o ./output/
python3 md2epub.py --input-file="./data/sample.md" --output="./output/"
})

OTHER scripts:
- batch converts PDFs in a folder, saving outputs to a directory
  - `../cli-and-tui/scripts/reading.batch-convert-pdf2md2epub.sh`
- PDF to markdown (via Gemini) and then to EPUB
  - `./gemini-pdf2md.py`
"""
