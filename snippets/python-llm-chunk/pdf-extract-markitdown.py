# PDF EXTRACT via markitdown
from markitdown import MarkItDown
from openai import OpenAI
from pprint import pprint
import pathlib, os
import pudb; # pu.db

# MarkItDown github
# • Python tool for converting files and office documents to Markdown.
#   - https://github.com/microsoft/markitdown
#
# MarkItDown: Microsoft’s Game-Changing Tool That Turns Any Document into Clean Markdown
# • A deep dive into Microsoft’s new Python library that seamlessly converts PDFs, Office files, and more into clean, version-control-friendly Markdown
#   - https://levelup.gitconnected.com/markitdown-microsofts-game-changing-tool-that-turns-any-document-into-clean-markdown-c0edc82f4c08

"""
# pip3 show markitdown
# pip3 index versions markitdown | grep -E "[(][0-9]+([.][0-9]+)+[)]"
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I markitdown==0.0.1a3

python3 -m venv my-test-env-2024a12m28d
source my-test-env-2024a12m28d/bin/activate
pip3 install markitdown==0.0.1a3
pip3 install openai==1.58.1
pip3 install pudb
"""

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
  api_key=GEMINI_API_KEY,
  base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# https://ai.google.dev/gemini-api/docs/models/gemini
md = MarkItDown(llm_client=client, llm_model="gemini-2.0-flash-exp")
# https://github.com/microsoft/markitdown/pull/139
result = md.convert("data/input.pdf")
md_text = result.text_content
print(md_text)
pathlib.Path("data/output-markitdown-pdf.md").write_text(md_text)
print("Markdown saved to output-markitdown-pdf.md")

# to use LLM for image descriptions, provide `llm_client` and `llm_model`
result = md.convert("data/input.png")
md_text = result.text_content
print(md_text)
pathlib.Path("data/output-markitdown-png.md").write_bytes(md_text.encode())
print("Markdown saved to output-markitdown-png.md")

"""
# BATCH PROCESSING MULTIPLE FILES
# Convert multiple files to markdown format in a single run
supported_extensions = ('.pptx', '.docx', '.pdf', '.jpg', '.jpeg', '.png')
files_to_convert = [f for f in os.listdir('.') if f.lower().endswith(supported_extensions)]
for file in files_to_convert:
  print(f"\nConverting {file}...")
  try:
    md_file = os.path.splitext(file)[0] + '.md'
    result = md.convert(file)
    md_text = result.text_content
    with open(md_file, 'w') as f:
      f.write(md_text)
    
    print(f"Successfully converted {file} to {md_file}")
  except Exception as e:
    print(f"Error converting {file}: {str(e)}")
"""



"""
HOW TO RUN THIS SCRIPT:

({
export GEMINI_API_KEY="XXXXXXXXXXXXXXXXXXXX"
python3 pdf-extract-markitdown.py
})
"""
