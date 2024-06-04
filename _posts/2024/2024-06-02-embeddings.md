---
layout: post
title: AI Embeddings - OpenAI, HuggingFace, SentenceTransformers
category: code-sample
---


This session idea was inspired by a blog post on Medium[^1].
You can find the original code on Github[^2] [^3] and Google Colab[^4].

One cool feature in the original Google Colab notebook[^4] is the ability to
build a similarity matrix, which lets you compare dot product scores for all
possible sentence combinations.

If you’re building an application and the relevant chunks aren’t picked up, try
changing the model[^1].

## Setup

```bash
python3 -m venv env-embedding
source env-embedding/bin/activate

# `-I`  ignore the installed packages, overwriting them.
# `-U`  upgrade all specified packages to the newest available version.

pip3 install -U langchain_openai==0.1.8 openai==1.30.5 langchain==0.2.1 langchain_community==0.2.1 sentence_transformers==3.0.0

pip3 install --upgrade --force-reinstall langchain_openai openai langchain langchain_community sentence_transformers

pip3 show langchain_openai openai langchain langchain_community sentence_transformers

pip3 index versions langchain_openai openai langchain langchain_community sentence_transformers
```

## Code Sample

<details markdown="block">
<summary><i><code>embeddings.py</code></i></summary>

```python
from pprint import pprint
# check the dimensionality of the returned vectors.
import numpy as np

sentences_A = [
  "Best travel neck pillow for long flights",
  "Lightweight backpack for hiking and travel",
  "Waterproof duffel bag for outdoor adventures",
  "Stainless steel cookware set for induction cooktops",
  "High-quality chef's knife set",
  "High-performance stand mixer for baking",
  "New releases in fiction literature",
  "Inspirational biographies and memoirs",
  "Top self-help books for personal growth",
]

sentences_B = [
  "I'm afraid of flights",
  "I like flying",
  "aerophobia",
  "Scary pictures of airplanes",
  "Do planes fear thunder?",
]

sentences = sentences_A

# OPENAI
from langchain_openai import OpenAIEmbeddings
openai_embedding = OpenAIEmbeddings()

# or

from openai import OpenAI
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
  text = text.replace("\n", " ")
  return client.embeddings.create(input = [text], model=model).data[0].embedding

_list = [get_embedding(s) for s in sentences]
# print(_list)
# check the dimensionality of the returned vectors.
pprint(np.array(_list).shape)
print('---')

# DIRECTLY FROM HUGGINGFACE
# https://docs.llamaindex.ai/en/stable/examples/embeddings/huggingface/
from langchain_community.embeddings import HuggingFaceEmbeddings
mpnet_embeddings = HuggingFaceEmbeddings(
  model_name="sentence-transformers/all-mpnet-base-v2",
)
print('---')

_list = [mpnet_embeddings.embed_query(s) for s in sentences]
# print(_list)
# check the dimensionality of the returned vectors.
pprint(np.array(_list).shape)
print('---')

# LOAD AS SENTENCETRANSFORMERS
from sentence_transformers import SentenceTransformer
gist_embedding = SentenceTransformer("avsolatorio/GIST-Embedding-v0")

_list = gist_embedding.encode(sentences, convert_to_tensor=True)
# print(_list)
# check the dimensionality of the returned vectors.
pprint(np.array(_list.cpu().numpy()).shape)
"""
TypeError: can't convert mps:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.
"""
print('---')
```

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 embeddings.py
```
</details>


---
{: data-content="footnotes"}

[^1]: [LangChain 101: Part 3b. Talking to Documents: Embeddings and Vectorstores](https://pub.towardsai.net/langchain-101-part-3b-talking-to-documents-embeddings-and-vectorstores-c37d460f1519)
[^2]: [Public code of Dr. Ivan Reznikov used in posts, articles, conferences](https://github.com/IvanReznikov/DataVerse)
[^3]: [Notebook hosted on Github by Dr. Ivan Reznikov](https://github.com/IvanReznikov/DataVerse/tree/bc1e275499809a7b1e7ddbea0ac1b4ed22d8bf65/Courses/LangChain/Lecture3.%20Talking%20to%20Data)
[^4]: [Notebook hosted on Google Colab by Dr. Ivan Reznikov](https://colab.research.google.com/drive/1gZ8CfC0n2hNczYfoqynezDkDsMtTmEbi#scrollTo=NhffeyZZlgIw)

