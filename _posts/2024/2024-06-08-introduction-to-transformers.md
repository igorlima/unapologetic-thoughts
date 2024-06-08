---
layout: post
title: AI - a brief introduction to transformers
category: code-sample
---

In its most basic sense, the transformer is an encoder-decoder style model.

The encoder converts an input into an abstract representation which the decoder
uses to iteratively generate output. [^1]

![image](https://github.com/igorlima/unapologetic-thoughts/assets/1886786/516718b1-51fb-43fb-9c88-48d693412358)
<sup><i>high level representation of how the output of the encoder relates to the decoder</i></sup> [^1]

Generally speaking, encoder-only style models are good at extracting
information from text for tasks like classification and regression, while
decoder-only style models focus on generating text. GPT, being a model focused
on text generation, is a decoder only style model.

GPT-1 uses a text and position embedding, which converts a given input word
into a vector which encodes both the words general meaning and the position of
the word within the sequence.

GPT is an abbreviation of “Generative Pre-Trained Transformer” for a reason.
GPT is pre-trained on a vast amount of text using language modeling (next word
prediction). It essentially learns __“given an input sequence X, the next word
should be Y."__


Other training strategies: [^1]
- Supervised Learning is the process of training a model based on labeled
  information. When training a model to predict if images contain cats or dogs,
  for instance, one curates a set of images which are labeled as having a cat
  or a dog, then trains the model (using gradient descent) to understand the
  difference between images with cats and dogs
- Unsupervised Learning is the process of giving some sort of model unlabeled
  information, and extracting useful inferences through some sort of
  transformation of the data. A classic example of unsupervised learning is
  clustering; where groups of information are extracted from un-grouped data
  based on local position.
- Self-supervised learning is somewhere in between. Selfsupervision uses labels
  that are generated programmatically, not by humans. In some ways it’s
  supervised because the model learns from labeled data, but in other ways it’s
  unsupervised because no labels are provided to the training algorithm. Hence
  selfsupervised


---
{: data-content="footnotes"}

[^1]: [GPT — Intuitively and Exhaustively Explained](https://towardsdatascience.com/gpt-intuitively-and-exhaustively-explained-c70c38e87491)
