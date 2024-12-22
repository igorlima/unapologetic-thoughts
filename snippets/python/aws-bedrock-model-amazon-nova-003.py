# USING AMAZON NOVA REEL WITH A REFERENCE IMAGE
import base64, random, time, os
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
MODEL_ID = "amazon.nova-reel-v1:0"
SLEEP_TIME = 30
S3_DESTINATION_BUCKET = os.getenv("S3_DESTINATION_BUCKET")

# curl -o seascape.png "https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/11/20/nova-reel-seascape.png"
input_image_path = "seascape.png"
video_prompt = "drone view flying over a coastal landscape"

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
bedrock_runtime = boto3.client("bedrock-runtime", region_name=AWS_REGION)
"""
bedrock_runtime = boto3.client(
  "bedrock-runtime",
  region_name=AWS_REGION,
  aws_access_key_id=os.getenv("ACCESS_ID"),
  aws_secret_access_key=os.getenv("ACCESS_KEY")
)
"""

# Load the input image as a Base64 string.
with open(input_image_path, "rb") as f:
  input_image_bytes = f.read()
  input_image_base64 = base64.b64encode(input_image_bytes).decode("utf-8")

model_input = {
  "taskType": "TEXT_VIDEO",
  "textToVideoParams": {
    "text": video_prompt,
    "images": [{ "format": "png", "source": { "bytes": input_image_base64 } }]
    },
  "videoGenerationConfig": {
    "durationSeconds": 6,
    "fps": 24,
    "dimension": "1280x720",
    "seed": random.randint(0, 2147483648)
  }
}

invocation = bedrock_runtime.start_async_invoke(
  modelId=MODEL_ID,
  modelInput=model_input,
  outputDataConfig={"s3OutputDataConfig": {"s3Uri": f"s3://{S3_DESTINATION_BUCKET}"}}
)

invocation_arn = invocation["invocationArn"]
s3_prefix = invocation_arn.split('/')[-1]
s3_location = f"s3://{S3_DESTINATION_BUCKET}/{s3_prefix}"
print(f"\nS3 URI: {s3_location}")

while True:
  response = bedrock_runtime.get_async_invoke(
    invocationArn=invocation_arn
  )
  status = response["status"]
  print(f"Status: {status}")
  if status != "InProgress":
    break
  time.sleep(SLEEP_TIME)

if status == "Completed":
  print(f"\nVideo is ready at {s3_location}/output.mp4")
else:
  print(f"\nVideo generation status: {status}")



"""
REFERENCE:
  Introducing Amazon Nova foundation models: Frontier intelligence and industry leading price performance
    https://aws.amazon.com/blogs/aws/introducing-amazon-nova-frontier-intelligence-and-industry-leading-price-performance/

HOW TO RUN THIS SCRIPT:

({
export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export S3_DESTINATION_BUCKET="my-s3-bucket"
python3 aws-bedrock-model-amazon-nova-003.py
})
"""
