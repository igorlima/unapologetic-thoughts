# USING VERTEXAI API WITH OPENAI LIBRARY
from openai import OpenAI
import pudb; # pu.db
import os

"""
# pip3 show openai
# pip3 index versions openai
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I openai==1.58.1

python3 -m venv my-test-env-2025a01m04d
source my-test-env-2025a01m04d/bin/activate
pip3 install openai==1.58.1
pip3 install pudb
"""

GOOGLE_PROJECT_ID=os.getenv("GOOGLE_PROJECT_ID")
GOOGLE_LOCATION=os.getenv("GOOGLE_LOCATION")
# https://igorlima.github.io/unapologetic-snippets/docs/languages/containerization/docker-samples#vertexai-gemini-rest-api
VERTEXAI_TOKEN=os.getenv("VERTEXAI_TOKEN")
client = OpenAI(
  base_url=f"https://{GOOGLE_LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{GOOGLE_PROJECT_ID}/locations/{GOOGLE_LOCATION}/endpoints/openapi",
  api_key=VERTEXAI_TOKEN,
)
"""
Authenticate with Vertex AI generative AI API in cloud functions

11:25pm on Thu, Jan 9

- https://stackoverflow.com/questions/76621780/authenticate-with-vertex-ai-generative-ai-api-in-cloud-functions -

- https://stackoverflow.com/questions/69843556/how-do-i-get-access-token-inside-node-js-google-cloud-function/69895524#69895524 -

- https://github.com/googleapis/google-auth-library-python -

- https://googleapis.dev/python/google-auth/latest/ -

- https://pypi.org/project/google-auth-oauthlib/ -
"""

#  CHAT COMPLETIONS API
response = client.chat.completions.create(
  # https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library#supported-gemini-models
  model="google/gemini-1.5-flash",
  n=1,
  messages=[{
    "role": "system", "content": "You are a helpful assistant."
  }, {
    "role": "user",
    "content": "Explain to me how AI works"
  }]
)
print(response.choices[0].message.content)
print('\n' + '-'*50 + '\n')

# STREAMING
response = client.chat.completions.create(
  model="google/gemini-1.5-flash",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True
)
for chunk in response:
  print(chunk.choices[0].delta.content)
print('\n' + '-'*50 + '\n')

"""
REFERENCE:
  Call Vertex AI models by using the OpenAI library
    https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/call-vertex-using-openai-library

HOW TO RUN THIS SCRIPT:
({
export GOOGLE_PROJECT_ID=xxxxxxx
export GOOGLE_LOCATION=xxxxxxxxx
export VERTEXAI_TOKEN=xxxxxxxx
python3 vertexai-with-openai-library-compatibility.py
})
"""
