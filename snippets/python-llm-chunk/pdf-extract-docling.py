# PDF EXTRACT via docling
# It download a detection model - it needs to wait at the first run
# And this may take several minutes depending upon the network connection.

from docling.document_converter import DocumentConverter
from pprint import pprint
import pathlib, os, asyncio
import pudb; # pu.db

# docling github
# • Get your documents ready for gen AI
#   - https://github.com/DS4SD/docling
#   - https://pypi.org/project/docling/
#   - https://ds4sd.github.io/docling/
#   - https://github.com/DS4SD/docling/issues/136
#
# Improved RAG Document Processing With Markdown
# • How to read and convert PDFs to Markdown for better RAG results with LLMs
#  - https://towardsdatascience.com/improved-rag-document-processing-with-markdown-426a2e0dd82b


"""
# pip3 show docling
# pip3 index versions docling | grep -E "[(][0-9]+([.][0-9]+)+[)]"
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I docling==2.14.0
# pip3 install git+https://github.com/DS4SD/docling

# pyenv local 3.10.6
python3.10 -m venv my-test-env-2024a12m28d
source my-test-env-2024a12m28d/bin/activate
pip3 install docling==2.14.0
pip3 install pudb
"""

source = "data/input.pdf"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
md_text = result.document.export_to_markdown()
print(md_text)  # output: "## Docling Technical Report[...]"
# save markdown to file
pathlib.Path("data/output-docling-pdf.md").write_text(md_text)
print("Markdown saved to output-docling-pdf.md")


"""
HOW TO RUN THIS SCRIPT:

({
python3 pdf-extract-docling.py
})
"""
