# HOW TO BUILD WITH NANO BANANA: Gemini 2.5 Flash Image
"""
Google has recently released Gemini 2.5 Flash Image, a powerful new model for
image generation and editing, also known by its codename, Nano Banana. This
model introduces state-of-the-art capabilities for creating and manipulating
images, unlocking a wide range of new applications.

You can now build interactive, multimodal applications with powerful creative
control that goes far beyond simple text-to-image.
- Maintain character consistency: Preserve a subject’s appearance across
  multiple generated images and scenes.
- Perform intelligent editing: Enable precise, prompt-based edits like
  inpainting (adding/changing objects), outpainting, and targeted
  transformations within an image.
- Compose and merge images: Intelligently combine elements from multiple images
  into a single, photorealistic composite.
- Leverage multimodal reasoning: Build features that understand visual context,
  such as following complex instructions on a hand-drawn diagram.

DOCUMENTATION
Explore all model capabilities and get advanced prompting tips.
- https://ai.google.dev/gemini-api/docs/image-generation

COOKBOOKS
Find more examples and code samples in the cookbook guide.
- https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Image_out.ipynb

BEST PRACTICES and prompting tips for Nano Banana
To achieve the best results with Nano Banana, follow these prompting
guidelines:
- Be Hyper-Specific: The more detail you provide about subjects, colors,
  lighting, and composition, the more control you have over the output.
- Provide Context and Intent: Explain the purpose or desired mood of the image.
  The model's understanding of context will influence its creative choices.
- Iterate and Refine: Don't expect perfection on the first try. Use the model's
  conversational ability to make incremental changes and refine your image.
- Use Step-by-Step Instructions: For complex scenes, break your prompt into a
  series of clear, sequential instructions.
- Use Positive Framing: Instead of negative prompts like "no cars," describe
  the desired scene positively: "an empty, deserted street with no signs of
  traffic."
- Control the Camera: Use photographic and cinematic terms to direct the
  composition, such as "wide-angle shot", "macro shot", or "low-angle
  perspective".

CUT YOUR GEMINI API COSTS BY 50% 
Cut costs and enjoy higher throughput rate limits by batching multiple images
in a single request and automating image generation tasks.
- https://ai.google.dev/gemini-api/docs/batch-api
"""

"""
# mkdir $(date +%Ya%mm%dd-%Hh%Mm)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
pip3 install -U google-genai==1.36.0
pip3 install Pillow==11.3.0
pip3 install --upgrade --force-reinstall google-genai
pip3 list
pip3 show google-genai
pip3 index versions google-genai
"""

# -------------------------- #
# IMAGE GENERATION FROM TEXT #
# -------------------------- #
from google import genai
from PIL import Image
from io import BytesIO

# configure the client with your API key if needed
# import os
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=GEMINI_API_KEY)
client = genai.Client()

prompt = """Create a photorealistic image of an orange cat
with a green eyes, sitting on a couch."""

# Call the API to generate content
response = client.models.generate_content(
  model="gemini-2.5-flash-image-preview",
  contents=prompt,
)
# The response can contain both text and image data.
# Iterate through the parts to find and save the image.
for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("output/cat.png")

# ---------------------------------------- #
# IMAGE EDITING WITH TEXT AND IMAGE INPUTS #
# ---------------------------------------- #
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()
prompt = """Using the image of the cat, create a photorealistic,
street-level view of the cat walking along a sidewalk in a
New York City neighborhood, with the blurred legs of pedestrians
and yellow cabs passing by in the background."""

image = Image.open("output/cat.png")
# Pass both the text prompt and the image in the 'contents' list
response = client.models.generate_content(
  model="gemini-2.5-flash-image-preview",
  contents=[prompt, image],
)
for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("output/cat2.png")

# ---------------------------------- #
# WORKING WITH MULTIPLE INPUT IMAGES #
# ---------------------------------- #
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()
prompt = "Make these two cats wear a t-shirt and hug each other."
image1 = Image.open("output/cat.png")
image2 = Image.open("output/cat2.png")
response = client.models.generate_content(
  model="gemini-2.5-flash-image-preview",
  contents=[prompt, image1, image2],
)
for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("output/cats-with-tshirt.png")

# ---------------------------- #
# CONVERSATIONAL IMAGE EDITING #
# ---------------------------- #
from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()
# Create a chat
chat = client.chats.create(
  model="gemini-2.5-flash-image-preview"
)
# Make the first image edit
response1 = chat.send_message([
  "Change the cat to a bengal cat, leave everything else the same",
  Image.open("output/cat.png"),
])
# Display / save image...
for part in response1.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("output/cat-bengal.png")
# Continue chatting and editing
response2 = chat.send_message("The cat should wear a funny party hat")
# Display / save image...
for part in response2.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
  elif part.inline_data is not None:
    image = Image.open(BytesIO(part.inline_data.data))
    image.save("output/cat-bengal-party-hat.png")

"""
HOW TO RUN THIS SCRIPT:
({
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
python3 gemini-nano-banana-image-generation.py
})

GENERATE AN API KEY
Follow these steps:
- In Google AI Studio, click Get API key in the left navigation panel.
  - https://aistudio.google.com/
- On the next page, click Create API key.
  - https://aistudio.google.com/apikey
- Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.
"""
