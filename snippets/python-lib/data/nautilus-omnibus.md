# Daily Planner 

The basic idea is to organize the day into events and tasks.

-------

## Calendar 2025

_One page calendar for: **2025**_

| - | - | - | - | - | - | - | - | - | - | - | - |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| . | . | . | . | . |Jun|Sep|Apr|Jan|May|Aug|Feb|
| . | . | . | . | . |   |Dec|Jul|Oct|   |   |Mar|
| . | . | . | . | . |   |   |   |   |   |   |Nov|
| - | - | - | - | - | - | - | - | - | - | - | - |
| 1 | 8 | 15| 22| 29|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
| 2 | 9 | 16| 23| 30|Mon|Tue|Wed|Thu|Fri|Sat|Sun|
| 3 | 10| 17| 24| 31|Tue|Wed|Thu|Fri|Sat|Sun|Mon|
| 4 | 11| 18| 25|   |Wed|Thu|Fri|Sat|Sun|Mon|Tue|
| 5 | 12| 19| 26|   |Thu|Fri|Sat|Sun|Mon|Tue|Wed|
| 6 | 13| 20| 27|   |Fri|Sat|Sun|Mon|Tue|Wed|Thu|
| 7 | 14| 21| 28|   |Sat|Sun|Mon|Tue|Wed|Thu|Fri|

-------

### Tasks

- [ ] task lorem ipsum
    - [ ] subtask lorem ipsum dolor sit amet
    - [ ] subtask lorem ipsum dolor sit amet
- [ ] task lorem ipsum
    - [ ] subtask lorem ipsum dolor sit amet
    - [ ] subtask lorem ipsum dolor sit amet
- [ ] task lorem ipsum
    - [ ] subtask lorem ipsum dolor sit amet
    - [ ] subtask lorem ipsum dolor sit amet
- [ ] task lorem ipsum
    - [ ] subtask lorem ipsum dolor sit amet
    - [ ] subtask lorem ipsum dolor sit amet

-------

### Events

| Time  | Event | Task |
| :---  | :---- | :--- |
| 05:00 | event | task |
| 06:00 | event | task |
| 07:00 | event | task |
| 08:00 | event | task |
| 09:00 | event | task |
| 10:00 | event | task |
| 11:00 | event | task |
| 12:00 | event | task |
| 13:00 | event | task |
| 14:00 | event | task |
| 15:00 | event | task |
| 16:00 | event | task |
| 17:00 | event | task |
| 18:00 | event | task |
| 19:00 | event | task |
| 20:00 | event | task |
| 21:00 | event | task |
| 22:00 | event | task |
| 23:00 | event | task |
| 00:00 | event | task |

-------

## Journal

Ask yourself questions. Answer them. Or leave them open.
[+](https://igorlima.github.io/unapologetic-thoughts/journal-springboard#journaling)

1. What was the most important moment of this day?
2. What did I learn today?
3. How was I helpful, friendly, or nice to others?
4. How was I unfriendly, angry, or cold to others?
5. How did I improve myself today?
6. How did I love myself today?

-------

## My Lambda Ideas Hub

This session is my go-to spot for refreshing my thoughts about the personal
automation tools I've drafted. Let me dive into each one!

- **PROMPT-TO-EMAIL**
    - **description**: transforms a TXT file into Kindle-ready content,
      including proofread and journal entries. The MyAiPrompt2 layer powers it.
    - **triggers**: `lambda/ai/llm/*.prompt.txt`, `lambda/ai/llm/*.proofread.txt`, `lambda/ai/llm/*.journal.txt`
        - _it sends the output via email_
- **MY-PY-MU-PDF**
    - **description**: extracts text from PDFs.
    - **triggers**: from `*.llm.pdf` to `*pdf.txt`
        - `lambda/ai/ocr/*.llm.pdf`, `lambda/ai/ocr/pdf-to-img-then-ocr/*.img.pdf`
- **OCR-TO-EMAIL**
    - **description**: reads text from PDFs and images and sends it to your Kindle. The MyAiOCR layer is responsible for this
    - **triggers**: `lambda/ai/ocr/*.png`, `lambda/ai/ocr/*.jpg`, `lambda/ai/ocr/*.heic`, `lambda/ai/ocr/*.PNG`, `lambda/ai/ocr/*.JPG`, `lambda/ai/ocr/*.HEIC`, `lambda/ai/ocr/*.list.ocr`, `lambda/ai/ocr/*.llm.pdf.txt`
- **MD-TO-KINDLE**
    - **description**: converts Markdown to Kindle formats.
    - **triggers**: `*.s2k.md`, `*.s2k-html.md`, `*.s2k-epub.md`, `*.s2k-epub-chapters.md`
- **SEND-TO-KINDLE**
    - **description**: sends texts directly to Kindle.
    - **triggers**: `*.s2k.txt`
- **PDF-TO-KINDLE**
    - **description**: sends PDF to Kindle as an attachment.
    - **triggers**: `*.s2k.pdf`
- **TTS-TO-EMAIL**
    - **description**: creates audio from text.
    - **triggers**: `lambda/ai/tts/*.ai.txt`, `lambda/ai/txt/*.en.txt`, `lambda/ai/txt/*.pt.txt`, `lambda/ai/*.fredo.txt`
- **AI-PROMPT**
    - **description**: generates AI content upon an HTTP, and sends output via email. It uses the MyAiPrompt layer.
    - **triggers**: API Gateway
- **SEND-ME-SMS**
    - **description**: sends SMS.
    - **triggers**: API Gateway
- **SEND-ME-EMAIL**
    - **description**: sends email.
    - **triggers**: API Gateway
- **SEND-ATTACHMENT**
    - **description**: sends attachment via email.
    - **triggers**: API Gateway

-------

## Nautilus Omnibus

- [web app](https://nautilus-omnibus.web.app/)
    - :: [ilima thoughts](https://thoughts.ilima.xyz/) :: [ilima snippets](https://snippets.ilima.xyz/) ::
    - :: [raw md](https://raw.githubusercontent.com/igorlima/unapologetic-thoughts/refs/heads/master/snippets/python-lib/data/nautilus-omnibus.md) :: [raw code](https://raw.githubusercontent.com/igorlima/unapologetic-thoughts/refs/heads/master/snippets/python-lib/markdown-conversion-xml2epub.py) ::

![Nautilus Omnibus A](./data/nautilus-omnibus-1.jpg)

![Nautilus Omnibus B](./data/nautilus-omnibus-2.jpg)


### Examples

**Example 1**
```
Start using Nautilus
x Finish a task by x
Change default task duration 60min
9:30-11am Add some fixed-time event
Recolor important task to red with !
16-17:20 Relax
Review what you accomplished
Click on Example 2
```

**Example 2**
```
[ ] Use brackets for tasks to add a typical markup
  This row is just a note – Nautilus ignores 
  rows starting with two spaces
[x] Finish tasks by inserting the x
[ ] Control task progress by adding the indicator d50% 90m
  The task will be narrower and dotted. This one is half-done.
[ ] Click on the task in spiral! 60m
[x] Add a timestamp like d10:30 to a finished task
  The task will be grayed and anchored in the spiral at the 
  specified time.

15:35-16:15 Try: 24h as format works too
4:30-5pm Afternoon meeting with notes:

  ...and as you see, you can add empty lines too!
```

-------

