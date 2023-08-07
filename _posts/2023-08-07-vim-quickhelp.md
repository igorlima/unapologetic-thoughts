---
layout: post
title: VIM quick help
category: technical
---

How to scape special characteres before sending it to Polly

- Polly - text to speech
  - EN: `<c-b>p1`
  - PT: `<c-b>p2`


```vim
:silent! %s/!/\./gc
:%s/%/percent/gc
:%s/#//gc
:%s/`/'/gc
```

```vim
:silent! %s/!/\./gc | silent! %s/%/percent/gc | silent! %s/#//gc | silent! %s/`/'/gc
```

---
{: data-content="footnotes"}

[^1]: none
