---
layout: post
title: AI Embedding Models - Google VertexAI
category: code-sample
---


<details markdown="block">
<summary><i>setup</i></summary>

```sh
python3 -m venv my-env-vertexai
source my-env-vertexai/bin/activate

pip3 install vertexai==1.49.0
pip3 show vertexai
```
</details>

<details markdown="block">
<summary><i>hands-on</i></summary>

- [how to set up `GOOGLE_APPLICATION_CREDENTIALS`](https://igorlima.github.io/unapologetic-snippets/docs/languages/containerization/docker-samples#google-cloud-cli)

```python
import vertexai
from typing import List, Optional
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

project_id = "PROJECT_ID"
vertexai.init(project=project_id, location="us-west1")

def embed_text(
  texts: List[str] = ["banana muffins? ", "banana bread? banana muffins?"],
  task: str = "RETRIEVAL_DOCUMENT",
  model_name: str = "text-embedding-004",
  dimensionality: Optional[int] = 256,
) -> List[List[float]]:
  """Embeds texts with a pre-trained, foundational model."""
  model = TextEmbeddingModel.from_pretrained(model_name)
  inputs = [TextEmbeddingInput(text, task) for text in texts]
  kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
  embeddings = model.get_embeddings(inputs, **kwargs)
  return [embedding.values for embedding in embeddings]

print(embed_text(
  texts=["banana muffins? ", "banana bread? banana muffins?"],
))

print('---')
```

```bash
GOOGLE_APPLICATION_CREDENTIALS=~/Downloads/tmp/application_default_credentials.json \
  python3 vertex-ai.py
```
</details>

## other embedding models

- [AI Embedding Models - Voyage, AnyScale, Google Gemini]({{site.baseurl}}{% post_url 2024/2024-06-08-ai-embedding-models %})

## other resources

- [RAG usage on an internal knowledge base]({{site.baseurl}}{% post_url 2024/2024-06-04-rag-knowledge-base %})

---
{: data-content="footnotes"}

[^1]: [Free GenAI APIs You Can Use in 2024](https://levelup.gitconnected.com/free-genai-apis-you-can-use-in-2024-3e71f406338b)
[^2]: [Google - API key](https://makersuite.google.com/app/apikey)
[^3]: [Google AI Studio - API key](https://aistudio.google.com/app/apikey)
