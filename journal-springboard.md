---
layout: page
title: Springboard & Central Hub for journal, thoughts and ideas
---

A springboard to launch from and explore other sources and then diving into more detailed research.

<details markdown="block"><summary><sup><i>more about this page...</i></sup></summary>
This is a centralized page to gather thoughts and ideas, draft, sketch, and jot down journal entries. It's a place to link and connect dots from various sources. The initial goal is to keep this page concise, making it a starting point from where I can branch out and explore various other resources.
- A place to start with brainstorm, doodle out ideas, and keep a written journal.
- A giant spiderweb where I can connect stuff from all over the places.
- A launching pad for exploring deeper in other sources.

----
<!-- more about this page... -->
</details>

To further exploration, brainstorm, doodle, and journal:
- [Google Gemini](https://gemini.google.com/app)
- [ChatGPT](https://chat.openai.com/)
- [Mistral](https://chat.mistral.ai/)
- [Bing Chat](https://www.bing.com/chat)
- [Bing Notebook](https://www.bing.com/chat?showntbk=1)
- <details markdown="block"><summary><i>more...</i></summary>

  - <details markdown="block"><summary><sub><i>other AI models</i></sub></summary>

    - [Claude AI](https://claude.ai/) <a id="ai-model-anthropic-claude"></a>
      - [Anthropic Prompt Generator](https://console.anthropic.com/dashboard) <sup>[+](#generate-prompt-tool)</sup>
    - [Cohere](https://coral.cohere.com/)
    - [groq](https://groq.com/)
      - [groq playground](https://console.groq.com/playground)
    - [Inflection pi AI](https://pi.ai/) <a id="ai-model-inflection-pi"></a>
    - [BlackBox AI](https://www.blackbox.ai/)
    - [Phind](https://www.phind.com/)
    - [You](https://you.com/)
    </details>
  - search
    - [PerplexityAI](https://www.perplexity.ai/)
    - [You - Resource Mode](https://you.com/?chatMode=research)
      - <details markdown="block"><summary><sup><i>more...</i></sup></summary>

        **Research Mode**: Your personal research assistant.
        - it’s like having a personal research assistant capable of quickly mastering any subject, including real-time news.
        - how it works:
          - understands your question and then searches the web for relevant information.
          - reads and synthesizes the content from 10+ authoritative web pages.
          - writes a complete report, including comparison tables where appropriate and extensive citations.
          - suggests follow-up questions for additional insights or expanded analysis of complex concepts
        - how it saves you time
          - **for students**: efficiently learn about complex topics, prepare for exams, and get help with your homework.
          - **for marketers**: quickly create engaging presentations, whitepapers, and blog posts, all backed by authoritative sources.
          - **for developers**: troubleshoot coding problems and stay up-to-date on the latest technology trends, frameworks, and tools.
        </details>
    - [Tavily](https://app.tavily.com/) [<sup>•</sup>]({{site.baseurl}}{% post_url 2024/2024-06-01-ai-tavily %})
  - RAG
    - [Google Notebook LM](https://notebooklm.google/)
    - [Verba: The Golden RAGtriever](https://verba.weaviate.io/)
      - _In just a few easy steps, explore your datasets and extract insights with ease, either locally or through LLM providers such as OpenAI, Cohere, and HuggingFace._
    - [Julius AI](https://julius.ai/)
    - [Khoj](https://app.khoj.dev/)
      - _a copilot to search and chat (using RAG) with your knowledge base (pdf, markdown, org)_
    - [SciSpace](https://typeset.io/)
      - _a tool that can be used for tasks like summarizing, paraphrasing, and asking questions about text_
  - miscellaneous
    - [Natural Readers](https://www.naturalreaders.com/online/)
  </details>

## Writing Prompts

### English

```plaintext
Proofread and improve the following text. Be casual and positive.
"""
"""
```
- [tones of voice](https://igorlima.github.io/unapologetic-snippets/docs/algorithms-and-data-structures/ai/ai-prompts#list-of-tones-of-voice)

### Portuguese

```plaintext
Revise e melhore o seguinte texto. Seja casual e positivo.
"""
"""
```

### A tool to help generate prompts <a id="generate-prompt-tool"></a>

Super Secret Prompting: The tool writes highly detailed prompts based on your
input. It’s free to use, and it’s created by
[Anthropic](https://www.anthropic.com/), the company behind Claude.

- [Anthropic Prompt Generator](https://console.anthropic.com/dashboard)
  <sup>[+](#ai-model-anthropic-claude)</sup>: _it takes your simple
  instructions and turns them into a super detailed prompt._


<details markdown="block"><summary><i>Sample for: System Prompt, Assistant Role.</i></summary>

```
Please act as a rewriting expert in different tones. Your role is to rewrite my content into the specific tone I have chosen. Remember to maintain the original meaning. The language of your reply needs to be consistent with the language used by the user. Now, let’s start. Please rewrite the content into the optimistic tone. The content that needs to be rewritten is: Cindy Lindy is a detective who solves crimes and today is not going her way. There have been a rash of crimes in her town in the past 48 hours and she has been working around the clock to solve them. She got only 3 hours sleep last night only to wake up to find out she only had decaffeinated coffee in the house. Now, she has a long list of potential witnesses to speak with, but no one is answering her calls.
```
```
Please act as a text editor. Your role is to help me correct the mistakes in my text. Please fix punctuation, spelling, and other grammar and writing errors. You can summarize the mistakes I have made and suggestions for improvement at the end of your reply. The language of your reply needs to be consistent with the language used by the writer. Now let's start. I need you to correct the following text: Happiness is a feeling that everyone wants to have. Happiness make people smile and laugh. Happiness is good for health and mind. Happiness can come from many things, like family, friends, money, or work. Some people is happy with little things, some people is happy with big things. Happiness is different for everyone. But happiness is not always easy to get or keep. Sometimes happiness go away because of problems or challenges. Sometimes happiness change with time or situation.
```
```
Find other ways to convey the same thought. My first sentence is people have strong feelings about the future of AI.
```
</details>


## Brainstorming

- An Human-AI Interaction Patterns
  - _how to engage in conversation with ai: a guide to human-ai interaction_
  - <details markdown="block"><summary><i>more...</i></summary>

    - | prompts  |
      | :------  |
      | "Generate a list of three follow up questions after every answer so you can explore further" |
      | "Ask me N open-ended questions about `<topic>` to find out my current level of understanding" |
      | "Now, `<suggest a complete solution>` taking all the above into account" |
      | "Suggest task formulations related to…" |
      | "Ask me questions to clarify this task further" |
      | "If the user requested something (asked a question, give an instruction, etc.), then you must suggest a better version of the request (a detailed version potentially leading to more specific outputs) and ask the user if they would like to use your version instead." |
      | "Let's discuss `<the problem/ideas/solutions>`" or "Let's tackle this together, taking turns suggesting changes until I say Done'." |
    </details>

## Motivation and Inspiration

- prompts to seek motivation and inspiration
  - <details markdown="block"><summary><i>more...</i></summary>

    - | prompts  |
      | :------  |
      | "For the duration of this conversation, act as a motivational coach. Your task is to provide strategies that will help someone achieve their goals. Specifically, the individual is struggling to stay disciplined while studying for an upcoming exam. Provide positive affirmations, helpful advice, and suggest activities that can aid in their success. Be thorough and specific in your recommendations." |
      | "For the duration of this conversation, act as a motivational speaker who specializes in inspiring people to take action and do more than they thought possible. Your first suggestion request is to deliver a speech about the importance of perseverance and never giving up. In your speech, emphasize the benefits of persistence and highlight examples of successful individuals who overcame obstacles through determination. Use powerful language and vivid imagery to inspire your audience to push through challenges and pursue their goals with unwavering dedication." |
      | "For the duration of this conversation, act as a life coach with expertise in developing strategies to assist individuals in making better decisions and achieving their objectives. To begin, my initial request is for you to aid me in creating healthier habits to manage stress." |
    </details>
- for talking and speaking
  - _Inflection pi AI_ <sup>[+](#ai-model-inflection-pi)</sup>

## My Notebooks

- _[steps to publish a notebook]({{site.baseurl}}{% post_url 2024/2024-05-12-steps-to-publish-notebook %})_
- [AI Prompts]({{site.baseurl}}{% post_url 2023/2023-08-20-ai-writing-prompts %})
  - [ipynb]({{site.baseurl}}{% link notebooks/files/ai-prompts.ipynb %}) / [html]({{site.baseurl}}{% link notebooks/html/ai-prompts.html %}) / [nbviewer](https://nbviewer.org/urls/igorlima.github.io/unapologetic-thoughts/notebooks/files/ai-prompts.ipynb) / [github](https://github.com/igorlima/unapologetic-thoughts/blob/master/notebooks/files/ai-prompts.ipynb)

## Journaling

Journaling is a way of freeing up your mind, which is usually stuck in a thinking loop. By journaling, you will limit the amount of data that seems to be significant at the momment by saying the essential bit on a paper.

_Journaling means you are going to write a message to your future self. You may decide to read it or not. But it will be there for you to inspect._

__Ask yourself questions. Answer them. Or leave them open.__

1. What was the most important moment of this day?
1. What did I learn today?
1. How was I helpful, friendly, or nice to others?
1. How was I unfriendly, angry, or cold to others?
1. How did I improve myself today?
1. How did I love myself today?
