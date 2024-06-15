---
layout: post
title: RAG usage on an internal knowledge base
category: code-sample
---

In short, RAG is a simple three-step process: __indexing__, __retrieval__, and __generation__ [^1].

![image](https://github.com/igorlima/unapologetic-thoughts/assets/1886786/c7c69f3a-06c6-4340-b0a9-41c5080cfd40)
<sup><sup>image source from Medium [^1]</sup></sup>

The key thing to remember from this diagram is the use of embeddings and a
vector database as a proxy to find a relevant context to the query [^2].

![image](https://github.com/igorlima/unapologetic-thoughts/assets/1886786/0d812cb4-9862-42b7-a17f-058375be2a58)
<sup><sup>image source from Medium [^2]</sup></sup>

![image](https://github.com/igorlima/unapologetic-thoughts/assets/1886786/ae858bcf-3284-4026-8cde-3e14a4ef36dd)
<sup><sup>a hight level RAG sample architecture [^3]</sup></sup>

## other references
- [Retrieval Augmented Generation - RAG]({{site.baseurl}}{% post_url 2024/2024-06-06-rag %})
- [Choosing between LlamaIndex or LangChain]({{site.baseurl}}{% post_url 2024/2024-06-14-llamaindex-or-langchain %})

---

{: data-content="footnotes"}

[^1]: [How to improve RAG results in your LLM apps: from basics to advanced](https://bootcamp.uxdesign.cc/how-to-improve-rag-results-in-your-llm-apps-from-basics-to-advanced-822818014144)
[^2]: [You Can Now Build A Chatbot To Talk To Your Internal Knowledge Base](https://levelup.gitconnected.com/you-can-now-build-a-chatbot-to-talk-to-your-internal-knowledge-base-b6066cacf2d5)
[^3]: [Level Up your RAG: Tuning Embeddings on Vertex AI](https://medium.com/google-cloud/level-up-your-rag-tuning-embeddings-on-vertex-ai-901bb7f65bd0)
