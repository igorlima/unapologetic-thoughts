# USING AMAZON NOVA PRO FOR DOCUMENT ANALYSIS
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
# curl -o the-sea.mp4 "https://d2908q01vomqb2.cloudfront.net/artifacts/AWSNews/2024/AWSNEWS-1259-nova-pro-input-video.mp4?_=1"
VIDEO_FILE = "the-sea.mp4"
# see list of models in the AWS Bedrock console
# https://github.com/igorlima/unapologetic-thoughts/blob/5ec42280b950a10d48b39c6509d0f2405533d49c/snippets/python/aws-bedrock-list-models.py#L38
MODEL_ID = "amazon.nova-pro-v1:0"

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

with open(VIDEO_FILE, "rb") as f:
  video = f.read()

user_message = "Describe this video."
messages = [{
  "role": "user",
  "content": [
    {"video": {"format": "mp4", "source": {"bytes": video}}},
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
  Introducing Amazon Nova foundation models: Frontier intelligence and industry leading price performance
    https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/

HOW TO RUN THIS SCRIPT:

({
export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python3 aws-bedrock-model-amazon-nova-001.py
})
"""
