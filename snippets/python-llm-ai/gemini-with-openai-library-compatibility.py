# USING GEMINI API WITH OPENAI LIBRARY
from openai import OpenAI
import pudb; # pu.db
import os

"""
# pip3 show openai
# pip3 index versions openai
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I openai==1.58.1

python3 -m venv my-test-env-2024a12m22d
source my-test-env-2024a12m22d/bin/activate
pip3 install openai==1.58.1
pip3 install pudb
"""

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = OpenAI(
  api_key=GEMINI_API_KEY,
  base_url="https://generativelanguage.googleapis.com/v1beta/"
)

#  CHAT COMPLETIONS API
response = client.chat.completions.create(
  model="gemini-1.5-flash",
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
  model="gemini-1.5-flash",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True
)
for chunk in response:
  print(chunk.choices[0].delta.content)
print('\n' + '-'*50 + '\n')

# EMBEDDING
response = client.embeddings.create(
  input="Your text string goes here",
  model="text-embedding-004"
)
print(response.data[0].embedding)

"""
REFERENCE:
  Gemini in the House: How to Use Google’s AI Powerhouse with OpenAI Library (and Why You Might Want To)
    https://ai.gopubby.com/gemini-in-the-house-how-to-use-googles-ai-powerhouse-with-openai-library-and-why-you-might-want-a64b1bcdbae8

HOW TO RUN THIS SCRIPT:

({
export GEMINI_API_KEY="XXXXXXXXXXXXXXXXXXXX"
python3 gemini-with-openai-library-compatibility.py
})
"""
