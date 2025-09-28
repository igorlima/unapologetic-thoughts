# HOW TO BUILD WITH VEO 3
"""
You can now generate high-fidelity, 720p videos with native audio using Veo 3
and Veo 3 Fast, available in paid preview in the Gemini API.

Veo 3 brings your prompts to life, creating 8-second videos with native audio.
It lets you generate video from a text prompt, an initial image, or a
combination of both to guide the style and starting frame. It can create a wide
range of visual styles and natively generate dialogue in multiple languages, as
well as sound effects and ambient noise.

REFERENCES:
  - https://ai.google.dev/gemini-api/docs/video
"""

"""
# mkdir $(date +%Ya%mm%dd-%Hh%Mm)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
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

import time
from google import genai

# configure the client with your API key if needed
# import os
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=GEMINI_API_KEY)
client = genai.Client()
prompt = """
A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'
"""
# Start the generation job
operation = client.models.generate_videos(
  # https://ai.google.dev/gemini-api/docs/video?example=dialogue#model-versions
  # model="veo-3.0-generate-001",
  # model="veo-3.0-generate-preview",
  model="veo-3.0-fast-generate-preview",
  prompt=prompt,
)
# Poll for the result
while not operation.done:
  print("Waiting for video generation to complete...")
  time.sleep(10)
  operation = client.operations.get(operation)
# Download the final video
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("output/dialogue_example.mp4")
print("Generated video saved to dialogue_example.mp4")

"""
HOW TO RUN THIS SCRIPT:
({
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
python3 gemini-veo3-video-genaration.py
})

GENERATE AN API KEY
Follow these steps:
- In Google AI Studio, click Get API key in the left navigation panel.
  - https://aistudio.google.com/
- On the next page, click Create API key.
  - https://aistudio.google.com/apikey
- Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.
"""
