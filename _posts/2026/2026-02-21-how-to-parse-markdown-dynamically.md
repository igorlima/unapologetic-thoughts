---
layout: post
title: A markdown parser and compiler
category: technical
---

_Injecting dynamically and Formatting Code in Markdown._

Below is the implementation of a script that fetches a code snippet, processes it as Markdown, and renders it with syntax highlighting in HTML. The script uses the following tools:

1. **[Marked](https://github.com/markedjs/marked)**: A fast and flexible Markdown parser and compiler.
2. **[Marked-Highlight](https://www.npmjs.com/package/marked-highlight)**: A plugin for `marked` that integrates syntax highlighting.
3. **[Highlight.js](https://github.com/highlightjs/highlight.js)**: A JavaScript library for syntax highlighting.


## How It Works

1. **Loading Dependencies**:
   - The script loads the `marked`[^1] library for parsing Markdown and the `highlight.js` library[^2] for syntax highlighting.
   - The `marked-highlight` plugin[^3] is used to integrate `highlight.js` with `marked`.

2. **Fetching the Code Snippet**:
   - The `fetch` API retrieves a YAML file from a remote repository.
   - The content of the file is then wrapped in Markdown code block syntax (```` ```yaml ````).

3. **Parsing and Rendering**:
   - The `marked.parse` method converts the Markdown content into HTML.
   - The resulting HTML is injected into a `div` element with the ID `code-block.tmuxp.unapologetic-world.yaml`.

4. **Syntax Highlighting**:
   - The `highlight.js` library is used to apply syntax highlighting to the code block.


## Why Use This Approach?

- **Dynamic Content Injection**: This method allows you to **dynamically** fetch and render code snippets, making it ideal for documentation or tutorials that rely on external code examples.
- **Improved Readability**: Syntax highlighting enhances the readability of code, making it easier for readers to understand.
- **Flexibility**: The combination of `marked` and `highlight.js` provides a flexible and customizable solution for rendering Markdown content.

{% raw %}
```html
<div id="code-block.tmuxp.unapologetic-world.yaml" class="language-bash highlighter-rouge"></div>
<script src="https://cdn.jsdelivr.net/npm/marked/lib/marked.umd.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked-highlight/lib/index.umd.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/yaml.min.js"></script>
<script>
  /*
  A markdown parser and compiler. Built for speed:
  - https://github.com/markedjs/marked
  - https://marked.js.org/
  - https://github.com/markedjs/marked-highlight
  - https://www.npmjs.com/package/marked-highlight
  JavaScript syntax highlighter for code blocks in Markdown:
  - https://github.com/highlightjs/highlight.js
  - https://highlightjs.org/
  - https://highlightjs.readthedocs.io/en/latest/readme.html#in-the-browser
  */
  const { Marked } = globalThis.marked;
  const { markedHighlight } = globalThis.markedHighlight;
  const marked = new Marked(
    markedHighlight({
          emptyLangClass: 'hljs',
      langPrefix: 'hljs language-',
      highlight(code, lang, info) {
        const language = hljs.getLanguage(lang) ? lang : 'plaintext';
        return hljs.highlight(code, { language }).value;
      }
    })
  );
  return
  // fetch('{{site.baseurl}}{% link snippets/bash/tmuxp/tmuxp.unapologetic-world.yaml %}')
  fetch('https://raw.githubusercontent.com/igorlima/unapologetic-thoughts/refs/heads/master/snippets/bash/run-script-only-once-at-time.sh')
    .then(response => response.text())
    .then(data => {
      const markdownCode = `\`\`\`yaml\n${data}\`\`\``;
      const htmlContent = marked.parse(markdownCode); // Convert Markdown to HTML
      document.getElementById('code-block.tmuxp.unapologetic-world.yaml').innerHTML = `
        <div class="highlight">
          <pre class="highlight">
            <code>${data}</code>
          </pre>
        </div>
      `;
      document.getElementById('code-block.tmuxp.unapologetic-world.yaml').innerHTML = `
        <div class="highlight">
          ${htmlContent}
        </div>
      `;
    });
</script>
```
{% endraw %}

---
{: data-content="footnotes"}

[^1]: [A markdown parser and compiler](https://github.com/markedjs/marked)
[^2]: [JavaScript syntax highlighter for code blocks in Markdown](https://github.com/highlightjs/highlight.js)
[^3]: [Add code highlighting to marked](https://github.com/markedjs/marked-highlight)
