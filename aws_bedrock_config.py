import boto3
import os
from dotenv import load_dotenv

# 0. Load environment variables
load_dotenv()
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

# 2. Create the client
client = boto3.client(
    service_name='bedrock-runtime',
    region_name='ap-southeast-1'
)

# ... rest of your code ...

# # 2. Create a Bedrock Runtime client
# bedrock = boto3.client(
#      service_name='bedrock',
#      region_name='ap-southeast-1'
#      )
# # List available models for the region
# model_list=bedrock.list_foundation_models()
# for x in range(len(model_list.get('modelSummaries'))):
#      print(model_list.get('modelSummaries')[x]['modelId'])

# 3. Define your Scenario and Message
# Your Jinja2 compiled prompt goes into the 'system' field
system_prompt = "You are a patient in a therapy session. Based on your backstory, you feel anxious and cautious."
user_message = "Hello, how can I help you today?"

# 4. Use the Converse API (Unified for all models)
try:
    response = client.converse(
        modelId="anthropic.claude-3-haiku-20240307-v1:0",
        system=[{"text": system_prompt}],
        messages=[
            {
                "role": "user",
                "content": [{"text": user_message}]
            }
        ],
        inferenceConfig={
            "maxTokens": 512,
            "temperature": 0.5,
            "topP": 0.9
        }
    )

    # 5. Extract the response text
    output_text = response['output']['message']['content'][0]['text']
    print(f"Claude Response: {output_text}")

except Exception as e:
    print(f"Error: {e}")