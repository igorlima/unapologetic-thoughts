---
layout: post
title: AI Embedding Models - Google Gemini
category: code-sample
---

[Gemini Embedding](https://ai.google.dev/gemini-api/docs/embeddings):
to get started, check out the official developer documentation and cookbooks:
- [Embeddings documentation](https://ai.google.dev/gemini-api/docs/embeddings)
- [Quickstart notebook](https://github.com/google-gemini/cookbook/blob/05b617f8fc6f8753361330b14d4bfc9461b2be54/quickstarts/Embeddings.ipynb)
- [Examples and guides for using the Gemini API](https://github.com/google-gemini/cookbook)

<details markdown="block">
<summary><i>setup</i></summary>

```sh
# mkdir $(date +%Ya%mm%dd-%Hh%M%S)
mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
python3 -m venv env-embeddings
source env-embeddings/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.

pip3 install -U google-genai==1.36.0
pip3 install --upgrade --force-reinstall google-genai
pip3 show google-genai
pip3 index versions google-genai
```
</details>

<details markdown="block">
<summary><i>hands-on</i></summary>

```python
from google import genai
client = genai.Client()
result = client.models.embed_content(
        model="gemini-embedding-001",
        contents="What is the meaning of life?")
print(result.embeddings)
```

```bash
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 gemini-ai.py
```
</details>

<details markdown="block">
<summary><i>more samples</i></summary>

**Generating embeddings**
```python
from google import genai
client = genai.Client()
result = client.models.embed_content(
        model="gemini-embedding-001",
        contents= [
          "What is the meaning of life?",
          "What is the purpose of existence?",
          "How do I bake a cake?"
        ])
for embedding in result.embeddings:
  print(embedding)
```

**Controlling embedding size**
```python
from google import genai
from google.genai import types
client = genai.Client()
result = client.models.embed_content(
  model="gemini-embedding-001",
  contents="What is the meaning of life?",
  config=types.EmbedContentConfig(output_dimensionality=768)
)
[embedding_obj] = result.embeddings
embedding_length = len(embedding_obj.values)
print(f"Length of embedding: {embedding_length}")
```

```bash
GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 gemini-ai.py
```
</details>


## other embedding models

- [AI Embedding Models - Google VertexAI]({{site.baseurl}}{% post_url 2024/2024-06-09-ai-embedding-models %})
- [Dots Mapping Embedding index]({{site.baseurl}}{% link pages/dots-mapping.md %}#2025a09m14d-20250914204144)

---
{: data-content="footnotes"}

[^1]: [Free GenAI APIs You Can Use in 2024](https://levelup.gitconnected.com/free-genai-apis-you-can-use-in-2024-3e71f406338b)
[^2]: [Google - API key](https://makersuite.google.com/app/apikey)
[^3]: [Google AI Studio - API key](https://aistudio.google.com/app/apikey)
