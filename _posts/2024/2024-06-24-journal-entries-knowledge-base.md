---
layout: post
title: AI Knowledge Base for Journal Entries
category: sketch
---

## Data Structure

<details markdown="block">
<summary><i>text sample</i></summary>

```
- 00h00 title of the entry
  - Mood: what is your mood?
  - Energy Level: how is your energy level?
  - I feel a sense of satisfaction today. It's rewarding to see that some
    efforts, even those from years ago, eventually pay off.
    - A side project I developed about two years ago to simplify sending
      content to my Kindle has unexpectedly proven valuable today. I'm now able
      to leverage that knowledge to explore and cultivate ideas related to AI.
      - By combining my past learnings with new AI knowledge, I've successfully
        automated a workflow to streamline my thoughts and ideas. It's exciting
        to see how past projects can fuel present innovation.
- 00h01 title of the entry
  - Mood: what is your mood?
  - Energy Level: how is your energy level?
  - I feel a sense of satisfaction today. It's rewarding to see that some
    efforts, even those from years ago, eventually pay off.
    - A side project I developed about two years ago to simplify sending
      content to my Kindle has unexpectedly proven valuable today. I'm now able
      to leverage that knowledge to explore and cultivate ideas related to AI.
      - By combining my past learnings with new AI knowledge, I've successfully
        automated a workflow to streamline my thoughts and ideas. It's exciting
        to see how past projects can fuel present innovation.
```
</details>

## Python Snippet

<details markdown="block">
<summary><i>a snippet</i></summary>

```
import re

def group_by_indent(chunks):
  result = []
  for chunk in chunks:
    if chunk[0] == 0:
      result.append([chunk[1]])
    else:
      result[-1].append(chunk[1])
    chunk[2] = len(result) - 1
  return result

def extract_chunks(text):
  splitted = text.split('\n')

  indent_width = 0
  chunks = []
  indent_char = '-'
  for line in splitted:
    indent = re.search(f'^(?P<indent>[ ]*)[{indent_char}]', line)
    if indent:
      width = len(indent.group('indent'))
      indent_width = width
      # index 0 is the indent width
      # index 1 is the text
      # index 2 is the parent
      chunks.append([indent_width, re.sub(f'^[{indent_char}]', '', line.strip()).strip(), -1])

    subindent = re.search(f'^(?P<indent>[ ]{{{indent_width}}})', line)
    if not indent and indent_width > 0 and subindent:
      width = len(subindent.group('indent'))
      chunks[-1][1] += f' {line.strip()}'
  return chunks

def add_parent(chunks):
  parents = group_by_indent(chunks)
  for chunk in chunks:
    chunk[2] = parents[chunk[2]]

chunks = extract_chunks(text)
print(chunks)
print(group_by_indent(chunks))
add_parent(chunks)
print(chunks)

N = 7
print(f"""
index: {N}

indent: {chunks[N][0]}

chunk: {chunks[N][1]}

parent: {' '.join(chunks[N][2])}
""")

print('\n'.join(chunks[3][2]))
```
</details>

<details markdown="block">
<summary><i><code>main.py</code></i></summary>

```
import pudb, re
from pprint import pprint as pp

text = '''
- 00h00 title of the entry
  - Mood: what is your mood?
  - Energy Level: how is your energy level?
  - I feel a sense of satisfaction today. It's rewarding to see that some
    efforts, even those from years ago, eventually pay off.
    - A side project I developed about two years ago to simplify sending
      content to my Kindle has unexpectedly proven valuable today. I'm now able
      to leverage that knowledge to explore and cultivate ideas related to AI.
      - By combining my past learnings with new AI knowledge, I've successfully
        automated a workflow to streamline my thoughts and ideas. It's exciting
        to see how past projects can fuel present innovation.
- 00h01 title of the entry
  - Mood: what is your mood?
  - Energy Level: how is your energy level?
  - I feel a sense of satisfaction today. It's rewarding to see that some
    efforts, even those from years ago, eventually pay off.
    - A side project I developed about two years ago to simplify sending
      content to my Kindle has unexpectedly proven valuable today. I'm now able
      to leverage that knowledge to explore and cultivate ideas related to AI.
      - By combining my past learnings with new AI knowledge, I've successfully
        automated a workflow to streamline my thoughts and ideas. It's exciting
        to see how past projects can fuel present innovation.
'''

def group_by_indent(chunks):
  result = []
  for chunk in chunks:
    if chunk[0] == 0:
      result.append([chunk[1]])
    else:
      result[-1].append(chunk[1])
    chunk[2] = len(result) - 1
  return result

def extract_chunks(text):
  splitted = text.split('\n')

  indent_width = 0
  chunks = []
  indent_char = '-'
  for line in splitted:
    indent = re.search(f'^(?P<indent>[ ]*)[{indent_char}]', line)
    if indent:
      width = len(indent.group('indent'))
      indent_width = width
      # index 0 is the indent width
      # index 1 is the text
      # index 2 is the parent
      chunks.append([indent_width, re.sub(f'^[{indent_char}]', '', line.strip()).strip(), -1])

    subindent = re.search(f'^(?P<indent>[ ]{{{indent_width}}})', line)
    if not indent and indent_width > 0 and subindent:
      width = len(subindent.group('indent'))
      chunks[-1][1] += f' {line.strip()}'
  return chunks

def add_parent(chunks):
  parents = group_by_indent(chunks)
  for chunk in chunks:
    chunk[2] = parents[chunk[2]]

chunks = extract_chunks(text)
pp(chunks)
pp(group_by_indent(chunks))
add_parent(chunks)
pp(chunks)

N = 7
print(f"""
index: {N}

indent: {chunks[N][0]}

chunk: {chunks[N][1]}

parent: {' '.join(chunks[N][2])}
""")

print('\n'.join(chunks[3][2]))
```
</details>

