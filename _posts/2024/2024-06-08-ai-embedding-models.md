---
layout: post
title: AI Embedding Models - Voyage, AnyScale, Google Gemini
category: code-sample
---

## [Voyage AI](https://www.voyageai.com/)

[Voyage](https://docs.voyageai.com/docs/introduction) is a team of leading AI
researchers and engineers, building embedding models for better retrieval and
RAG. [^1]

<details markdown="block">
<summary><i>setup</i></summary>

```sh
python3 -m venv env-embeddings
source env-embeddings/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.

pip3 install -U voyageai==0.2.3
pip3 install --upgrade --force-reinstall voyageai
pip3 show voyageai
pip3 index versions voyageai
```
</details>

<details markdown="block">
<summary><i>hands-on</i></summary>

```python
# import the 'voyageai' module
import voyageai
import os

# Create a 'Client' object from the 'voyageai' module and initialize it with your API key
vo = voyageai.Client(api_key=os.environ.get("VOYAGE_AI_API_KEY"))

# user query
user_query = "when apple is releasing their new Iphone?"


# The 'model' parameter is set to "voyage-2", and the 'input_type' parameter is set to "document"
documents_embeddings = vo.embed(
    [user_query], model="voyage-2", input_type="document"
).embeddings

# printing the embedding
print(documents_embeddings)
```

```bash
VOYAGE_AI_API_KEY=pa-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 voyage-ai.py
```
</details>


Supported Embedding models, and more to come.

| Model                   | Context Length (tokens) | Embedding Dimension | Description                                                                             |
| ---                     | ---                     | ---                 | ---                                                                                     |
| voyage-code-2           | 16000                   | 1536                | Optimized for code retrieval (17% better than alternatives)                             |
| voyage-2                | 4000                    | 1024                | Embedding model with the best retrieval quality (better than OpenAI ada)                |
| voyage-lite-02-instruct | 4000                    | 1024                | Instruction-tuned for classification, clustering, and sentence textual similarity tasks |


## [AnyScale AI](https://www.anyscale.com)

Anyscale, the company behind Ray, releases APIs for LLM developers to run and
fine-tune open-source LLMs quickly, cost-efficiently, and at scale. [^1]

<details markdown="block">
<summary><i>setup</i></summary>

```sh
python3 -m venv env-embeddings
source env-embeddings/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.

pip3 install -U openai==1.33.0
pip3 install --upgrade --force-reinstall openai
pip3 show openai
pip3 index versions openai
```
</details>

<details markdown="block">
<summary><i>hands-on llm</i></summary>

```python
# import necessary modules
import openai
import os

# define the anyscale endpoint token
ANYSCALE_ENDPOINT_TOKEN = os.environ.get("ANYSCALE_ENDPOINT_TOKEN")

# Create an OpenAI client with the Anyscale base URL and API key
oai_client = openai.OpenAI(
  base_url="https://api.endpoints.anyscale.com/v1",
  api_key=ANYSCALE_ENDPOINT_TOKEN,
)

# Define the OpenAI model to be used for chat completions
model = "mistralai/Mistral-7B-Instruct-v0.1"

# Define a prompt for the chat completion
prompt = '''hello, how are you?
'''

# Use the AnyScale model for chat completions
# Send a user message using the defined prompt
response = oai_client.chat.completions.create(
  model=model,
  messages=[
    {"role": "user", "content": prompt}
  ],
)

# printing the response
print(response.choices[0].message.content)
```

```bash
ANYSCALE_ENDPOINT_TOKEN=esecret_xxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 anyscale-ai.py
```
</details>

<details markdown="block">
<summary><i>hands-on embedding</i></summary>

```python
# import necessary modules
import openai
import os

# Define the Anyscale endpoint token
ANYSCALE_ENDPOINT_TOKEN = os.environ.get("ANYSCALE_ENDPOINT_TOKEN")

# Create an OpenAI client with the Anyscale base URL and API key
oai_client = openai.OpenAI(
  base_url="https://api.endpoints.anyscale.com/v1",
  api_key=ANYSCALE_ENDPOINT_TOKEN,
)

# https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
# https://cookbook.openai.com/examples/using_embeddings
embeddings = oai_client.embeddings.create(
  model="thenlper/gte-large",
  input=["Your text string goes here"],
)
# print(embeddings.model_dump())
print(embeddings.data[0].embedding)
```

```bash
ANYSCALE_ENDPOINT_TOKEN=esecret_xxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 anyscale-ai.py
```
</details>

Supported LLM and Embedding models.

| Model                       | Price ($/M tokens) |
| ---                         | ---                |
| Mistral-7B-OpenOrca         | 0.15               |
| Mistral-7B-Instruct-v0.1    | 0.15               |
| Zephyr-7b-beta              | 0.15               |
| Llama-Guard-7b              | 0.15               |
| Llama-2-7b-chat-hf          | 0.15               |
| NeuralHermes-2.5-Mistral-7B | 0.15               |
| Llama-2-13b-chat-hf         | 0.25               |
| Mixtral-8x7B-Instruct-v0.1  | 0.50               |
| Llama-2-70b-chat-hf         | 1.0                |
| CodeLlama-34b-Instruct-hf   | 1.0                |
| CodeLlama-70b-Instruct-hf   | 1.0                |
| thenlper-gte-large          | 0.05               |
| BAAI/bge-large-en-v1.5      | 0.05               |

## [Google Gemini AI](https://ai.google.dev/docs)

The free tier API usage is what makes it more interesting. [^1] [^2] [^3]

<details markdown="block">
<summary><i>setup</i></summary>

```sh
python3 -m venv env-embeddings
source env-embeddings/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.

pip3 install -U google-generativeai==0.6.0 grpcio==1.64.1 grpcio-tools==1.62.2
pip3 install --upgrade --force-reinstall google-generativeai grpcio grpcio-tools
pip3 show google-generativeai grpcio grpcio-tools
pip3 index versions google-generativeai grpcio grpcio-tools
```
</details>

<details markdown="block">
<summary><i>hands-on llm</i></summary>

```python
# importing google.generativeai as genai
import google.generativeai as genai
import os

# setting the api key
genai.configure(api_key=os.environ.get("GOOGLE_GEMINI_API_KEY"))

# setting the text model
model = genai.GenerativeModel('gemini-pro')

# generating response
response = model.generate_content("What is the meaning of life?")

# printing the response
print(response.text)
```
```bash
GOOGLE_GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 gemini-ai.py
```
</details>

<details markdown="block">
<summary><i>hands-on embedding</i></summary>

```python
# importing google.generativeai as genai
import google.generativeai as genai
import os

# setting the api key
genai.configure(api_key=os.environ.get("GOOGLE_GEMINI_API_KEY"))

# https://python.langchain.com/v0.2/docs/integrations/text_embedding/google_generative_ai/
# https://github.com/google-gemini/cookbook
# https://ai.google.dev/api/python/google/generativeai
# https://ai.google.dev/api/python/google/generativeai/generate_embeddings

title = "The next generation of AI for developers and Google Workspace"
sample_text = '''
Title: The next generation of AI for developers and Google Workspace
Full article:
Gemini API & Google AI Studio: An approachable way to explore and prototype with generative AI applications
'''

# https://github.com/google-gemini/cookbook/blob/main/examples/Talk_to_documents_with_embeddings.ipynb
# https://ai.google.dev/api/python/google/generativeai/embed_content
model = 'models/embedding-001'
embedding = genai.embed_content(
  model=model,
  content=[
    sample_text,
    "The next generation of AI for developers and Google Workspace"
  ],
  task_type="retrieval_query",
  # task_type="retrieval_document",
  # title is optional - only applicable when task_type is RETRIEVAL_DOCUMENT.
  # title=title,
)
print(embedding['embedding'][0])
print('-----')

model = 'models/embedding-001'
embedding = genai.embed_content(
  model=model,
  content= sample_text,
  task_type="retrieval_document",
  title=title,
)
print(embedding)
```
```bash
GOOGLE_GEMINI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
  python3 gemini-ai.py
```
</details>

Supported Models.

| Model Name        | Task Type                           | Query per Minute |
| ---               | ---                                 | ---              |
| gemini-pro        | Text                                | 60               |
| gemini-pro-vision | Image                               | 60               |
| embedding-001     | Classification, clustering and more | Unknown          |

List of Task Types.

| `task_type`           | Description                                                                                                         |
| ---                   | ---                                                                                                                 |
| `RETRIEVAL_QUERY`     | Specifies the given text is a query in a search or retrieval setting.                                               |
| `RETRIEVAL_DOCUMENT`  | Specifies the given text is a document in a search or retrieval setting.                                            |
| `SEMANTIC_SIMILARITY` | Specifies the given text is used for Semantic Textual Similarity (STS).                                             |
| `CLASSIFICATION`      | Specifies that the embedding is used for classification.                                                            |
| `CLUSTERING`          | Specifies that the embedding is used for clustering.                                                                |
| `QUESTION_ANSWERING`  | Specifies that the query embedding is used for answering questions. Use `RETRIEVAL_DOCUMENT` for the document side. |
| `FACT_VERIFICATION`   | Specifies that the query embedding is used for fact verification.                                                   |

## other embedding models

- [AI Embedding Models - Google VertexAI]({{site.baseurl}}{% post_url 2024/2024-06-09-ai-embedding-models %})

---
{: data-content="footnotes"}

[^1]: [Free GenAI APIs You Can Use in 2024](https://levelup.gitconnected.com/free-genai-apis-you-can-use-in-2024-3e71f406338b)
[^2]: [Google - API key](https://makersuite.google.com/app/apikey)
[^3]: [Google AI Studio - API key](https://aistudio.google.com/app/apikey)
