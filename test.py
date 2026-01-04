import os
from dotenv import load_dotenv

print("Before dotenv:", os.environ.get("AWS_BEARER_TOKEN_BEDROCK"))

load_dotenv(override=True)  # 👈 THIS is the key

print("After dotenv:", os.environ.get("AWS_BEARER_TOKEN_BEDROCK"))
