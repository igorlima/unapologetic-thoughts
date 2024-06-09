---
layout: post
title: AI Cohere and Pinecone
category: code-sample
---

Using Cohere and Pinecone to generate and index high-quality vector embeddings. [^2]

The Cohere platform builds natural language processing and generation into your
product with a few lines of code. Cohere’s large language models (LLMs) can
solve a broad spectrum of natural language use cases, including classification,
semantic search, paraphrasing, summarization, and content generation.

Use the Cohere Embed API endpoint to generate language embeddings, and then
index those embeddings in the Pinecone vector database for fast and scalable
vector search.

## SETUP

```bash
python3 -m venv env-cohere
source env-cohere/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
pip3 install -U cohere==5.5.4 pinecone-client==4.1.0
pip3 install --upgrade --force-reinstall cohere pinecone-client
pip3 show cohere pinecone-client
pip3 index versions cohere

https://docs.pinecone.io/integrations/cohere
```

## Delete Data

Since Pinecone records can always be efficiently accessed using their ID,
deleting by ID is the most efficient way to remove specific records.

To delete all records from a namespace, specify the appropriate `deleteAll`
parameter for your client and provide a `namespace` parameter. [^4]

<details markdown="block">
<summary><i>code sample <code>delete-data.py</code></i></summary>

```python
import os
from pprint import pprint

# debugging
import pudb;
# pu.db

import cohere
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

from pinecone import Pinecone, ServerlessSpec
# initialize connection to pinecone (get API key at app.pinecone.io)
pc = Pinecone(
  api_key=os.environ.get("PINECONE_API_KEY")
)
index_name = 'ilima-cohere'
# if the index does not exist, we create it
if index_name not in pc.list_indexes().names():
  print('index does not exist.')
  exit()

# connect to index
index = pc.Index(index_name)

# delete all vectors in the index
# https://docs.pinecone.io/guides/data/delete-data
index.delete(
  delete_all=True,
  # namespace='default'
)
print('deleted all vectors in the index.')
print('done.')
```

```bash
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
python3 delete-data.py
```
</details>

## Insert Data

MD5 (Message Digest 5) is a cryptographic hash function that produces a 128-bit
fingerprint of a message.

Cryptographic hashes are used in digital signatures, message authentication
codes, manipulation detection, fingerprints, checksums (message integrity
check), hash tables, password storage and much more. [^3]

<details markdown="block">
<summary><i>code sample <code>insert-data.py</code></i></summary>

```python
import os
from pprint import pprint

# debugging
import pudb;
# pu.db

import cohere
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

DATA = [
 'How did serfdom develop in and then leave Russia ?',
 'What films featured the character Popeye Doyle ?',
 "How can I find a list of celebrities ' real names ?",
 'What fowl grabs the spotlight after the Chinese Year of the Monkey ?',
 'What is the full form of .com ?',
 'What contemptible scoundrel stole the cork from my lunch ?',
 "What team did baseball 's St. Louis Browns become ?",
 'What is the oldest profession ?',
 'What are liver enzymes ?',
 'Name the scar-faced bounty hunter of The Old West .',
 'When was Ozzy Osbourne born ?',
 'Why do heavier objects travel downhill faster ?',
 'Who was The Pride of the Yankees ?',
 'Who killed Gandhi ?',
 'What is considered the costliest disaster the insurance industry has ever faced ?',
 'What sprawling U.S. state boasts the most airports ?',
 'What did the only repealed amendment to the U.S. Constitution deal with ?',
 'How many Jews were executed in concentration camps during WWII ?',
 "What is 'Nine Inch Nails' ?",
 'What is an annotated bibliography ?'
]

embeds = co.embed(
  texts=DATA,
  model='embed-english-v3.0',
  input_type='search_document',
  truncate='END'
).embeddings

# check the dimensionality of the returned vectors.
import numpy as np
shape = np.array(embeds).shape
# pprint(shape)

from pinecone import Pinecone, ServerlessSpec
# initialize connection to pinecone (get API key at app.pinecone.io)
pc = Pinecone(
  api_key=os.environ.get("PINECONE_API_KEY")
)
index_name = 'ilima-cohere'
# if the index does not exist, we create it
if index_name not in pc.list_indexes().names():
  pc.create_index(
    name=index_name,
    dimension=shape[1],
    metric='cosine',
    spec=ServerlessSpec(
      cloud='aws',
      region='us-east-1'
    )
  )

# connect to index
index = pc.Index(index_name)

# md5
# https://www.geeksforgeeks.org/md5-hash-python/
from hashlib import md5
# upsert the embeddings into the index
batch_size = 128
ids = [md5(DATA[i].encode()).hexdigest() for i in range(shape[0])]
# create list of metadata dictionaries
meta = [{'text': text} for text in DATA]
# create list of (id, vector, metadata) tuples to be upserted
to_upsert = list(zip(ids, embeds, meta))
for i in range(0, shape[0], batch_size):
  i_end = min(i+batch_size, shape[0])
  index.upsert(vectors=to_upsert[i:i_end])
# let's view the index statistics
print(index.describe_index_stats())
```

