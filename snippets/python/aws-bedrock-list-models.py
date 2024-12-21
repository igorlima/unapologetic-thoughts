import boto3
from pprint import pprint
import pudb; # pu.db

# LIST ALL FOUNDATION MODELS
# Supported foundation models in Amazon Bedrock
# https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html
# ListFoundationModels
# https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html
# list_foundation_models
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_models.html

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

# AWS_REGION = "us-east-1"
AWS_REGION = "us-west-2"
client = boto3.client("bedrock", region_name=AWS_REGION)
"""
import os
client = boto3.client(
  "bedrock",
  region_name=AWS_REGION,
  aws_access_key_id=os.getenv("ACCESS_ID"),
  aws_secret_access_key=os.getenv("ACCESS_KEY")
)
"""

response = client.list_foundation_models()
"""
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#bedrock
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_models.html
response = client.list_foundation_models(
    byProvider='string',
    byCustomizationType='FINE_TUNING'|'CONTINUED_PRE_TRAINING'|'DISTILLATION',
    byOutputModality='TEXT'|'IMAGE'|'EMBEDDING',
    byInferenceType='ON_DEMAND'|'PROVISIONED'
)
"""
modelSummaries = response["modelSummaries"]
pprint(modelSummaries)

# iterate a dictionary/array in a single line in python
models = [m for m in modelSummaries if "responseStreamingSupported" in m]
models = [model["modelId"] for model in models if model["responseStreamingSupported"] is True]
# models = [{"modelId": model["modelId"], "input": model["inputModalities"]} for model in models if model["responseStreamingSupported"] is True]
pprint(models)

"""
HOW TO RUN THIS SCRIPT:

({
export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python3 aws-bedrock-list-models.py
})
"""
