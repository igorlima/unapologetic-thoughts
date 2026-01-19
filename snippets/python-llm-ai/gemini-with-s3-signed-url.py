# How I use Gemini on my PDF files using Python
"""
# mkdir $(date +%Ya%mm%dd-%Hh%Mm)
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

python3 -m venv my-test-env-2026a01m18d 
source my-test-env-2026a01m18d/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
pip3 install pudb
pip3 install -U google-genai==1.56.0
pip3 install -U boto3==1.42.30
pip3 install --upgrade --force-reinstall google-genai
pip3 install --no-cache --upgrade-strategy eager -I google-genai==1.56.0
pip3 list
pip3 show google-genai
pip3 index versions google-genai
"""

import os
import boto3
from botocore.config import Config
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html
# https://github.com/boto/botocore/issues/2109#issuecomment-1305284157
# https://stackoverflow.com/questions/26533245/the-authorization-mechanism-you-have-provided-is-not-supported-please-use-aws4
my_config = Config(
  region_name=os.getenv('AWS_REGION'),
  signature_version = 'v4',
  retries = {
    'max_attempts': 10,
    'mode': 'standard'
  }
)

# Generate a signed S3 object URL.
s3 = boto3.client(
  's3',
  aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS"),
  config=my_config,
)
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/generate_presigned_url.html
signed_url = s3.generate_presigned_url(
  'get_object',
  Params={
    'Bucket': 'my-bucket-name',
    'Key': 'document.pdf',
  },
  HttpMethod='GET',
  ExpiresIn=3600
)
print("Signed URL:", signed_url)

PROMPT = """
What are these documents about?
"""

# https://github.com/googleapis/python-genai
# https://ai.google.dev/gemini-api/docs/libraries
from google import genai
from google.genai import types
import pathlib
# import pudb; pu.db
# import pudb;

client = genai.Client()
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
    # types.Part.from_uri(
    #   # Use a public HTTPS URL
    #   file_uri="https://example.com/secure/image.pdf",
    # ),
    types.Part.from_uri(
      # Use a signed private URL
      file_uri=signed_url,
    ),
    PROMPT
  ]
)
print(response.text)


"""
REFERENCE:
  Gemini API Gmail newsletter
    subject: Gemini API: 5x higher file size limits + new cloud file input methods
    https://mail.google.com/mail/u/0/#inbox/FMfcgzQfBQDcqPbSCbXxRzFwgKNkVvKj
  Gemini API Documentation
    https://ai.google.dev/gemini-api/docs/

HOW TO RUN THIS SCRIPT:
export GEMINI_API_KEY="xxxxxxxxxxxxxxxxxxxx"
export AWS_REGION="xxxxxxxxx"
export AWS_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxx"
export AWS_SECRET_ACCESS="xxxxxxxxxxxxxxxxx"
python3 gemini-with-s3-signed-url.py

GENERATE AN API KEY
Follow these steps:
- In Google AI Studio, click Get API key in the left navigation panel.
  - https://aistudio.google.com/
- On the next page, click Create API key.
  - https://aistudio.google.com/apikey
- Select an existing Google Cloud project or create a new one. This project is used to manage billing for API usage.

# vi "$HOME/Library/Application Support/aichat/config.yaml"
"""

