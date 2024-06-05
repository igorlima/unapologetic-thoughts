---
layout: post
title: AI Knowledge Base for Messages
category: code-sample
---

- login in:
  - [Pinecone](https://app.pinecone.io/indexes)
  - [Cohere](https://coral.cohere.com/)

It is a fun and engaging side project for delving into the world of a message
knowledge base! The goal is to search through unstructured data and uncover
meaningful connections. It's a beginning journey in learning and playing around
with data analysis and pattern recognition.

It all began with a read I previously had [here]({{site.baseurl}}{% post_url
2024/2024-06-01-ai-cohere-and-pinecone %}).  I'm thrilled to continue learning and
exploring the topic further! Let me dive in and have some fun learning on this
journey.

## SETUP [^1]

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

## Data Structure

<details markdown="block">
<summary><i>sample <code>data.txt</code></i></summary>

```
...
Wed, Mar 20, 2024
meeting schedule #what-meeting-schedule #d-2024a03m20d
@who-xxxxx
...
in #xxxxxxxxxx-xxxx-xxxx
- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
- Maecenas varius enim at nisl venenatis, ac aliquet dui mollis.
- Donec ullamcorper, libero eget lacinia vulputate, nisi nunc bibendum nunc, eu
  consectetur dui nunc eget velit.
...
Fri, Mar 29, 2024
in #xxx-xxxx-xxxx #what-slack-channel #d-2024a03m29d
in #xxx-xxxx #what-slack-channel #d-2024a03m29d
- Sed blandit orci ac lacus egestas, nec rhoncus justo feugiat.
- Nam in turpis nec turpis scelerisque pharetra. Sed in dui et mi tempor
  interdum.
- Donec bibendum scelerisque ante, ac pharetra nunc sagittis et.
...
Wed, Mar 27, 2024
in DM @who-xxxxxxx #d-2024a03m27d
- Nullam id felis et ipsum bibendum ultrices. Pellentesque habitant morbi
  tristique senectus et netus et malesuada fames ac turpis egestas. Sed congue,
  nisi sed aliquam lacinia, nunc nunc fermentum velit, ac pharetra nunc velit
  vel nisl.
...
Wed, Mar 27, 2024
in #xxxxxx-xxxxxxxxx #what-slack-channel #d-2024a03m27d
- Fusce dapibus, justo ac fermentum euismod, quam lacus venenatis nisl, vel
  aliquet mi massa a nunc. Proin bibendum convallis nibh ac egestas. Nam
  elementum, nunc quis semper elementum, augue nisi porttitor velit, vel
  aliquet nisl nisi eu sapien.
...
```
</details>

## Update Messages

<details markdown="block">
<summary><i>code sample <code>update-messages.py</code></i></summary>

```python
from pprint import pprint
from hashlib import md5
import pudb
import re, os

# open the file in read mode
with open("data.txt", "r") as f:
  """
  # read the file line by line
  lines = f.readlines()
  for line in lines:
    print(line, end="")  # Print without extra newline
  """
  # read the entire file
  data = f.read()

import cohere
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

IDS = []
EMBEDS = []
META = []

chunks = data.split("...")
for chk in chunks:
  chunk = chk.strip()
  # Wed, Mar 27, 2024
  date = chunk.split("\n")[0]
  date = "" if re.match(r"^[A-Z][a-z][a-z], [A-Z][a-z][a-z] \d\d, \d{4}", date) is None else date

  date_pattern = r"#d-(\d{4})a(\d\d)m(\d\d)d"
  dt = re.search(date_pattern, chunk)
  if dt is None:
    year = "0000"
    month = "00"
    day = "00"
  else:
    year = dt.group(1)
    month = dt.group(2)
    day = dt.group(3)

  tag_pattern = r"#(?:\S+)"
  tags = re.findall(tag_pattern, chunk)
  unique_tags = list(set(tags))

  who_pattern = r"@(?:\S+)"
  whoes = re.findall(who_pattern, chunk)
  unique_whoes = list(set(whoes))

  if date is None or len(tags) == 0:
    continue

  # https://www.geeksforgeeks.org/md5-hash-python/
  _id = md5(chunk.encode()).hexdigest()
  _id = f"{year}{month}{day}-{_id}"

  meta = {
    'date': date,
    'year': year,
    'month': month,
    'day': day,
    'tag': unique_tags,
    'chunk': chunk,
    'who': unique_whoes
  }

  IDS.append(_id)
  META.append(meta)

EMBEDS = co.embed(
  texts=[meta['chunk'] for meta in META],
  model='embed-english-v3.0',
  input_type='search_document',
  truncate='END'
).embeddings

import numpy as np
shape = np.array(EMBEDS).shape
# pprint(shape)

from pinecone import Pinecone, ServerlessSpec
# initialize connection to pinecone (get API key at app.pinecone.io)
pc = Pinecone(
  api_key=os.environ.get("PINECONE_API_KEY")
)
index_name = 'ilima-messages'
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

batch_size = 128
# create list of (id, vector, metadata) tuples to be upserted
to_upsert = list(zip(IDS, EMBEDS, META))
for i in range(0, shape[0], batch_size):
  i_end = min(i+batch_size, shape[0])
  index.upsert(vectors=to_upsert[i:i_end])
# let's view the index statistics
print(index.describe_index_stats())
```

```bash
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
python3 update-messages.py
```
</details>

## Query Messages

<details markdown="block">
<summary><i>code sample <code>query-messages.py</code></i></summary>

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
index_name = 'ilima-messages'
# if the index does not exist, we create it
if index_name not in pc.list_indexes().names():
  print('index does not exist.')
  exit()

# connect to index
index = pc.Index(index_name)

# SEMANTIC SEARCH
query = "Code contributions on Wed"
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
  print(f"{match['score']:.2f}: \n{match['id']}: \n{match['metadata']['chunk']}\n")
```

```bash
PINECONE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
python3 query-messages.py
```
</details>

---
{: data-content="footnotes"}

[^1]: [AI Cohere and Pinecone]({{site.baseurl}}{% post_url 2024/2024-06-01-ai-cohere-and-pinecone %})
