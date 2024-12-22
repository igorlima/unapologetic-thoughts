# USING AMAZON NOVA PRO FOR PROOFREADING
import boto3
import pudb; # pu.db

"""
# pip3 show boto3
# pip3 index versions boto3
# pip3 list
# pip3 install --no-cache --upgrade-strategy eager -I boto3==1.35.86

python3 -m venv my-test-env-2024a12m21d
source my-test-env-2024a12m21d/bin/activate
pip3 install boto3==1.35.86
pip3 install pudb
"""

AWS_REGION = "us-east-1"
# see list of models in the AWS Bedrock console
# https://github.com/igorlima/unapologetic-thoughts/blob/5ec42280b950a10d48b39c6509d0f2405533d49c/snippets/python/aws-bedrock-list-models.py#L38
MODEL_ID = "amazon.titan-text-lite-v1"
MODEL_ID = "amazon.titan-text-premier-v1:0"
MODEL_ID = "amazon.nova-pro-v1:0"
MODEL_ID = "amazon.nova-micro-v1:0"

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)
"""
import os
bedrock_runtime = boto3.client(
  "bedrock-runtime",
  region_name=AWS_REGION,
  aws_access_key_id=os.getenv("ACCESS_ID"),
  aws_secret_access_key=os.getenv("ACCESS_KEY")
)
"""

user_message = """
**Proofread**, enhance and improve the {{text_type}} below. {{tone}}. Use a randomness level of {{randomness_level}}.
<context>

The policies of the next US administration could have profound consequences for the future of the climate, the wars in Ukraine and the Middle East and the global economy.
Our rigorous, fact-based independent journalism will hold those in power to account and interrogate the human impact of the decisions made in the White House.

</context>
Please make it clear and concise.

{{text_type}}: chat message
{{tone}}: Be positive, friendly, and kind
{{randomness_level}}: 1
"""
messages = [{
  "role": "user",
  "content": [
    {"text": user_message}
  ]
}]

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html
response = bedrock_runtime.converse(
  modelId=MODEL_ID,
  messages=messages,
  inferenceConfig={"temperature": 0.0}
)

response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)

"""
REFERENCE:
  Using Amazon Nova Pro for document analysis
    https://github.com/igorlima/unapologetic-thoughts/blob/9869d8f8f5247a013d653e3b5d7da4ebc897d2d0/snippets/python/aws-bedrock-model-amazon-nova-001.py#L1

HOW TO RUN THIS SCRIPT:

({
export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python3 aws-bedrock-model-amazon-nova-004.py
})
"""
