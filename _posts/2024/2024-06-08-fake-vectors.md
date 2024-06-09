---
layout: post
title: AI - Vectors Fake Representation
category: code-sample
---

[Alternatively] Use fake representation with random vectors. [^1]

If you couldn't download the model due to network issues, as a walkaround, you
can use random vectors to represent the text and still finish the example. Just
note that the search result won't reflect semantic similarity as the vectors
are fake ones. [^1]

<details markdown="block">
<summary><i>code sample</i></summary>

```python
import random

# Text strings to search from.
docs = [
  "Artificial intelligence was founded as an academic discipline in 1956.",
  "Alan Turing was the first person to conduct substantial research in AI.",
  "Born in Maida Vale, London, Turing was raised in southern England.",
]
# Use fake representation with random vectors (768 dimension).
vectors = [[random.uniform(-1, 1) for _ in range(768)] for _ in docs]
data = [
  {"id": i, "vector": vectors[i], "text": docs[i], "subject": "history"}
  for i in range(len(vectors))
]

print("Data has", len(data), "entities, each with fields: ", data[0].keys())
print("Vector dim:", len(data[0]["vector"]))
# print(data)
```
</details>

Vector DB:
- [Milvus DB]({{site.baseurl}}{% post_url 2024/2024-06-08-milvus-vector-db %})
- [Weaviate DB]({{site.baseurl}}{% post_url 2024/2024-06-08-cohere-and-weaviate %})
- [Chroma, FAISS, DocArrayInMemorySearch]({{site.baseurl}}{% post_url 2024/2024-06-02-vectors-db %})

---
{: data-content="footnotes"}

[^1]: [Milvus Introduction](https://milvus.io/docs/overview.md)
