# GETTING STARTED WITH CHONKIE
#
# Text Chunking for RAG Systems with Chonkie
# 
# Chonkie is a lightweight Python library designed to facilitate efficient text
# chunking, a critical component in RAG applications. It provides a suite of
# chunking methods, each optimized for specific use cases, ensuring developers
# have the tools necessary to process text data effectively.
#
# Reference:
# - https://github.com/chonkie-ai/chonkie
# - https://docs.chonkie.ai/getting-started/introduction
# - https://generativeai.pub/text-chunking-for-rag-systems-with-chonkie-d609d0eef55c

"""
# pip3 show chonkie
# pip3 index versions chonkie | grep -E "[(][0-9]+([.][0-9]+)+[)]"
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I chonkie==0.4.1

rm -rf my-test-env-2025a01m18d
python3 -m venv my-test-env-2025a01m18d 
source my-test-env-2025a01m18d/bin/activate
pip3 install chonkie==0.4.1
pip3 install numpy==2.2.1
pip3 install tokenizers==0.21.0
pip3 install pudb
"""

# PDF Document Processing: Chonkie processed a 200-page PDF in
# under 30 seconds, compared to 3 minutes for spaCy and NLTK.
#
# Large-Scale Text Corpus: Chonkie processed over 100,000 lines of
# text in under 3 minutes, while other libraries took over 5
# minutes.

from chonkie import TokenChunker

# Import your favorite tokenizer library
# Also supports AutoTokenizers, TikToken and AutoTikTokenizer
from tokenizers import Tokenizer
tokenizer = Tokenizer.from_pretrained("gpt2")
# Initialize the chunker
chunker = TokenChunker(tokenizer)
# Chunk some text
chunks = chunker("Woah! Chonkie, the chunking library is so cool! I love the tiny hippo hehe.")
# Access chunks
for chunk in chunks:
  print(f"Chunk:  {chunk.text}")
  print(f"Tokens:  {chunk.token_count}")
