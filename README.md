## Generative AI with Amazon Bedrock

### Hands-on Learning & RAG Implementations

This repository contains my hands-on learning and experiments from the AWS Skill Builder course – Building Generative AI Applications Using Amazon Bedrock.
It showcases how to build Generative AI applications, including prompt engineering, chaining, memory handling, and Retrieval-Augmented Generation (RAG) using Amazon Bedrock.

This repo is designed as a learning + experimentation space, but the patterns here can be extended to real-world production systems.

###  What I Learned from This Project

Through this project, I explored:

-  Fundamentals of Generative AI & Foundation Models
- Invoking Amazon Bedrock models using Python
- Prompt engineering and reusable prompt templates
- Chaining LLM calls for multi-step reasoning
- Context & memory handling in LLM-based systems
- Retrieval-Augmented Generation (RAG) using Bedrock
- Secure configuration using environment variables (.env)

📁 Repository Structure
bedrock-learning/
│
├── RAG_bedrock/
├── aws_bedrock_config.py     # Bedrock client & configuration
├── chain_example.py          # Prompt chaining examples
├── memory_handling.py        # Context & memory management
├── prompt.py                 # Prompt templates & helpers
├── test.py                   # Basic Bedrock API testing
├── test_lang_aws.py          # Language model invocation tests
├── Tutorials_aws/            # Notes & tutorials from labs
├── requirements.txt
├── .env.example              # Environment variable template
└── README.md

### Environment Configuration (Important)

This project uses a .env file to securely manage credentials.

#### Create a .env file in the root directory:
```
AWS_BEARER_TOKEN_BEDROCK=your_bedrock_token_here
AWS_REGION=us-east-1
```


#### Never commit your .env file
- Add it to .gitignore to keep credentials safe.
- The token is automatically loaded using python-dotenv.

#### Setup Instructions
✅ Prerequisites
Python 3.8+

- AWS account with Amazon Bedrock access
- Virtual environment (recommended)

📦 Install Dependencies
pip install -r requirements.txt

#### 📚 RAG Implementation (RAG_bedrock/)

- The RAG_bedrock folder contains a complete Retrieval-Augmented Generation pipeline built on Amazon Bedrock.

🧠 What This RAG Pipeline Does

- Ingests documents
- Generates embeddings
- Stores them in a vector store
- Retrieves relevant context for a user query Passes retrieved data to a Bedrock foundation model
- Generates grounded, context-aware responses
