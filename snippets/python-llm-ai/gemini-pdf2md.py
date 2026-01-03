# How I use Gemini on my PDF files using Python
"""
# mkdir $(date +%Ya%mm%dd-%Hh%Mm)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

python3 -m venv my-test-env-2026a01m02d
source my-test-env-2026a01m02d/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
pip3 install pudb
pip3 install -U google-genai==1.56.0
pip3 install -U xml2epub==2.6.10
pip3 install -U markdown==3.10
pip3 install --upgrade --force-reinstall google-genai
pip3 install --no-cache --upgrade-strategy eager -I google-genai==1.56.0
pip3 list
pip3 show google-genai
pip3 index versions google-genai
"""

import argparse
parser = argparse.ArgumentParser(
  description="""
  A script to convert PDF files to markdown and then to EPUB using Google Gemini API.
  If the markdown file already exists, it will be reused to generate the EPUB.
  """
)
parser.add_argument(
  "-i", "--input-file",
  type=str,
  required=True,
  help="The path to the input file."
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
import pudb;

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

if not MD_FILEPATH.exists():
  PROMPT = """
  Convert the following PDF page to markdown.
  Return only the markdown with no explanation text. Do not include deliminators like '''markdown.

  RULES:
  - You MUST include all information on the page. Do NOT exclude headers, footers, or subtext.
  - Charts & infographics must be interpreted to a markdown format
  - Non text based images must be replaced with [Description of image](image.png)
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

HOW TO RUN THIS SCRIPT:
python3 gemini-pdf2md.py --help
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
"""

