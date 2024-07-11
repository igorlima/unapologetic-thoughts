---
layout: post
title: jekyll markdown internal links
category: technical
---

There is no need to include the file extension when using the `post_url` tag.

- `[Some Link]({% raw %}{% post_url 2010-07-21-name-of-post %}{% endraw %})` [^1] [^2]
  - if you want to include a link to a post on your site, the `post_url` tag will generate the correct permalink URL for the post you specify.
    - `{% raw %}{% post_url 2010-07-21-name-of-post %}{% endraw %}`
  - if you organize your posts in subdirectories, you need to include subdirectory path to the post:
    - `{% raw %}{% post_url /subdir/2010-07-21-name-of-post %}{% endraw %}`


###  __troubleshooting__

- [post_url generates urls without baseurl](https://github.com/jekyll/jekyll/issues/8887)
  - _the `post_url` and `link` tags prefixes `site.baseurl` from Jekyll 4.0 onward._
  - _`{% raw %}{% post_url ... %}{% endraw %}` is meant for posts only. For everything else, please use `{% raw %}{% link ... %}{% endraw %}`_
  - _`{% raw %}[article 1]({{site.baseurl}}/{% post_url DATE-article1.md %}){% endraw %}`_

# Other Resources

- [other Jekyll resources]({{site.baseurl}}{% post_url 2024/2024-07-11-jekyll %})

---
{: data-content="footnotes"}

[^1]: [Jekyll Documentation](https://jekyllrb.com/docs/liquid/tags/#linking-to-posts)
[^2]: [Jekyll PR](https://github.com/jekyll/jekyll/pull/369)
