---
layout: post
title: sketch drafting and design
category: sketch
---

- categories:
  - speaking
  - likebility
  - writing
  - inspiration
  - [technical]({{site.baseurl}}{% post_url 2013-01-01-technical %}) [^1]
    - [internal absolute html]({{site.baseurl}}{% link editable.html %}) [^2]
  - code-sample [^4]
    - <details markdown="block">
      <summary><i>a sample for a piece of block</i></summary>

      ```
      <details markdown="block">
      <summary><i>...</i></summary>

      </details>
      ```
      </details>
    - <details markdown="block">
      <summary><i>a sample raw block</i></summary>

      ```
      {{ "{" }}% raw %}
      ...
      {{ "{" }}% endraw %}
      ```
      {% raw %}
      ```
      <tag> ... </tag>
      ```
      {% endraw %}
      </details>
  - sketch

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. [^3]

```js
const a = 10
function a () {
  return 0
}
```

```javascript
const a = 10
function a () {
  return 0
}
```

---
{: data-content="footnotes"}

[^1]: [internal link]({{site.baseurl}}{% post_url 2023/2023-03-30-internal-links %})
[^2]: [another internal link]({{site.baseurl}}{% link editable.html %})
[^3]: it's a footnote
[^4]: [jekyll reference]({{site.baseurl}}{% post_url 2024/2024-07-11-jekyll %})
