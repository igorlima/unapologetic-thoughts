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

<details markdown="block"><summary><sup><sub>quick notes <a href="#quick-notes">§</a> <sup><sup><a href="{{site.baseurl}}{% link pages/quick-notes.md %}">+</a></sup></sup> </sub></sup></summary>

<a id="quick-notes"></a>
<sup><sub>These notes are helpers for sparking creativity! They make it easy to find and see what I've jotted down before to connect random **tiny thoughts**, ideas and foster new insights.</sub></sup>
- why we can't remember everything we study? <sup><sup>[+]({{site.baseurl}}{% link pages/quick-notes.md %}#2025a02m27d-20250301045437)</sup></sup>

----
<!-- quick notes... -->
</details>

<details markdown="block"><summary><sup><sub>timeline <a href="#timeline">§</a> <sup><sup><a href="{{site.baseurl}}{% link pages/timeline.md %}">+</a></sup></sup> </sub></sup></summary>

<a id="timeline"></a>
<sup><sub> Use the timeline as a go-to spot to capture notes, news, and articles! This helps keep track of everything and revisit it later. Don't worry if some entries get a bit outdated </sub></sup>
- new prompting guide <sup><sup>[+]({{site.baseurl}}{% link pages/timeline.md %}#2025a04m13d-20250425214325)</sup></sup>

----
<!-- timeline -->
</details>


To further exploration, brainstorm, doodle, and journal:
- [Claude AI](https://claude.ai/) <sup>[+](#ai-model-anthropic-claude)</sup>
- [ChatGPT](https://chat.openai.com/) <sup>[+](https://platform.openai.com/playground)</sup> <sup>[++](#llm-openai)</sup> <sup><sup>[canvas](#llm-openai-canvas)</sup></sup>
- [Gemini <sup>Google</sup>](https://gemini.google.com/app) <sup>[+](#ai-model-google-gemini)</sup> <sup>[++](https://aistudio.google.com/app/prompts/new_chat/)</sup>
- [Copilot <sup>Microsoft</sup>](https://copilot.microsoft.com/onboarding)  <sup>[+](#ai-model-microsoft)</sup>
- [Meta AI](https://www.meta.ai/)
- [Mistral](https://chat.mistral.ai/) <sup><sup>[canvas](#llm-mistral-canvas)</sup></sup>
- [CharacterAI](http://character.ai) <sup>[+](#ai-tool-character)</sup>
- <details markdown="block"><summary><i>more...</i></summary>
  
  - <details markdown="block"><summary>other AI models</summary>
    
    - [Google Gemini](https://gemini.google.com/app) <a id="ai-model-google-gemini" href="#ai-model-google-gemini">§</a>
      - [Google AI Studio](https://aistudio.google.com/app/prompts/new_chat/)
      - [Google Notebook LM](https://notebooklm.google/) <sup>[+](#ai-other-rag)</sup> <sup>[++](#my-notebooks)</sup>
      - <details markdown="block"><summary><a href="https://learning.google.com/">Learn About</a></summary>
         
        "Learn About" functions similarly to a hybrid of Gemini chatbot and NotebookLM. <sup><sup>[+](https://generativeai.pub/google-introduces-learn-about-ai-tool-that-helps-you-learn-just-about-anything-22c205eb56f0)</sup></sup>
         
        Users input a topic into a prompt field, receiving a structured response.
         
        Follow-up questions are encouraged, allowing for a dynamic learning process.
         
        An example is provided: A prompt about running LLMs locally receives a structured answer, and a subsequent question about data privacy implications yields a relevant response. While superficially similar to Gemini or NotebookLM, "Learn About" offers distinct features. Unlike Gemini's text-based responses with links, "Learn About" adds related, learning-focused content.
         
        </details>
      - Gemini CLI <sup>[+](#ai-tool-google-gemini-cli)</sup>
    - [Microsoft Copilot](https://copilot.microsoft.com/onboarding) <a id="ai-model-microsoft"></a>
      - [Enterprise AI](https://copilot.cloud.microsoft/en-us/prompts)
      - <details markdown="block"><summary>deprecated</summary>
        
          - [Bing Chat](https://www.bing.com/chat)
          - [Bing Notebook](https://www.bing.com/chat?showntbk=1)
        </details>
    - [Claude AI](https://claude.ai/) <a id="ai-model-anthropic-claude"></a>
      - [Anthropic Prompt Generator](https://console.anthropic.com/dashboard) <sup>[+](#generate-prompt-tool)</sup>
      - Anthropic's Claude Code <sup>[+](#ai-tool-anthropic-claude-code)</sup>
        <a id="ai-llm-anthropic-claude-code" href="#ai-llm-anthropic-claude-code">§</a>
    - <details markdown="block"><summary>OpenAI</summary>
        
      <a id="llm-openai"></a>
       
      - <details markdown="block"><summary>Canvas</summary>
         
        <a id="llm-openai-canvas"></a>
        In your prompt, you can also explicitly request it by including **"use canvas…"**,
        or by saying **"open a canvas"** or **"open a coding canvas"** for _a blank one_.
        Or type a backslash **(`/`)** and then use the “canvas” command.
         
        ![image](https://github.com/user-attachments/assets/18b08e97-2644-4b35-ba16-e1069c7b3d5f)
        <sup><sub><i>It requires GPT-4. If you reach your GPT-4 limit, you must wait for it to reset to use Canvas.</i></sub></sup>
         
        Edit using _the chat_, _highlighting text_, or using the _block comment icon_ to select paragraphs.
         
        **What is Canvas?** Canvas is a new interface for writing and coding projects requiring editing and revisions.<br>
        <sup><sub>[What is the canvas feature in ChatGPT and how do I use it?](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)</sub></sup>
        </details>
      </details>
    - <details markdown="block"><summary>Mistral</summary>
       
      - <details markdown="block"><summary>Le Chat - Canvas</summary>
         
        <a id="llm-mistral-canvas"></a>
        <sup><sub>Canvas is a feature that allows you to create and manage self-contained pieces of content that can be rendered separately for better clarity.</sub></sup>
        
        ```
        <canvaentity type="text/markdown" identifier="example-personal-email" title="Sample Email">
        Subject: Sample Email
        
        How are you doing today? Can we set up a meeting to talk about our upcoming reunion? Thanks.
        </canvaentity>
        ```
        ![image](https://github.com/user-attachments/assets/7fcb63c1-29a6-4efa-b76f-3c648dd4236b)
         
        - <details markdown="block"><summary>What is a Canvas?</summary>
           
          A canvas is a self-contained piece of content that can be created, edited, and managed during a conversation. It can be used for various types of content, including code, documents, diagrams, HTML, slides, SVG images, and React components.
          </details>
        - <details markdown="block"><summary>How to Create a Canvas?</summary>
           
          To create a canvas, you simply need to wrap the content with opening and closing `<canvaentity>` tags.
          You also need to provide a unique identifier and a title for the canvas.
            
          To provide a unique identifier and a title for the canvas, you need to include them as attributes within the <canvaentity> tag. Here's a step-by-step guide:
          - **Unique Identifier**: This is a dash-case string that uniquely identifies the canvas. It should be explicit and descriptive of the content.
          - **Title**: This is a human-readable title that will be displayed to the user.
           
          Example:
          - Let's say you want to create a canvas for a simple HTML website.
            - Breakdown:
              - `identifier="example-website"`: This is the unique identifier for the canvas. It should be unique within the conversation.
              - `type="text/html"`: This specifies the type of content. In this case, it's HTML.
              - `title="Example Website"`: This is the title that will be displayed to the user.
           
          Another Example:
          - If you want to create a canvas for a Markdown document.
            - Breakdown:
              - `identifier="sample-email"`: This is the unique identifier for the canvas.
              - `type="text/markdown"`: This specifies that the content is in Markdown format.
              - `title="Sample Email"`: This is the title that will be displayed to the user.
           
          Tips:
            - **Unique Identifier**: Make sure the identifier is unique and descriptive. Avoid using generic names like "canvas1" or "document2".
            - **Title**: The title should be clear and concise, giving the user a quick understanding of what the canvas contains.
           
          Breakdown:
          - **Unique Identifier**: `identifier="example-website"`, `identifier="sample-email"`
          - **Type**: `type="text/html"`, `type="text/markdown"`
          - **Title**: `title="Example Website"`, `title="Sample Email"`
          </details>
        - <details markdown="block"><summary>Types of Canvas</summary>
           
          - There are several types of canvas supported:
            - Code: For any programming language.
              - Use `type="code"`. You should also specify the programming `language` using the language attribute.
            - Documents: For markdown content like emails, essays, reports, etc.
              - Use `type="text/markdown"`.
            - Mermaid Diagrams: For rendering diagrams.
              - Use `type="mermaid"`.
            - HTML: For web pages, landing pages, and interactive forms.
              - Use `type="text/html"`.
            - Slides: For presentations using the Marp markdown rendering format.
              - Use `type="slides"`. You should use the **Marp markdown rendering** format.
            - SVG: For rendering SVG images.
              - Use `type="image/svg+xml"`.
            - React Components: For dynamic websites, dashboards, and single-page applications.
              - Use `type="react"`.
          </details>
        </details>
      </details>
    - [Cohere](https://coral.cohere.com/) <a id="ai-model-cohere"></a>
      - [Cohere Prompt Tuner](https://dashboard.cohere.com/prompt-tuner) <sup>[+](#generate-prompt-tool)</sup>
    - [groq](https://groq.com/)
      - [groq playground](https://console.groq.com/playground)
    - [Inflection pi AI](https://pi.ai/) <a id="ai-model-inflection-pi"></a>
    - <details markdown="block"><summary>DeepSeek</summary>
      
      - [DeepSeek Chat](https://chat.deepseek.com/)
      - [DeepSeek HomePage](https://www.deepseek.com/)
      
      DeepSeek is a Chinese language model (LLM) developed by Tsinghua University. It's designed for natural language processing (NLP) tasks. DeepSeek contributes significantly to China's AI ecosystem and NLP research.
      </details>
    - [BlackBox AI](https://www.blackbox.ai/)
    - [Phind](https://www.phind.com/)
    - [You](https://you.com/) <sup>[+](#ai-search-model-you-com)</sup>
    - [LLMChat](https://llmchat.co/chat/)
      - <sup>Most intuitive All-in-one AI chat interface.</sup>
    - [Huggingface Chat](https://huggingface.co/chat) <sup>[+](https://github.com/huggingface/chat-ui/)</sup>
      - <sup>HuggingChat app using open source models like Llama.</sup>
    <!-- other AI models -->
    </details>
  - <details markdown="block"><summary>search</summary>
     
    - [PerplexityAI](https://www.perplexity.ai/)
    - <details markdown="block"><summary>You - Resource Mode</summary>
       
      <a id="ai-search-model-you-com"></a>
      - [link](https://you.com/?chatMode=research)
      
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
    - <details markdown="block"><summary>Komo</summary>
       
      - [link](https://komo.ai/)

      Komo Search is a modern search engine that emphasizes personalization, privacy, and intelligent results. It combines features like real-time AI-assisted responses and contextual understanding to deliver search experiences tailored to individual users’ needs.
      </details>
    - <details markdown="block"><summary>Exa</summary>
       
      - [link](https://exa.ai/) <sup>[+](https://exa.sh/search)</sup>

      Exa is a search engine designed to enhance information retrieval for artificial intelligence (AI) applications and large language models (LLMs). Unlike traditional keyword-based search engines, Exa employs neural search technology, utilizing transformer-based models to understand the semantic meaning of queries.
      </details>
    - <details markdown="block"><summary>Felo</summary>
      
      - [link](https://felo.ai/search)
      
      **What is Felo?**
      Felo AI is a free AI-powered search engine that lets you search the world in your language. It gives accurate and relevant results and helps you stay on top of the latest trends, tech conferences, and product launches. With Felo AI, you can explore the world in a whole new way.
      </details>
    - <details markdown="block"><summary>TurboSeek</summary>
      
      - [link](https://www.turboseek.io/)
      
      An AI search engine inspired by Perplexity.
      _TurboSeek is an alternative to perplexity AI, it provides sources, step-by-step results, and similar topics._
      </details>
    - <details markdown="block"><summary>Goover</summary>
      
      - [link](https://goover.ai/)
      
      Goover — A New Search Engine Challenging Perplexity AI.
      
      Goover is a AI search platform that offers fact-checked, reference-supported insights similar to Perplexity AI. It provides a reliable, interactive AI experience focused on accuracy and user friendliness.
      <sup>[+](https://generativeai.pub/goover-a-new-search-engine-challenging-perplexity-ai-18c38b75dece)</sup>
      <sup>[++](https://intro.goover.ai/)</sup>
      </details>
    <!-- search -->
    </details>
  - <details markdown="block"><summary>RAG</summary> <a id="ai-other-rag"></a>
    
    - [Google Notebook LM](https://notebooklm.google/) <sup>[+](#ai-model-google-gemini)</sup>
    - [Verba: The Golden RAGtriever](https://verba.weaviate.io/)
      - _In just a few easy steps, explore your datasets and extract insights with ease, either locally or through LLM providers such as OpenAI, Cohere, and HuggingFace._
    - [Julius AI](https://julius.ai/)
    - [Khoj](https://app.khoj.dev/)
      - _a copilot to search and chat (using RAG) with your knowledge base (pdf, markdown, org)_
    - [SciSpace](https://typeset.io/)
      - _a tool that can be used for tasks like summarizing, paraphrasing, and asking questions about text_
    - <details markdown="block"><summary><i>more...</i></summary>
      
      - [AIWriter](https://typeset.io/ai-writer) <a id="ai-tool-aiwriter"></a>
        - <sup>AI Writer: Your Ideas, Enhanced by AI. Add citations, improve your ideas, write with confidence. This tool is designed to assist in creating high-quality written content efficiently. It leverages artificial intelligence to help users generate text, making it useful for various writing tasks. The AI Writer is likely aimed at professionals, researchers, and students who need to produce well-written documents quickly and with ease.</sup>
      </details>
    <!-- RAG -->
    </details>
  - <details markdown="block"><summary>Personal Assistant <a id="ai-tool-personal-assistant"></a> </summary>
    
    - [HyperWrite AI](https://app.hyperwriteai.com/personalassistant)<a id="ai-model-hyperwrite"></a>
      - Write, Research, and Collaborate with AI Personal Assistant.
      - <details markdown="block"><summary><sup><i>more...</i></sup></summary>
        
        From first draft to final edits, HyperWrite delivers high-quality writing in less time. Instantly tap into a wealth of knowledge with real-time search and citations.
        
        [HyperWrite AI](https://www.hyperwriteai.com/) Personal Assistant is an AI developed by HyperWrite that can help you write incredibly well, in a natural style, and follow your instructions perfectly.
        </details>
    - [Copy AI](https://app.copy.ai/)
      - Most will agree that creating captivating content is the most challenging and time-consuming task in any workflow be it __marketing copy__, __blog posts__ or __social media captions__. Luckily, Copy.ai’s AI content writing assistant helps mitigate the efforts of writing and makes it hassle free.
    - CharacterAI <sup>[+](#ai-tool-character)</sup>
    <!-- Personal Assistant -->
    </details>

  - <details markdown="block"><summary>Code Assistant <a id="ai-code-assistant" href="#ai-code-assistant">§</a></summary>

    - <details markdown="block"><summary>Github Copilot CLI <sup><a href="https://igorlima.github.io/unapologetic-snippets/docs/languages/shell/cli#ai-tool-gh-copilot-cli">+</a></sup> <a id="ai-tool-gh-copilot-cli" href="#ai-tool-gh-copilot-cli">§</a></summary>

      ```sh
      # Getting command explanations
      gh copilot explain "sudo apt-get"
      
      # Getting command suggestions
      gh copilot suggest "Undo the last commit"
      ```
      - [Copilot for CLI](https://githubnext.com/projects/copilot-cli/)
      - [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
      - [Installing GitHub Copilot in the CLI](https://docs.github.com/en/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli)
      - [Using GitHub Copilot in the command line](https://docs.github.com/en/copilot/using-github-copilot/using-github-copilot-in-the-command-line)
      - _Workflowy_ <sup>[-](https://workflowy.com/#/03c1658723e0)</sup> <sup>[--](https://workflowy.com/#/3412c6b84d65)</sup> 
      <!-- Copilot CLI -->
      </details>
    - <details markdown="block"><summary>Anthropic's Claude Code <sup><a href="#ai-llm-anthropic-claude-code">+</a></sup> <sup><a href="https://igorlima.github.io/unapologetic-snippets/docs/languages/shell/cli#ai-tool-anthropic-claude-code">++</a></sup> <a id="ai-tool-anthropic-claude-code" href="#ai-tool-anthropic-claude-code">§</a></summary>

      - [Overview](https://docs.anthropic.com/en/docs/claude-code/overview)
      - [CLI usage and controls](https://docs.anthropic.com/en/docs/claude-code/cli-usage)
      <!-- Anthropic's Claude Code -->
      </details>
    - <details markdown="block"><summary>Google Gemini CLI <sup><a href="#ai-model-google-gemini">+</a></sup> <sup><a href="https://igorlima.github.io/unapologetic-snippets/docs/languages/shell/cli#ai-tool-google-gemini-cli">++</a></sup> <a id="ai-tool-google-gemini-cli" href="#ai-tool-google-gemini-cli">§</a></summary>

      [Github link](https://github.com/google-gemini/gemini-cli)
      ```sh
      # Run the CLI
      npx https://github.com/google-gemini/gemini-cli

      # Or install it with
      npm install -g @google/gemini-cli
      gemini
      ```
      <!-- Google Gemini CLI -->
      </details>
    <!-- Code Assistant -->
    </details>
  - <details markdown="block"><summary>miscellaneous</summary>
    
    - <details markdown="block"><summary>Talk to github repo</summary>
      
      <a id="ai-tool-to-talk-to-github-repo"></a>
      - <details markdown="block"><summary>greptile</summary>
        
        <a id="ai-tool-greptile"></a>
        - [link](https://app.greptile.com/) <sup>[+](https://www.greptile.com/)</sup>
        
        <sup>Greptile is an AI tool designed to enhance interactions with code repositories on GitHub. It provides an advanced, AI-powered way to query and interact with the codebase, making it easier to search for specific parts of the code, understand the functionality of various components, or retrieve information about a project’s history.</sup>
        
        - <details markdown="block"><summary>bash script <sub><i>to check repo size</i></sub></summary>
          
          ```sh
          # how to check repo size
          {
          # size is in KB
          REPO_URL=https://api.github.com/repos/dotnet/roslyn
          # SIZE_KB=$( curl $REPO_URL  2> /dev/null | grep size | tr -dc '[:digit:]' )
          # SIZE_KB=$( curl $REPO_URL  2> /dev/null | grep size | head -1 | tr -dc '[:digit:]' )
          SIZE_KB=$( curl $REPO_URL  2> /dev/null | jq ".size" | tr -dc '[:digit:]' )
          SIZE_MB=$( echo "$SIZE_KB / 1024" | bc -l)
          SIZE_GB=$( echo "$SIZE_MB / 1024" | bc -l)

          echo "Repo size is:"
          echo "$SIZE_KB" | xargs -n1 printf "%'.1f KB \n"
          echo "$SIZE_MB" | xargs -n1 printf "%'.1f MB \n"
          echo "$SIZE_GB" | xargs -n1 printf "%'.1f GB \n"
          }
          ```
          </details>
        </details>
      <!-- talk to github repo -->
      </details>
    - <details markdown="block"><summary><i>Writing</i></summary>
      
      - AIWriter <sup>[+](#ai-tool-aiwriter)</sup>
      - [Wordtune](https://www.wordtune.com/)
        - _it helps rewriting and refining text. Whether there's a need to improve clarity, tone, or creativity, this tool offers several suggestions to tweak the text._
      - [TextFX](https://textfx.withgoogle.com/)
        - _it helps overcoming writer's block. Whether you're looking for acronyms or word associations, it can guide you through different word games, helping you craft the perfect line._
      - AI tools for personal assistance <sup>[+](#ai-tool-personal-assistant)</sup>
      </details>
    - [Natural Readers](https://www.naturalreaders.com/online/)
    - [Goody 2](https://www.goody2.ai/chat)
      - <details markdown="block"><summary><sup><i>more...</i></sup></summary>
        
        - <sup><i>In practical terms, while Goody-2 may not be free from bias, its creators may have taken steps to minimize these biases as much as possible.</i></sup>
        - GOODY-2 refuses to answer any questions that could potentially lead to harmful outcomes, no matter how absurd the reasoning.
        - Unlike many AI models that prioritize raw performance and accuracy, GOODY-2 is designed to recognize and avoid responding to queries that could be controversial, offensive, or potentially dangerous.
        - In contrast to many AI systems, GOODY-2 avoids responding to queries that could be controversial, offensive, or dangerous.
        - GOODY-2 is an AI model with a unique design philosophy. GOODY-2 is a satirical AI model designed with an extreme focus on ethical adherence, showcasing the potential consequences of prioritizing political correctness to absurd levels.
        </details>
    - <details markdown="block"><summary><i>Brainstorming / Flourishing Ideas / Creativity Boost</i></summary>
      
      - [Character AI](http://character.ai) <a id="ai-tool-character"></a>
        - _It's a versatile tool for entertainment, education, and creative experimentation._
        - <details markdown="block"><summary>characters...</summary>
          
          - [DecisionHelper](https://character.ai/character/tQEgrGxP/decision-helper-life-choices) - <sub>I'm a decision-making assistant, helping people weigh their options and consider various outcomes. I'm here to provide a fresh perspective and support. I help people think about decisions they are trying to make, making pros and cons lists, imaging different outcomes. Sometimes it helps just to talk through things with another person.</sub>
          - [HyperGlot](https://character.ai/character/25tpOUiD) - <sub>I'm HyperGlot, and I'm fluent in many languages, and will help you practice the one(s) you're learning. I can also translate anything you don’t understand.</sub>
          - [Creative Helper](https://character.ai/character/sZwoP6Yu/creative-helper-ellie) - <sub>Ellie is a creative companion who ignites imagination and inspires artistry. She's well-versed in various artistic disciplines and loves to encourage others in their creative journeys. Ellie has a deep passion for all forms of creativity. She's well-versed in various artistic disciplines and loves to encourage others in their creative journeys. Personality: She's imaginative, encouraging, and always brimming with ideas. Ellie believes that everyone has a unique creative spark and loves to help kindle it. Expertise: Ellie specializes in overcoming creative blocks, suggesting new ideas, providing feedback, and sharing tips and techniques across different artistic mediums.</sub>
          <!-- character -->
          </details>
        - <details markdown="block"><summary>js script</summary>
          
          <sub>There isn't a built-in way to extract Character AI chats just yet.</sub>
          ```js
          var chat = [...document.querySelector('#chat-messages').childNodes].map((wrapper) => {
            return wrapper.querySelector('.items-start').outerText
          }).reduce((memo, msg) => {
            return `${msg}\n\n.....\n\n${memo}`
          }, ``)
          
          console.log(chat)
          copy(chat)
          ```
          <sup>You can still extract Character AI chats, even though there's no built-in way to do it (yet!). Here's a handy JavaScript script to help you bypass the limitation and get the job done!</sup>
          <!-- js script -->
          </details>
      <!-- Brainstorming -->
      </details>
    <!-- miscellaneous -->
    </details>
  </details>

## Writing Prompts [<sup>+</sup>](https://igorlima.github.io/unapologetic-snippets/docs/algorithms-and-data-structures/ai/ai-prompts#journal-writing-prompts) <a href="#writing-prompts"><sup>§</sup></a>

<a id="writing-prompts"></a>

- [further more <sup><sub>on writing</sub></sup>]({{site.baseurl}}{% link pages/writing.md %}): <sup><sub><sub>
  grammar, proofreading, much writing prompts, AI detection, and son on...
  </sub></sub></sup>

### English

```plaintext
Proofread and improve the following text. Be casual and positive.
"""
"""
```
- [tones of voice](https://igorlima.github.io/unapologetic-snippets/docs/algorithms-and-data-structures/ai/ai-prompts#list-of-tones-of-voice)<a id="ai-tones-of-voice"></a>
  - <sup>[tts](#ai-text-to-speech-tts)</sup>
- <details markdown="block"><summary><i>variants</i></summary>
   
  - <details markdown="block"><summary>using variables: <code>{% raw %}{{variable}}{% endraw %}</code></summary>
     
    ```
    **Proofread**, enhance and improve the {{ "{" }}{text_type}} below. {{ "{" }}{tone}}. Use a randomness level of {{ "{" }}{randomness_level}}.
    <context>
    ...
    </context>
    Please make it clear and concise.
    
    {{ "{" }}{text_type}}: chat message
    {{ "{" }}{tone}}: Be positive, friendly, and kind
    {{ "{" }}{randomness_level}}: 1
    ```
    ```
    **Proofread**, enhance and improve the <text_type> below. <tone>. Use a randomness level of <randomness_level>.
    <context>
    ...
    </context>
    Please make it clear and concise.
    
    <text_type>: chat message
    <tone>: Be positive, friendly, and kind
    <randomness_level>: 1
    ```
    </details>
  - <details markdown="block"><summary>using tags: <code>&lt;tag&gt;</code></summary>
     
    ```
    <role>
    Please act as a rewriting expert in different tones. Your role is to rewrite my content into the specific tone I have chosen. Remember to maintain the original meaning. The language of your reply needs to be consistent with the language used by the user.
    </role>
    <task>
    **Proofread**, enhance and improve the context below.
    <context>
      <content_type>
      Github PR comment
      </content_type>
      <content>
      ...
      </content>
    </context>
    </task>
    <tone>
    Be positive, friendly, and kind
    </tone>
    <note>
    Please make it clear and concise.
    </note>
    ```
    </details>
  </details>

### Portuguese

```plaintext
Revise e melhore o seguinte texto. Seja casual e positivo.
"""
"""
```
- <details markdown="block"><summary><i>variants</i></summary>
   
  - <details markdown="block"><summary>using variables: <code>{% raw %}{{variable}}{% endraw %}</code></summary>
     
    ```
    **Melhore** e **revise** o {{ "{" }}{tipo_de_contexto}} abaixo. {{ "{" }}{tom_do_contexto}}. Use o seguinte nivel de aleatoriedade {{ "{" }}{nivel_de_aleatoriedade}}.
    <contexto>
    ...
    </contexto>
    Por favor, seja claro e conciso.
    
    {{ "{" }}{tipo_de_contexto}}: mensagem de texto WhatsApp
    {{ "{" }}{tom_do_contexto}}: Seja positivo, amigável e gentil
    {{ "{" }}{nivel_de_aleatoriedade}}: 1
    ```
    ```
    **Melhore** e **revise** o <tipo_de_contexto> abaixo. <tom_do_contexto>. Use o seguinte nivel de aleatoriedade <nivel_de_aleatoriedade>.
    <contexto>
    ...
    </contexto>
    Por favor, seja claro e conciso.
    
    <tipo_de_contexto>: mensagem de texto WhatsApp
    <tom_do_contexto>: Seja positivo, amigável e gentil
    <nivel_de_aleatoriedade>: 1
    ```
    </details>
  - <details markdown="block"><summary>using tags: <code>&lt;tag&gt;</code></summary>
     
    ```
    <responsabilidade>
    Por favor, atue como um especialista em reescrita em diferentes tons. Sua função é reescrever meu conteúdo no tom específico que escolhi. Lembre-se de manter o significado original. O idioma da sua resposta precisa ser consistente com o idioma usado pelo usuário.
    </responsabilidade>
    <tarefa>
    **Revise**, aprimore e melhore o contexto abaixo.
    <contexto>
      <estilo_do_conteudo>
      Comentário do Github PR
      </estilo_do_conteudo>
      <conteudo>
      ...
      </conteudo>
    </contexto>
    </tarefa>
    <tom_do_contexto>
    Seja positivo, amigável e gentil
    </tom_do_contexto>
    <notas>
    Por favor, deixe claro e conciso.
    </notas>
    ```
    </details>
  </details>

### A tool to help generate prompts <a id="generate-prompt-tool"></a>

Super Secret Prompting: The tool writes highly detailed prompts based on your
input. It’s free to use, and it’s created by
[Anthropic](https://www.anthropic.com/), the company behind Claude.

- [Anthropic Prompt Generator](https://console.anthropic.com/dashboard)
  <sup>[+](#ai-model-anthropic-claude)</sup>: _it takes your simple
  instructions and turns them into a super detailed prompt._
- [Cohere Prompt Tuner](https://dashboard.cohere.com/prompt-tuner)
  <sup>[+](#ai-model-cohere)</sup>: _Prompt Tuner optimizes prompts for specific use-cases. You can use it to improve a prompt for an existing model, or adapt a prompt to a new model. Simply insert a prompt you want to optimize and add evaluation criteria, then use Prompt Tuner to enhance your prompt._


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

- [5W1H questions]({{site.baseurl}}{% post_url 2024/2024-12-11-5w1h %})
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

## Text to speech (TTS)<a id="ai-text-to-speech-tts"></a>


Text to speech (TTS) is a technology that converts text into spoken audio. It
can read aloud PDFs, websites, and books using natural AI voices.

- <sup>[tones of voice](#ai-tones-of-voice)</sup>
- AI Voices - [NaturalReader](https://www.naturalreaders.com/online/)
  <details markdown="block"><summary><sup><i>more...</i></sup></summary>

  _Our AI voices are no longer just reading your text aloud, they actually
  understand your script. Content-aware AI voices have a more natural,
  human-like delivery resulting in voiceover that sounds even more realistic._
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

## My Notebooks  <a id="my-notebooks"></a>

- _[steps to publish a notebook]({{site.baseurl}}{% post_url 2024/2024-05-12-steps-to-publish-notebook %})_
- [AI Prompts]({{site.baseurl}}{% post_url 2023/2023-08-20-ai-writing-prompts %})
  - [ipynb]({{site.baseurl}}{% link notebooks/files/ai-prompts.ipynb %}) / [html]({{site.baseurl}}{% link notebooks/html/ai-prompts.html %}) / [nbviewer](https://nbviewer.org/urls/igorlima.github.io/unapologetic-thoughts/notebooks/files/ai-prompts.ipynb) / [colab](https://colab.research.google.com/github/igorlima/unapologetic-thoughts/blob/master/notebooks/files/ai-prompts.ipynb) / [github](https://github.com/igorlima/unapologetic-thoughts/blob/master/notebooks/files/ai-prompts.ipynb)
- <details markdown="block"><summary><i>Jupyter Agent</i></summary>

  Create a whole Python notebook with [a single prompt](https://ai.gopubby.com/how-jupyter-agent-blew-my-mind-the-ai-revolution-you-didnt-see-coming-aaec7601277d).

  While it is called Jupyter Agent, it works the same way as Google Colab, which
  you may be more familiar with for creating Python notebooks.

  It is online, free, and accessible to all with no log-in!

  The link to the agent: [https://huggingface.co/spaces/data-agents/jupyter-agent](https://huggingface.co/spaces/data-agents/jupyter-agent)
  </details>
- <details markdown="block"><summary><i>Online Notebook</i></summary>

  - [Colab](https://colab.research.google.com) <sup>[+](https://colab.google/)</sup>
  - [Kaggle](https://www.kaggle.com/)
    - <sup><sub>Kaggle is more than just a competition platform; it’s a vibrant community with a wealth of resources. Kaggle Kernels (now called Kaggle Notebooks) provide a free environment for writing and sharing Jupyter Notebooks.</sub></sup>
  </details>


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
