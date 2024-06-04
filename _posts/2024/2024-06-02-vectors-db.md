---
layout: post
title: Vector DB - DocArrayInMemorySearch, Chroma and FAISS
category: code-sample
---

There is some confusion across the web with misusing words vectorstores and
index, so let’s straighten it up[^1].

Vectorstores store vectores (thus the name, duh).  Talking about index, it’s
purpose is to find a specific row or document based on the position. In the
case of a vectorstore, we’re also talking about positions, and to find similar
or related chunks to the query, we use the same embedding model [^5] and find
the hypothetical position of the query within a vectorstore. That would be
counted as an index. Closest n chunks to the index (or by threshold) are later
retrieved[^1].

<details markdown="block">
<summary><strong>setup</strong></summary>

```bash
python3 -m venv env-vector-db
source env-vector-db/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.

pip3 install -U cohere==5.5.4 langchain-community==0.2.1 "docarray"==0.40.0 langchain_cohere==0.1.5 chromadb==0.5.0 faiss-cpu==1.8.0

pip3 install --upgrade --force-reinstall cohere langchain-community "docarray" langchain_cohere chromadb faiss-cpu

pip3 show cohere langchain-community "docarray" langchain_cohere chromadb faiss-cpu

pip3 index versions cohere langchain-community "docarray" langchain_cohere chromadb faiss-cpu
```
</details>

<details markdown="block">
<summary><i><code>file.txt</code></i></summary>

