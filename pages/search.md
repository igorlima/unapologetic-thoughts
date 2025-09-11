---
layout: page
title: Search
---

This is an example search page!

Reference:
- [Talk to github repo using AI]({{site.baseurl}}{% link journal-springboard.md %}#ai-tool-to-talk-to-github-repo)
- <details markdown="block"><summary>Leveraging <strong>AIChat for RAG</strong> with ILIMA THOUGHTS <a href="#aichat-rag-rc-knowledge-base"> §</a></summary>

  <a id="aichat-rag-rc-knowledge-base"></a>

  **Leveraging AIChat for RAG with a GitHub Repository**

  This guide demonstrates how to use AIChat's built-in vector database and full-text search capabilities to create a knowledge base from an entire GitHub repository. This enables Retrieval-Augmented Generation (RAG), allowing AIChat to provide more informed and contextually relevant responses based on the repository's content.

  **Creating a RAG Knowledge Base from a GitHub Repository**

  Follow these steps to create a RAG knowledge base using AIChat:

  1.  **Initiate RAG:** Use the following command within AIChat, replacing `ilima-thoughts` with your desired RAG name:

      ```
      > .rag ilima-thoughts
      ```

  2.  **Configure Embedding Model:** AIChat will prompt you to select an embedding model. Choose the appropriate model based on your needs. For example:

      ```
      > Select embedding model: gemini:text-embedding-004 (max-tokens:2048; max-batch:100; price:0)
      ```

  3.  **Set Chunk Size and Overlay:** Configure the chunk size and overlay for optimal retrieval performance.  Experiment with these values to find what works best for your repository.

      ```
      > Set chunk size: 1500
      > Set chunk overlay: 100
      ```

  4.  **Add Documents:**  Specify the paths to the relevant directories within your GitHub repository.  This example uses the `unapologetic-thoughts` repository.  Adjust the paths to match your repository's structure.  Use the `**` wildcard to include all files within the specified directories.

      ```
      > Add documents: https://github.com/igorlima/unapologetic-thoughts/tree/master/_posts/**; https://github.com/igorlima/unapologetic-thoughts/tree/master/snippets/**; https://github.com/igorlima/unapologetic-thoughts/tree/master/pages/**; https://github.com/igorlima/unapologetic-thoughts/tree/master/notebooks/**
      ```

  5.  **Exit RAG Configuration:**  Once you've added all the desired documents, exit the RAG configuration mode.

      ```
      @ilima-thoughts> .exit rag
      ```

  **Managing Your RAG Knowledge Base**

  AIChat provides several commands for managing your RAG knowledge base:

  *   **View Citation Sources:**  After a query, use the following command to see the sources used in the last query:

      ```
      .sources rag
      ```
      This helps you understand where AIChat is getting its information.

  *   **Edit Documents:**  Add or remove documents from an existing RAG knowledge base:

      ```
      .edit rag-docs
      ```

  *   **Rebuild RAG:**  After making changes to the documents in your repository, rebuild the RAG knowledge base to reflect those changes:

      ```
      .rebuild rag
      ```

  *   **Show RAG Information:**  View information about your RAG knowledge base, such as the number of documents and the embedding model used:

      ```
      .info rag
      ```

  **Further Resources**

  * **AIChat RAG Guide:**  For a more in-depth explanation, refer to the official [AIChat RAG Guide](https://github.com/sigoden/aichat/wiki/RAG-Guide) <sup>[+](https://github.com/sigoden/aichat/wiki/RAG-Guide/900d5644a72b33a0adba0e420bc3e645177a9f68)</sup>.
  * Leveraging *AIChat RAG* with Your RC File: [Configuration Assistance Made Easy]({{site.baseurl}}{% link pages/dots-mapping.md %}#aichat-rag-rc-knowledge-base)
  * Leveraging *AIChat RAG* with [ILIMA SNIPPETS](https://igorlima.github.io/unapologetic-snippets/docs/search.html)
  * Using RAG internally with the _**quick-notes**_ markdown <sup>[+]({{site.baseurl}}{% link pages/quick-notes.md %}#2025a09m11d-20250911143229)</sup>
  <br> <br>
  </details>

- <details markdown="block"><summary>Fuse JS</summary>

  - [FuseJS Home Page](https://www.fusejs.io/)
  - [Fuse Live Demo](https://www.fusejs.io/demo.html)
  - [Fuse options documentation](https://www.fusejs.io/api/options.html)
  </details>

- the following __vim__ hint is helpful when enabling the option to include the matches - `includeMatches: true`.
  - to move the cursor to a match position, use the one character in the [search pattern](https://learnbyexample.gitbooks.io/vim-reference/content/Regular_Expressions.html) `/.` and then move the `N` characters ahead by repeating the last search from the cursor's position.
    - to go to the `Nth` match in the file: type the amount of movement to go ahead, then press the `n` - eg. `78n` `250n`.
    - the dot `.` matches any character except the new line.

<div class="live-demo" style="width: 100%; margin: 0%;">
  <p>Search</p>
  <input type="text" id="search" style="width: 100%; height: 30px;">
  <div id="html" style="margin-top: 2%;"></div>
  <p>Config</p>
  <textarea id="config" rows="18" style="width: 100%;" wrap="off">
  {
    // isCaseSensitive: false,
    includeScore: true,
    shouldSort: true,
    // includeMatches: false,
    // findAllMatches: false,
    // minMatchCharLength: 1,
    // location: 0,
    threshold: 0.3,
    distance: 10000,
    // useExtendedSearch: false,
    // ignoreLocation: false,
    // ignoreFieldNorm: false,
    // fieldNormWeight: 1,
    keys: [
      "title._text",
      "content._text"
    ]
  }
  </textarea>
  <p>JSON</p>
  <textarea id="json" rows="4" style="width: 100%;" disabled wrap="off"></textarea>
  <p>Results</p>
  <textarea id="results" rows="4" style="width: 100%;" disabled wrap="off"></textarea>
</div>

<script>
// data:text/html, <html contenteditable>
;(async function() {
  const CTX = {}
  console.log('loading scripts...')
  await Promise.all([
    // https://lodash.com/docs/4.17.21
    // 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.21/lodash.min.js',
    // https://caolan.github.io/async/v3/docs.html
    // 'https://cdnjs.cloudflare.com/ajax/libs/async/3.2.4/async.min.js',

    // https://www.jsdelivr.com/package/npm/xmltojson
    // CTX.xmlToJSON.parseString('<xml><a>It Works!</a></xml>')
    ['https://cdn.jsdelivr.net/npm/xmltojson@1.3.5/lib/xmlToJSON.min.js', 'xmlToJSON'],
    // https://cdnjs.com/libraries/x2js
    // https://cdnjs.cloudflare.com/ajax/libs/x2js/1.2.0/xml2json.js
    // ...

    // Fuzzy Search
    // https://stackoverflow.com/questions/23305000/javascript-fuzzy-search-that-makes-sense
    // https://github.com/atom/fuzzaldrin/
    // https://github.com/farzher/fuzzysort
    // 'https://cdn.jsdelivr.net/npm/fuzzysort@2.0.4/fuzzysort.min.js',
    // ...
    // https://fusejs.io/demo.html
    // https://github.com/krisk/Fuse
    // https://fusejs.io/getting-started/installation.html
    ['https://cdn.jsdelivr.net/npm/fuse.js/dist/fuse.min.js', 'Fuse'],
  ].map(value => {
    const [scriptLink, funcName] = ((value) => {
      if (typeof value === 'string') {
        return [value, null]
      } else if (Array.isArray(value)) {
        return value
      }
      return []
    })(value)
    return fetch(scriptLink).then(response => response.text()).then(script => [script, funcName])
  })).then((scripts) => {
    scripts.forEach(([script, funcName]) => {
      ;(function(script, funcName) {
        if (!script) return;
        const result = eval(`${script};${funcName}`);

        if (!funcName) return;
        CTX[funcName] = result;
        // eval(`this['${funcName}'] = ${funcName}`)
      }.call(CTX, script, funcName));
    })
  }).catch(err => {
    console.error(err)
    throw err
  })
  console.log('scripts loaded!!')

  console.log('loading xml...')
  const xml = await fetch('{{site.baseurl}}/feed.xml').then(
    response => response.text()
  ).then(xml => {
    return xml
  }).catch(err => {
    console.error(err)
    throw err
  })
  console.log('xml loaded!!')

  const json = CTX.xmlToJSON.parseString(xml)
  document.querySelector('#json').textContent = JSON.stringify(json, null, 2 )

  // https://www.w3schools.com/jsref/obj_event.asp
  document.querySelector('#search').addEventListener("input", function (elem) {
    const options = (function () {
      const result = eval(`const config=${document.querySelector('#config').value};config;`);
      return result
    }).call({})

    const list = json.feed[0].entry
    const fuse = new CTX.Fuse(list, options);
    const pattern = elem.target.value
    const results = fuse.search(pattern)

    html.textContent = null
    results.forEach(({item} = {}) => {
      const {
        link: [{
          _attr: {
            href: {_value: link}
          }
        }],
        id: [{_text: idlink}],
        title: [{_text: title}],
        content: [{_text: content}]
      } = item

      const html = document.querySelector('#html')
      html.insertAdjacentHTML( 'beforeend', `
        <div style=" display: flex; flex-direction: column; ">
          <a href="${link}">${title}</a>
          <div style="height: 150px; overflow-x: hidden; overflow-y: auto;">${content}</div>
        </div>
        <br/>
      `)
    })
    document.querySelector('#results').value = JSON.stringify(results, null, 2)
  });
}());
</script>
