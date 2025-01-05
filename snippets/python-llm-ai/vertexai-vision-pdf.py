# VertexAI Sample For extracting text from PDF files
import os
import pudb; # pu.db
import vertexai
from vertexai.generative_models import GenerativeModel, Part

"""
# pip3 show openai
# pip3 index versions openai
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I openai==1.58.1

python3 -m venv my-test-env-2025a01m04d
source my-test-env-2025a01m04d/bin/activate

# To use the Vertex GAPIC clients, please install the `google-cloud-aiplatform`
# PyPi package by running `pip install google-cloud-aiplatform`.
# 
# To use the Vertex AI SDK, please install the `vertexai` PyPi package by running
# `pip install vertexai`.
# 
# https://pypi.org/project/vertexai/
# https://www.piwheels.org/project/vertexai/
# https://www.piwheels.org/project/google-cloud-aiplatform/
pip3 install google-cloud-aiplatform==1.75.0
pip3 install pudb
"""

VISION_MODEL_PROMPT ="""
Convert the following PDF page to markdown.
Return only the markdown with no explanation text. Do not include deliminators like '''markdown.

RULES:
- You MUST include all information on the page. Do NOT exclude headers, footers, or subtext.
- Charts & infographics must be interpreted to a markdown format
- Non text based images must be replaced with [Description of image](image.png)
"""

PROJECT_ID=os.environ["GOOGLE_PROJECT_ID"]
LOCATION=os.environ["GOOGLE_LOCATION"]
vertexai.init(project=PROJECT_ID, location=LOCATION)
# https://cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-pdf#generativeaionvertexai_gemini_pdf-python
# https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference
# https://cloud.google.com/vertex-ai/docs/start/install-sdk
def extract_text_vertexai(file_path, model_id = None):
  with open(file_path, "rb") as file:
    doc_bytes = file.read()
  model = GenerativeModel(model_id)
  pdf_file = Part.from_data(
    data=doc_bytes,
    mime_type="application/pdf",
  )
  contents = [pdf_file, VISION_MODEL_PROMPT]
  response = model.generate_content(contents)
  return response.text

print(extract_text_vertexai("data/vision-pdf-test.pdf", model_id="gemini-1.5-flash-002"))

"""
REFERENCE:
  Call Vertex AI models by using the OpenAI library
    https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library#curl
  Generate content with the Gemini Enterprise API
    https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#request

HOW TO RUN THIS SCRIPT:

({
export GOOGLE_APPLICATION_CREDENTIALS="./data/credentials.json"
export GOOGLE_PROJECT_ID=xxxxxxxxxy
export GOOGLE_LOCATION=xxxxxxxxz
python3 vertexai-vision-pdf.py
})
"""
