"""Chat models example

The following example demonstrates how you can get a response from an LLM
 by passing a user request to the LLM."""


import boto3
import os
from dotenv import load_dotenv
# Corrected imports for LangChain Core v0.3+
from langchain_aws import ChatBedrock as Bedrock
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
# 0. Load environment variables
load_dotenv()
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = os.getenv("AWS_BEARER_TOKEN_BEDROCK")


# you can pass the prompt throught he bedrock with langchain also

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


# 2. Initialize ChatBedrock by PASSING the client
# This ensures LangChain uses your Bearer Token and Region 
chat = Bedrock(

      model_id="anthropic.claude-3-haiku-20240307-v1:0",
      region_name='ap-southeast-1',

      model_kwargs={"temperature": 0.1}
)

# 3. Define Messages (Using SystemMessage for your "Scenario" system)
messages = [
    SystemMessage(content="You are a helpful culinary guide."),
    HumanMessage(content="I would like to try Indian food, what do you suggest should I try?")
]

# 4. Invoke the model
try:
#     response = chat.invoke(messages)
    response = chat.invoke(prompt)

    print(response.content)
except Exception as e:
    print(f"Error: {e}")