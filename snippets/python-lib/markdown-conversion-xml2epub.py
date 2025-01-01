# CONVERT MARKDOWN TO EPUB
import xml2epub, markdown
import re
# https://github.com/Python-Markdown/markdown
# https://pypi.org/project/Markdown/
# https://python-markdown.github.io/reference/
# https://python-markdown.github.io/extensions/tables/
# https://python-markdown.github.io/changelog/#the-tables-extension-now-uses-a-style-attribute-instead-of-an-align-attribute-for-alignment
# https://python-markdown.github.io/reference/markdown/extensions/tables/#markdown.extensions.tables
from markdown.extensions.tables import TableExtension
import pudb; # pu.db

"""
# pip3 show xml2epub
# pip3 index versions xml2epub
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I xml2epub==2.6.6
# pip3 install git+https://github.com/igorlima/xml2epub.git@address-issue-40

python3 -m venv my-test-env-2025a01m01d
source my-test-env-2025a01m01d/bin/activate
pip3 install xml2epub==2.6.6
pip3 install standard-imghdr==3.13.0
pip3 install markdown==3.7
pip3 install importlib-metadata==8.5.0
pip3 install typing-extensions==4.12.2
pip3 install pudb
"""

def convert(html_text, extensions=[]):
  print("converting markdown to html...")
  output = markdown.markdown(html_text, extensions=extensions)
  print("converted md to html.")
  return output

def generate_html(html_text, filepath=None):
  with open(filepath, 'wb') as file:
    file.write(html_text.encode('utf-8'))
  print("html file generated.")


def generate_epub(html_text='', title=None, output_directory=None, filename=None, chapters=None):
  # Basic Usage of xml2epub
  # https://pypi.org/project/xml2epub/#basic-usage
  book = xml2epub.Epub(title, creator="Igor Lima", publisher="Nautilus Omnibus")
  if chapters:
    for chapter_num, chapter_text in enumerate(chapters):
      chapter = xml2epub.create_chapter_from_string(chapter_text, title=f"Chapter {chapter_num+1}", local=True)
      book.add_chapter(chapter)
  else:
    chapter = xml2epub.create_chapter_from_string(html_text, local=True)
    book.add_chapter(chapter)
  book.create_epub(output_directory, filename)

def split_markdown_in_chapters(md_text):
  # to test Regex
  # - https://pythex.org/
  # - https://regex101.com/
  #
  # python regex split multiline
  # https://stackoverflow.com/questions/13871893/python-regex-split-multiline-inclusive-of-pattern

  # split text into chapters
  chapters = re.split(r'^-{5,}$', md_text, flags=re.MULTILINE)
  # remove leading and trailing whitespaces
  chapters = [c.strip() for c in chapters]
  # remove empty chapter
  # https://sparkbyexamples.com/python/python-remove-empty-strings-from-list/
  chapters = [c for c in chapters if c]
  return chapters

# read markdown from file
MD_TEXT = open('./data/nautilus-omnibus.md', 'r').read()

generate_html(
  convert(MD_TEXT, extensions=['fenced_code', TableExtension(use_align_attribute=True)]),
  # filepath = '/tmp/code-sample.html'
  filepath = './data/nautilus-omnibus.html'
)
generate_epub(
  convert(MD_TEXT, extensions=['fenced_code', TableExtension(use_align_attribute=True)]),
  title = 'Daily Planner',
  # output_directory = '/tmp/'
  output_directory = './data/',
  filename = 'nautilus-omnibus'
)

generate_epub(
  chapters = [convert(chapter_text, extensions=['fenced_code', TableExtension(use_align_attribute=True)]) for chapter_text in split_markdown_in_chapters(MD_TEXT)],
  title = 'Daily Planner',
  # output_directory = '/tmp/'
  output_directory = './data/',
  filename = 'nautilus-omnibus-with-chapters',
)

"""
REFERENCE:
• Why You Need To Stop Using To-Do Lists and Use This to Manage Your Time Better
  - https://medium.com/change-your-mind/why-you-need-to-stop-using-to-do-lists-and-use-this-to-manage-your-time-better-4f6f6a4f6c91

```sh
# image conversion
# image to text
(INPUT_IMG="data/nautilus-omnibus-1.png" && echo -n "data:image/png;base64,$(cat $INPUT_IMG | base64 | tr -d '\r\n')" | pbcopy)
(INPUT_IMG="data/nautilus-omnibus-2.png" && echo -n "data:image/png;base64,$(cat $INPUT_IMG | base64 | tr -d '\r\n')" | pbcopy)
# generic version
(INPUT_IMG="" && echo -n "data:image/png;base64,$(cat $INPUT_IMG | base64 | tr -d '\r\n')" | pbcopy)
```
"""
