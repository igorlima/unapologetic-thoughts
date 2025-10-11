# GEMIMG
"""
Lightweight wrapper for generating and editing images from Gemini 2.5 Flash Image/Nano Banana
- https://github.com/minimaxir/gemimg -
"""

"""
# mkdir $(date +%Ya%mm%dd-%Hh%Mm)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
pip3 install -U gemimg==0.2.0
pip3 install --upgrade --force-reinstall gemimg
pip3 list
pip3 show gemimg
pip3 index versions gemimg
"""

# -------------------------- #
# IMAGE GENERATION FROM TEXT #
# -------------------------- #
from gemimg import GemImg

# configure the client with your API key if needed
# import os
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# g = GemImg(api_key=GEMINI_API_KEY)
g = GemImg()
gen = g.generate("A kitten with prominent purple-and-green fur.", save_dir="./output")

prompt = """
Create an image of a three-dimensional pancake in the shape of a skull, garnished on top with blueberries and maple syrup.
"""
gen = g.generate(prompt, save_dir="./output")

# ---------------------------------------- #
# IMAGE EDITING WITH TEXT AND IMAGE INPUTS #
# ---------------------------------------- #
edit_prompt = """
Make ALL of the following edits to the image:
- Put a strawberry in the left eye socket.
- Put a blackberry in the right eye socket.
- Put a mint garnish on top of the pancake.
- Change the plate to a plate-shaped chocolate-chip cookie.
- Add happy people to the background.
"""
gen_edit = g.generate(edit_prompt, gen.image, save_dir="./output")

# ------------------------------------- #
# IMAGE GENERATION WITH DETAILED PROMPT #
# ------------------------------------- #
prompt = """
Create an image featuring three specific kittens in three specific positions.
All of the kittens MUST follow these descriptions EXACTLY:
- Left: a kitten with prominent black-and-silver fur, wearing both blue denim overalls and a blue plain denim baseball hat.
- Middle: a kitten with prominent white-and-gold fur and prominent gold-colored long goatee facial hair, wearing a 24k-carat golden monocle.
- Right: a kitten with prominent #9F2B68-and-#00FF00 fur, wearing a San Franciso Giants sports jersey.
Aspects of the image composition that MUST be followed EXACTLY:
- All kittens MUST be positioned according to the "rule of thirds" both horizontally and vertically.
- All kittens MUST lay prone, facing the camera.
- All kittens MUST have heterochromatic eye colors matching their two specified fur colors.
- The image is shot on top of a bed in a multimillion-dollar Victorian mansion.
- The image is a Pulitzer Prize winning cover photo for The New York Times with neutral diffuse 3PM lighting for both the subjects and background that complement each other.
- NEVER include any text, watermarks, or line overlays.
"""
gen = g.generate(prompt, aspect_ratio="16:9", save_dir="./output")

"""
HOW TO RUN THIS SCRIPT:
({
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
python3 gemini-nano-banana-gemimg.py
})

GENERATE AN API KEY
Follow these steps:
- In Google AI Studio, click Get API key in the left navigation panel.
  - https://aistudio.google.com/
- On the next page, click Create API key.
  - https://aistudio.google.com/apikey
- Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.
"""
