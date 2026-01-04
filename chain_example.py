"""Chain example

The following example demonstrates how to use chains to call an LLM multiple times in a sequence using LLMChain.
"""
from langchain.chains import LLMChain
from langchain_aws import ChatBedrock as Bedrock
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


# 0. Load environment variables
load_dotenv()
os.environ['AWS_BEARER_TOKEN_BEDROCK'] = os.getenv("AWS_BEARER_TOKEN_BEDROCK")

chat = Bedrock(
     region_name = "ap-southeast-1",
     model_kwargs={"temperature":1,"top_k":250,"top_p":0.999,"anthropic_version":"bedrock-2023-05-31"},
     model_id="anthropic.claude-3-haiku-20240307-v1:0"
)

multi_var_prompt = PromptTemplate(
     input_variables=["company"],
     template="Create a list with the names of the main metrics tracked in the reports of {company}?",
)
 
chain = LLMChain(llm=chat, prompt=multi_var_prompt)
answers = chain.invoke("Amazon")
print(answers)

answers = chain.invoke("AWS")
print(answers)