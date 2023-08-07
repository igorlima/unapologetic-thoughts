---
layout: post
title: VIM quick help
category: technical
---

How to scape special characteres before sending it to Polly

```vim
:silent! %s/!/\./gc
:%s/%/percent/gc
:%s/#//gc
:%s/`/'/gc
```

```vim
:silent! %s/!/\./gc | %s/%/percent/gc | %s/#//gc | %s/`/'/gc
```

---
{: data-content="footnotes"}

[^1]: none
