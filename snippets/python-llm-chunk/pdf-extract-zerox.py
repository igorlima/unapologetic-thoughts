# PDF EXTRACT via zerox
from pyzerox import zerox
from pprint import pprint
import pathlib, os, asyncio
import pudb; # pu.db

import litellm
# # https://github.com/BerriAI/litellm/blob/11932d0576a073d83f38a418cbdf6b2d8d4ff46f/litellm/litellm_core_utils/get_llm_provider_logic.py#L322
litellm.suppress_debug_info = True
# https://docs.litellm.ai/docs/debugging/local_debugging#set-verbose
litellm.set_verbose=False
# https://docs.python.org/3/library/logging.html#logging-levels
# https://github.com/BerriAI/litellm/blob/ea8f0913c2aac4a7b4ec53585cfe9ea04a3282de/litellm/_logging.py#L11
os.environ['LITELLM_LOG'] = 'CRITICAL'

# zerox github
# • PDF to Markdown with vision models
#   - https://github.com/getomni-ai/zerox
#   - https://www.libhunt.com/r/zerox
#   - https://getomni.ai/ocr-demo
#
# Improved RAG Document Processing With Markdown
# • How to read and convert PDFs to Markdown for better RAG results with LLMs
#  - https://towardsdatascience.com/improved-rag-document-processing-with-markdown-426a2e0dd82b


"""
# pip3 show py-zerox
# pip3 index versions py-zerox | grep -E "[(][0-9]+([.][0-9]+)+[)]"
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I py-zerox==0.0.7

python3 -m venv my-test-env-2024a12m28d
source my-test-env-2024a12m28d/bin/activate
pip3 install py-zerox==0.0.7
pip3 install pudb
"""

## placeholder for additional model kwargs which might be required for some models
kwargs = {}
## system prompt to use for the vision model
custom_system_prompt = None
# to override
# custom_system_prompt = "For the below pdf page, do something..something..." ## example

# https://ai.google.dev/gemini-api/docs/models/gemini
model = "gemini/gemini-1.5-flash-8b"
model = "gemini/gemini-1.5-flash"
model = "gemini/gemini-2.0-flash-exp"

# Define main async entrypoint
async def main():
  file_path = "data/input.pdf" ## local filepath and file URL supported
  ## process only some pages or all
  select_pages = None ## None for all, but could be int or list(int) page numbers (1 indexed)
  output_dir = "./data" ## directory to save the consolidated markdown file
  output_dir = None
  result = await zerox(file_path=file_path, model=model, output_dir=output_dir,
                       custom_system_prompt=custom_system_prompt,select_pages=select_pages, **kwargs)
  return result

# run the main function:
result = asyncio.run(main())
md_text = "\n".join([page.content for page in result.pages])

# print markdown md_text
print(md_text)
# save markdown to file
pathlib.Path("data/output-zerox-pdf.md").write_text(md_text)
print("Markdown saved to output-zerox-pdf.md")




"""
HOW TO RUN THIS SCRIPT:

({
export GEMINI_API_KEY="XXXXXXXXXXXXXXXXXXXX"
export LITELLM_LOG=CRITICAL
python3 pdf-extract-zerox.py
})
"""
