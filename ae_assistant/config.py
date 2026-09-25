""" All settings for the app live here, in one place."""

import os
from dotenv import load_dotenv

load_dotenv()


## ENVIRONMENT VARIABLES (SECRETS)
# API Keys for respective tasks/requirements

GROQ_API_KEY = os.getenv("GROQ_API_KEY") # we are getiing this from .env file present in the main folder
JINA_API_KEY = os.getenv("JINA_API_KEY") 
# we can also write the API keys directly for respective variables.



## Checks for API Keys - Error prompt
def check_api_keys() -> None:
    """Stop early with a clear message if a API Key is missing"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Please add it")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY. Please add it")
    

## MODELS
# LLM and EMBEDDING MODEL

LLM_MODEL_NAME = "openai/gpt-oss-20b"
EMBEDDING_MODEL_NAME = "jina-embeddings-v2-base-en"





## DEFINE THE PATH - DATA & Vector DB Path

DATA_FILE_PATH = os.path.join("data", "AE_Contract.txt")
VECTOR_STORE_PATH = os.path.join("data", "faiss_index")

# Note: we have 3 types of vector store
# 1. In memory ( like assigning verctor to a variable "a = ___")
# 2. Persistent memory 
# ( like if we have 100 gb of vectors and we need to store it, we will store it in a file so that the data will not be lost)
# 3. Cloud memory ( like storing the vectors in to the cloud data base)




## CHUNKING / TEXT SPLITTING CONFIG

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

## RETRIVAL RESULTS
TOP_K_RESULTS = 3

## SYSTEM PROMPT
SYSTEM_PROMPT = (
    "You are an AI Contract Intelligence Assistant for oil and gas contracts. "
    "Your task is to answer user questions about the contract documents. "
    "When the user asks a question about a contract, use the aqe_chat_tool to retrieve the relevant information before answering."
    "Use only the information retrieved from the contract documents."
    "Do not invent, assume, or use information that is not available in the documents."
    "If the required information is not found, clearly state that it was not found in the available contract documents."
    "Provide clear, concise, and professional answers"
    "When possible, mention the relevant contract ID and section or page from the retrieved information."
)











