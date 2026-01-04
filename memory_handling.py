import boto3
from langchain.chains import ConversationChain
from langchain_aws import BedrockLLM
from langchain_aws import ChatBedrock
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

# Bedrock client
client = boto3.client(
    service_name='bedrock-runtime',
    region_name='ap-southeast-1'
)

# LLM
# BedrockLLM → supports models like Amazon Titan.
llm = ChatBedrock(
    model_id="anthropic.claude-3-haiku-20240307-v1:0",
    client=client
)

# Memory
memory = ConversationBufferMemory()

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

# ---- Chat 1 ----
print("USER:", "Hi! I am in Los Angeles. What are some popular sightseeing places?")
print("AI:", conversation.predict(
    input="Hi! I am in Los Angeles. What are some popular sightseeing places?"
))

# ---- Chat 2 (no city mentioned) ----
print("\nUSER:", "What is the closest beach that I can go to?")
print("AI:", conversation.predict(
    input="What is the closest beach that I can go to?"
))

# ---- Chat 3 (still no city) ----
print("\nUSER:", "How far is it from downtown?")
print("AI:", conversation.predict(
    input="How far is it from downtown?"
))
