---
layout: post
title: Choosing between LlamaIndex or LangChain
category: code-sample
---

LlamaIndex is a framework designed to index and query LLMs based on your own custom data.

![image](...)
LlamaIndex Architecture [^1]
- https://miro.medium.com/v2/resize:fit:1400/format:webp/1*MRlNUfoklpCls0-yRwnJEg.png


LangChain is another framework used to build tailored LLMs based on custom data sources.

![image](...)
Langchain Architecture [^1]
- https://d11qlje7gx84z0.cloudfront.net/wp-content/uploads/2024/05/3ab6191d-2d39-4aee-8c41-88c42957f030.jpg


__LlamaIndex vs LangChain: Choosing the Right Framework__

![image](...)
LLamaIndex vs Langchain key factors [^1]
- https://miro.medium.com/v2/resize:fit:1280/format:webp/0*Od_-SbaGYXecYIxx.png


__What are the Project requirements?__ For a primitive: index, query search and
retrieve application, we can go for LlamaIndex. But in the case of applications
where we need to integrate custom workflows, then LangChain is a better choice.

__How simple and accessible is it to use?__ While LlamaIndex gives a simpler
interface, LangChain requires a deeper understanding of NLP concepts and
components.

__How much customization do you want to make?__ LangChain’s has a modular design
that allows for ease in customization and tool integration, However, LlamaIndex
is more of a search and retrieval-based framework.

__In short__ if you were in a dilemma of choosing between them, then consider
asking yourself questions like: __What are the Project requirements? How simple
and accessible is it to use? How much customization do you want to make?__

------

How do LlamaIndex and LangChain differ in their primary focus?
_LangChain’s main focus is the development & deployment of LLMs, along with the
customization of LLMs using fine-tuning methods. However, LlamaIndex aims to
provide an end-to-end ML workflow, along with data management & model
evaluation._

Which platform is better for beginners in machine learning?
_LlamaIndex is more preferrable for beginners due to its simple and intuitive
implementation. As opposed to this, LangChain requires more indepth
understanding of LLMs and NLP concepts._

------

## other references
- [Retrieval Augmented Generation - RAG]({{site.baseurl}}{% post_url 2024/2024-06-06-rag %})
- [RAG usage on an internal knowledge base]({{site.baseurl}}{% post_url 2024/2024-06-04-rag-knowledge-base %})

---
{: data-content="footnotes"}

[^1]: [Choosing the right RAG framework for your LLM: LlamaIndex or LangChain](https://generativeai.pub/choosing-the-right-rag-framework-for-your-llm-llamaindex-or-langchain-a89b9ffd7e41)
