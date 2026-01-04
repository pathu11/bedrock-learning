import boto3
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


# 0. Load environment variables
load_dotenv()
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

# 2. Create the client
client = boto3.client(
    service_name='bedrock-runtime',
    region_name='ap-southeast-1'
)

# we canpass the arguments through the prompt template directly to aws bedrock
# prompt from prompt.py
multi_var_prompt = PromptTemplate(
    input_variables=["customerName", "feedbackFromCustomer"],
    template="""
Human: Create an email to {customerName} in response to the following customer service feedback:

<customer_feedback>
{feedbackFromCustomer}
</customer_feedback>

Assistant:
"""
)

prompt = multi_var_prompt.format(
    customerName="John Doe",
    feedbackFromCustomer="""Hello AnyCompany,
I am very pleased with the recent experience I had when I called your customer support.
I got an immediate call back, and the representative was very knowledgeable in fixing the problem.
We are very happy with the response provided and will consider recommending it to other businesses.
"""
)

# ... rest of your code ...

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
                # "content": [{"text": user_message}]
                "content": [{"text": prompt}]
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