### Output

<details markdown="block">
<summary><i>chunks output</i></summary>

```
chunks
[[0, '00h00 title of the entry', -1],
 [2, 'Mood: what is your mood?', -1],
 [2, 'Energy Level: how is your energy level?', -1],
 [2,
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  -1],
 [4,
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  -1],
 [6,
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.',
  -1],
 [0, '00h01 title of the entry', -1],
 [2, 'Mood: what is your mood?', -1],
 [2, 'Energy Level: how is your energy level?', -1],
 [2,
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  -1],
 [4,
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  -1],
 [6,
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.',
  -1]]
```
</details>

<details markdown="block">
<summary><i>parents</i></summary>

```
parents
[['00h00 title of the entry',
  'Mood: what is your mood?',
  'Energy Level: how is your energy level?',
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.'],
 ['00h01 title of the entry',
  'Mood: what is your mood?',
  'Energy Level: how is your energy level?',
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.']]
```
</details>

<details markdown="block">
<summary><i>chunk with parent</i></summary>

```
chunks with parents
[[0,
  '00h00 title of the entry',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  'Mood: what is your mood?',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  'Energy Level: how is your energy level?',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [4,
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [6,
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.',
  ['00h00 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [0,
  '00h01 title of the entry',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  'Mood: what is your mood?',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  'Energy Level: how is your energy level?',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [2,
  "I feel a sense of satisfaction today. It's rewarding to see that some "
  'efforts, even those from years ago, eventually pay off.',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [4,
  'A side project I developed about two years ago to simplify sending content '
  "to my Kindle has unexpectedly proven valuable today. I'm now able to "
  'leverage that knowledge to explore and cultivate ideas related to AI.',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']],
 [6,
  "By combining my past learnings with new AI knowledge, I've successfully "
  "automated a workflow to streamline my thoughts and ideas. It's exciting to "
  'see how past projects can fuel present innovation.',
  ['00h01 title of the entry',
   'Mood: what is your mood?',
   'Energy Level: how is your energy level?',
   "I feel a sense of satisfaction today. It's rewarding to see that some "
   'efforts, even those from years ago, eventually pay off.',
   'A side project I developed about two years ago to simplify sending content '
   "to my Kindle has unexpectedly proven valuable today. I'm now able to "
   'leverage that knowledge to explore and cultivate ideas related to AI.',
   "By combining my past learnings with new AI knowledge, I've successfully "
   "automated a workflow to streamline my thoughts and ideas. It's exciting to "
   'see how past projects can fuel present innovation.']]]
```
</details>

<details markdown="block">
<summary><i>chunk index 7 output</i></summary>

```
index: 7

indent: 2

chunk: Mood: what is your mood?

parent: 00h01 title of the entry Mood: what is your mood? Energy Level: how is your energy level? I feel a sense of satisfaction today. It's rewarding to see that some efforts, even those from years ago, eventually pay off. A side project I developed about two years ago to simplify sending content to my Kindle has unexpectedly proven valuable today. I'm now able to leverage that knowledge to explore and cultivate ideas related to AI. By combining my past learnings with new AI knowledge, I've successfully automated a workflow to streamline my thoughts and ideas. It's exciting to see how past projects can fuel present innovation.
```
</details>

## References

- [AI Knowledge Base for Messages]({{site.baseurl}}{% post_url 2024/2024-06-01-message-knowledge-base %})

---
{: data-content="footnotes"}

[^1]: [...](...)
