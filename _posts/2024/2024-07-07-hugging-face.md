---
layout: post
title: Hugging Face
category: code-sample
---

Hugging Face is a hub that aims to provide democratical access to several
pre-training __models__ for a variety of tasks, such as translation,
summarization, question answering, object detection, image segmentation and
more. _It encorauges the users to contribute to open-source models._

The beauty of this centralized repository is Hugging Face __Transformers__, a
very popular Python library that enables to download, load and fine-tune models
easily.

In addition to models, it also hosts __datasets__ and machine learning demos,
called __Hugging Face Spaces__.

In Hugging Face, there are three main components: __models__, __datasets__ and
__spaces__.

If you go the [model’s page](https://huggingface.co/models), you may feel
overwhelmed due to the huge variery of open-source __models__. It’s recommended
to first identify the task you want to solve and, then, filter by this task.
After selecting the task, you can sort the models based on different criterias,
like Trending and Most Downloads.

To get access to Hugging Face’s models and datasets in your notebook, you first
need the __Hugging Face API key__.

<details markdown="block">
<summary><i>setup</i></summary>

```
python3 -m venv my-hf-env
source my-hf-env/bin/activate

export HF_TOKEN=your_token
```

</details>

<details markdown="block">
<summary><i>sample A</i></summary>

An introductionary guide that can help you to getting started with Hugging
Face. Transformers is the python library that enables to get access to
state-of-art models, especially NLP models, easily. [^1]

```sh
pip3 install transformers==4.42.3
pip3 install torch==2.3.1
```

```python
from transformers import pipeline
import torch

translator = pipeline(
  task="translation",
  model="facebook/nllb-200-distilled-600M",
  torch_dtype=torch.bfloat16 
)

text = """
ChatGPT developer OpenAI has introduced a new tool that it says can reproduce
human voices with just a short audio sample.  The tool is among several
developed by technology companies that aim to clone voices with a high level of
exactness.  The system is called Voice Engine. OpenAI released details about
Voice Engine on March 29.
"""

text_translated = translator(
  text,
  src_lang="eng_Latn",
  tgt_lang="por_Latn"
)

print(text_translated[0]['translation_text'])
```

Useful resources:
- [Hugging Face’s Documentation](https://huggingface.co/docs/transformers/main/en/quicktour#pipeline)
- [Hugging Face Free Course](https://www.youtube.com/watch?v=00GKzGyWFEs&list=PLo2EIpI_JMQvWfQndUesu0nPBAtZ9gP1o)
- [Open Source Models with Hugging Face Course](https://learn.deeplearning.ai/courses/open-source-models-hugging-face)

----

</details>

<details markdown="block">
<summary><i>sample B</i></summary>

From Pixels to Paragraphs[^2].

```sh
pip3 install transformers==4.42.3
pip3 install torch==2.3.1
pip3 install pillow==10.4.0
pip3 install torchvision==0.18.1 einops==0.8.0 timm==1.0.7
```

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

model_id = "vikhyatk/moondream2"
revision = "2024-03-06"
model = AutoModelForCausalLM.from_pretrained(
  model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

image = Image.open('photo.jpg')
enc_image = model.encode_image(image)


query = "Describe this image."
response = model.answer_question(enc_image, query, tokenizer)
print(response)
"""
A woman is depicted in this image, wearing a blue dress and standing on a
platform. Another woman is seated on a wooden plank, with a bag beside her.
The background features a body of water.
"""


query = "How is the weather?"
response = model.answer_question(enc_image, query, tokenizer)
print(response)
"""
The weather in the image is sunny.
"""


query = "How many people are there in the photo?"
response = model.answer_question(enc_image, query, tokenizer)
print(response)
"""
2
"""
```

----

</details>

---
{: data-content="footnotes"}

[^1]: [A Comprehensive Guide for Getting Started with Hugging Face](https://pub.towardsai.net/a-comprehensive-guide-for-getting-started-with-huggingface-94aeea38692f)
[^2]: [Exploring Hugging Face: Image-Text-to-Text](https://towardsdev.com/exploring-hugging-face-image-text-to-text-e037c83cb7ab)