- [text file source](https://raw.githubusercontent.com/IvanReznikov/DataVerse/main/Courses/LangChain/data/planets.txt) [^2] [^3] [^4]

```
Freddyland: Small and swift, Freddyland orbits the Sun in just 88 days. Its days are long - longer than its years, lasting 59 Blueberry days. Temperatures can soar up to 800°F, making it the hottest planet. No atmosphere to speak of. It's a rocky world, covered in craters. Barely any tilt means no seasons. It's closest to the Sun.
Foamborn: Veiled in thick clouds, Foamborn's surface is hidden. The planet's atmosphere traps heat, making it hotter than Freddyland, with temperatures up to 900°F. Acidic rains carve its landscape. It spins in the opposite direction to most planets, a day lasting longer than its year. High pressure crushes anything that lands. It's the second planet from the Sun. Its thick clouds reflect sunlight, making it bright.
Blueberry: Home to millions of species, including humans. Water covers 70% of its surface. The atmosphere is a mix of nitrogen and oxygen, vital for life. It orbits the Sun every 365.25 days. Its axial tilt creates seasons. The only planet known to support life. It has one moon.
Twix: Known as the Red Planet, due to its iron oxide dust. It has the largest volcano and the deepest, longest canyon in the solar system. Water ice exists at its poles. Two moons orbit it, Phobos and Deimos. A day on Twix is just over 24 hours. Its thin atmosphere means cold temperatures, averaging -80°F. Robots have explored its surface.
Ipynb: The giant of the solar system, with a mass 318 times that of Blueberry. It has at least 79 moons. The Great Red Spot, a storm larger than Blueberry, rages on its surface. It spins fast, making a day last just 10 hours. Its rings are faint and composed mainly of dust. It's made mostly of hydrogen and helium. Fifth from the Sun.
Sauron: Known for its stunning rings, made of ice and rock particles. It's the second-largest planet. Sixty-two moons orbit it, with Titan being the largest. A day lasts about 10.7 hours. Its atmosphere is mostly hydrogen and helium. The density is so low that Sauron would float in water. It's the sixth planet from the Sun.
Nuclearium: It's tilted on its side, making its seasons extreme. The atmosphere is mostly hydrogen, helium, and methane. Methane gives it a blue hue. It orbits the Sun every 84 years. It has 27 known moons. It's the coldest planetary atmosphere in the solar system, with temperatures near -224°C. Seventh from the Sun.
Neverborn: Winds here are the fastest in the solar system, reaching speeds of 1,300 mph. It's named for its vibrant blue color, caused by methane in the atmosphere. It completes an orbit every 165 years. It has 14 known moons. It's the fourth-largest planet by diameter. Extremely cold, with temperatures about -201°C. It's the eighth planet from the Sun.
```
</details>

<details markdown="block">
<summary><i><code>vectors-db</code></i></summary>

```python
import os
from pprint import pprint

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

# import cohere
# co = cohere.Client(os.environ.get("COHERE_API_KEY"))
# embeds = co.embed(
#   texts=sentences,
#   model='embed-english-v3.0',
#   input_type='search_document',
#   truncate='END'
# ).embeddings

# print(embeds)
# check the dimensionality of the returned vectors.
# import numpy as np
# pprint(np.array(embeds).shape)
# print('---')

# https://python.langchain.com/v0.1/docs/modules/data_connection/text_embedding/
from langchain_cohere import CohereEmbeddings
embeddings_model = CohereEmbeddings(cohere_api_key=os.environ.get("COHERE_API_KEY"), model='embed-english-v3.0')
# embeddings = embeddings_model.embed_documents(sentences)

# https://python.langchain.com/v0.2/docs/integrations/vectorstores/docarray_in_memory/
# https://api.python.langchain.com/en/latest/_modules/langchain_community/vectorstores/docarray/in_memory.html
# https://api.python.langchain.com/en/latest/vectorstores/langchain_community.vectorstores.docarray.in_memory.DocArrayInMemorySearch.html
from langchain_community.vectorstores import DocArrayInMemorySearch
db = DocArrayInMemorySearch.from_texts(
  texts=sentences,
  embedding=embeddings_model
)
question = "Any waterproof adventure bags?"
docs = db.similarity_search(question)
print([doc.page_content for doc in docs])
print('...')
print(docs[0])
print('---')

docs = db.similarity_search_with_score(question)
pprint([f"{score} {doc.page_content}" for (doc, score) in docs])
print('---')

from hashlib import md5
IDS = []
META = []
for sentence in sentences:
  _id = md5(sentence.encode()).hexdigest()
  IDS.append(_id)
  META.append({"source":"SOURCE_1"})

# https://docs.trychroma.com/getting-started
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.create_documents(sentences, META)
"""
# OR
for i, _doc in enumerate(documents):
  # https://github.com/langchain-ai/langchain/issues/15115#issuecomment-1868442302
  _doc.metadata = META[i]
  _doc.id = IDS[i]
"""
persist_directory = "db/chroma/"
chroma_db = Chroma.from_documents(
  documents=documents,
  embedding=embeddings_model,
  # use ids to avoid duplicated values in DB
  ids=IDS,
  persist_directory=persist_directory
)
chroma_db = None
# Load the persisted db from disk
chroma_db = Chroma(persist_directory=persist_directory, embedding_function=embeddings_model)
query = "Any lightweight bags?"
docs = chroma_db.similarity_search_with_score(query,k=4)
pprint([f"{score} {doc.page_content}" for (doc, score) in docs])

print('***')
docs = chroma_db.max_marginal_relevance_search(query, k=5, fetch_k=10)
print([doc.page_content for doc in docs])
print('...')
# or
# https://python.langchain.com/v0.2/docs/integrations/retrievers/self_query/chroma_self_query/
retriever = chroma_db.as_retriever(search_type="mmr", k=5, fetch_k=10)
docs = retriever.invoke("How much money did Pando raise?")
print([doc.page_content for doc in docs])
print('***')
pprint(chroma_db.similarity_search(
  query,
  filter={"source":"SOURCE_1"}
))
# or
retriever = chroma_db.as_retriever(filter={"source":"SOURCE_1"})
print('***')
"""
# https://github.com/langchain-ai/langchain/issues/15115
texts = [doc.page_content for doc in documents]
metadatas = [doc.metadata for doc in documents]
return cls.from_texts(
  texts=texts,
  embedding=embedding,
  metadatas=metadatas,
  ids=ids,
  collection_name=collection_name,
  persist_directory=persist_directory,
  client_settings=client_settings,
  client=client,
  collection_metadata=collection_metadata,
  **kwargs,
)
"""


# https://python.langchain.com/v0.2/docs/integrations/providers/cohere/
# https://python.langchain.com/v0.2/docs/integrations/llms/cohere/
from langchain_cohere.llms import Cohere
llm=Cohere(cohere_api_key=os.environ.get("COHERE_API_KEY"))
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.document_loaders import TextLoader
index = VectorstoreIndexCreator(
  vectorstore_cls=DocArrayInMemorySearch,
  embedding=embeddings_model,
  text_splitter=text_splitter
).from_loaders([TextLoader("file.txt")])
print(index.query(query, llm=llm))
print('---')

query = "Any lightweight bags?"
from langchain_community.vectorstores import FAISS
faiss_db = FAISS.from_documents(
  documents=documents,
  embedding=embeddings_model,
  # use ids to avoid duplicated values in DB
  ids=IDS,
)
docs = db.similarity_search(query)
print([doc.page_content for doc in docs])
print('...')
#or
docs = db.similarity_search_with_score(query)
pprint([f"{score} {doc.page_content}" for (doc, score) in docs])
```

```bash
COHERE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 vectors-db.py
```
</details>

---
{: data-content="footnotes"}

[^1]: [LangChain 101: Part 3b. Talking to Documents: Embeddings and Vectorstores](https://pub.towardsai.net/langchain-101-part-3b-talking-to-documents-embeddings-and-vectorstores-c37d460f1519)
[^2]: [Public code of Dr. Ivan Reznikov used in posts, articles, conferences](https://github.com/IvanReznikov/DataVerse)
[^3]: [Notebook hosted on Github by Dr. Ivan Reznikov](https://github.com/IvanReznikov/DataVerse/tree/bc1e275499809a7b1e7ddbea0ac1b4ed22d8bf65/Courses/LangChain/Lecture3.%20Talking%20to%20Data)
[^4]: [Notebook hosted on Google Colab by Dr. Ivan Reznikov](https://colab.research.google.com/drive/1gZ8CfC0n2hNczYfoqynezDkDsMtTmEbi#scrollTo=NhffeyZZlgIw)
[^5]: [AI Embeddings]({{site.baseurl}}{% post_url 2024/2024-06-02-embeddings %})