```bash
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
python3 insert-data.py
```
</details>


## Query Data

The `query` operation searches the index using a query vector. It retrieves the
IDs of the most similar records in the index, along with their similarity
scores. This operation can optionally return the result’s vector values and
metadata, too. You specify the number of vectors to retrieve each time you send
a query. Matches are always ordered by similarity from most similar to least
similar. [^1]

<details markdown="block">
<summary><i>code sample <code>query-data.py</code></i></summary>

```python
import os
from pprint import pprint

# debugging
import pudb;
# pu.db

import cohere
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

from pinecone import Pinecone, ServerlessSpec
# initialize connection to pinecone (get API key at app.pinecone.io)
pc = Pinecone(
  api_key=os.environ.get("PINECONE_API_KEY")
)
index_name = 'ilima-cohere'
# if the index does not exist, we create it
if index_name not in pc.list_indexes().names():
  print('index does not exist.')
  exit()

# connect to index
index = pc.Index(index_name)

# SEMANTIC SEARCH
query = "What caused the 1929 Great Depression?"
query = "Who was The Pride of?"
# create the query embedding
xq = co.embed(
  texts=[query],
  model='embed-english-v3.0',
  input_type='search_query',
  truncate='END'
).embeddings

# # check the dimensionality of the returned vectors.
# import numpy as np
# print(np.array(xq).shape)

# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)
# print the results
for match in res['matches']:
  print(f"{match['score']:.2f}: {match['id']}: {match['metadata']['text']}")
print('---')

query = "What was the cause of the major recession in the early 20th century?"
# create the query embedding
xq = co.embed(
  texts=[query],
  model='embed-english-v3.0',
  input_type='search_query',
  truncate='END'
).embeddings
# query, returning the top 5 most similar results
res = index.query(vector=xq, top_k=5, include_metadata=True)
# print the results
for match in res['matches']:
  print(f"{match['score']:.2f}: {match['id']}: {match['metadata']['text']}")
print('---')

query = "Why was there a long-term economic downturn in the early 20th century?"
# create the query embedding
xq = co.embed(
  texts=[query],
  model='embed-english-v3.0',
  input_type='search_query',
  truncate='END'
).embeddings
# query, returning the top 10 most similar results
res = index.query(vector=xq, top_k=10, include_metadata=True)
# print the results
for match in res['matches']:
  print(f"{match['score']:.2f}: {match['id']}: {match['metadata']['text']}")
print('---')
```

```bash
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
python3 query-data.py
```
</details>

## other external resources

- [Pinecone Documentation](https://docs.pinecone.io/home)
- [Pinecone Notebooks](https://docs.pinecone.io/examples/notebooks)
  - [Langchain Retrieval Augmentation](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/langchain-retrieval-augmentation.ipynb)
    - _Give knowledge base information to an LLM using LangChain._
  - [Semantic Search](https://colab.research.google.com/github/pinecone-io/examples/blob/master/docs/semantic-search.ipynb)
    - _Perform a simple semantic search._

---
{: data-content="footnotes"}

[^1]: [Pinecone Docs - Query data](https://docs.pinecone.io/guides/data/query-data)
[^2]: [Pinecone Docs - Cohere](https://docs.pinecone.io/integrations/cohere)
[^3]: [MD5 hash in Python](https://www.geeksforgeeks.org/md5-hash-python/)
[^4]: [Pinecone Docs - Delete data](https://docs.pinecone.io/guides/data/delete-data)
