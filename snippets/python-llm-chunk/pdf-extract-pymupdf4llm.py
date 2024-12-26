# PDF EXTRACT via pymupdf4llm
import pymupdf4llm
import pathlib
from pprint import pprint
import pudb; # pu.db

# PDF EXTRACT via pymupdf4llm
# Why PyMuPDF4LLM is the Best Tool for Extracting Data from PDFs (Even if You Didn’t Know You Needed It)
# https://python.plainenglish.io/why-pymupdf4llm-is-the-best-tool-for-extracting-data-from-pdfs-even-if-you-didnt-know-you-needed-7bff75313691

"""
# pip3 show pymupdf4llm
# pip3 index versions pymupdf4llm | grep -E "[(][0-9]+([.][0-9]+)+[)]"
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I pymupdf4llm==0.0.17

python3 -m venv my-test-env-2024a12m25d
source my-test-env-2024a12m25d/bin/activate
pip3 install pymupdf4llm==0.0.17
pip3 install pudb
"""

# EXTRACT PDF CONTENT AS MARKDOWN
md_text = pymupdf4llm.to_markdown("data/input.pdf")
print(md_text[:500])  # print first 500 characters

# EXTRACT ONLY PAGES 2 AND 3
md_text = pymupdf4llm.to_markdown("data/input.pdf", pages=[2, 3])
print(md_text[:500])  # print first 500 characters

# SAVING MARKDOWN TO A FILE
md_text = pymupdf4llm.to_markdown("data/input.pdf")
pathlib.Path("data/output.md").write_bytes(md_text.encode())
print("Markdown saved to output.md")

'''
# extracting data as llamaindex documents
llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data("data/input.pdf")
print(f"Number of LlamaIndex documents: {len(llama_docs)}")
print(f"Content of first document: {llama_docs[0].text[:500]}")
'''

# IMAGE EXTRACTION
md_text_images = pymupdf4llm.to_markdown(doc="data/input.pdf",
                                         pages=[1, 10],
                                         page_chunks=True,
                                         write_images=True,
                                         image_path="data/images",
                                         image_format="jpg",
                                         dpi=200)
print(md_text_images[0]['images']) # print image information from the first chunk

# CHUNKING WITH METADATA
md_text_chunks = pymupdf4llm.to_markdown(doc="data/input.pdf",
                                         pages=[0, 1, 2],
                                         page_chunks=True)
print(md_text_chunks[0])  # print the first chunk

# WORD-BY-WORD EXTRACTION
md_text_words = pymupdf4llm.to_markdown(doc="data/input.pdf",
                                        pages=[1,2],
                                        page_chunks=True,
                                        write_images=True,
                                        image_path="data/images",
                                        image_format="jpg",
                                        dpi=200,
                                        extract_words=True)
print(md_text_words[0]['words'][:5])  # print the first 5 words from the first chunk

# TABLE EXTRACTION
md_text_tables = pymupdf4llm.to_markdown(doc="data/input.pdf",
                                         pages=[10],  # specify pages containing tables
                                         )
print(md_text_tables)

"""
HOW TO RUN THIS SCRIPT:

({
python3 pdf-extract-pymupdf4llm.py
})
"""
