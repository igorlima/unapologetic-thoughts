"""
SNIPPET
Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed.
- https://markdown-it-py.readthedocs.io/en/latest/
- https://github.com/executablebooks/markdown-it-py
- https://github.com/markdown-it/markdown-it/blob/d2782d892a51201b25d3eeab172201ad5a53a24c/README.md
"""

"""
# mkdir $(date +%Ya%mm%dd-%Hh%M%S)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
python3 -m venv tmp-env
source tmp-env/bin/activate
#
# pip3 show markdown-it-py
# pip3 index versions markdown-it-py
# pip3 list
#
pip3 install markdown-it-py==4.0.0
pip3 install linkify-it-py==2.0.3
pip3 install mdit-py-plugins==0.5.0
"""

from markdown_it import MarkdownIt
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin
from pprint import pprint

md = (
  MarkdownIt('commonmark', {'breaks':True,'html':True})
  .use(front_matter_plugin)
  .use(footnote_plugin)
  .enable('table')
)
text = ("""
---
a: 1
---

a | b
- | -
1 | 2

A footnote [^1]

[^1]: some details
""")
tokens = md.parse(text)
html_text = md.render(text)
print(tokens)
print(html_text)

# FIND ALL THE ACTIVE PARSING RULES: all the parsing configuration options enabled
# pprint(md.get_active_rules())
# FIND ALL THE PARSING RULES
# pprint(md.get_all_rules())

# CREATING A SYNTAX TREE
# in some use cases it may be useful to convert the token stream into a syntax
# tree, with opening/closing tokens collapsed into a single token that contains
# children.
from markdown_it.tree import SyntaxTreeNode
node = SyntaxTreeNode(tokens)
print(node.pretty(indent=2, show_text=True))
pprint(node.children)

## To export the html to a file, uncomment the lines below:
# from pathlib import Path
# Path("output.html").write_text(html_text)

"""
REFERENCE:
• Markdown parser done right. Fast and easy to extend.
  - https://github.com/markdown-it/markdown-it/blob/d2782d892a51201b25d3eeab172201ad5a53a24c/README.md
• Usage:
  - https://markdown-it-py.readthedocs.io/en/latest/using.html

```sh
# RUN this file by:
python3 markdown-parser.py

# RENDER markdown to HTML with markdown-it-py from the command-line
# type ctrl-d to complete input, or ctrl-c to exit.
markdown-it
# in batch
markdown-it README.md README.footer.md > index.html
```
"""
