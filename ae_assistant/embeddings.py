"""Step 3: Turn text into numbers(vectors) using Jina"""

from langchain_community.embeddings import JinaEmbeddings
from ae_assistant import config

def get_embeddings_model(): # this is going to be called in vector_store initialisation
    """This function will return the Jina embeddings"""
    return JinaEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

## this is only the model creation or calling a model...