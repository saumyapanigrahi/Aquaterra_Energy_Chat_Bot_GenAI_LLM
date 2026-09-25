"""Step 4: Store chunk embeddings in FAISS so we can search them later"""

import os
from langchain_community.vectorstores import FAISS
from ae_assistant import config
from ae_assistant.embeddings import get_embeddings_model

# Building a vector store using FAISS
# Here, we will do actual text to number conversation and store in a vector db

def build_vector_store(chunks):
    """Embed every chunk and build a searchable FAISS index in memory."""
    embeddings_model = get_embeddings_model()
    return FAISS.from_documents(chunks, embeddings_model)

# here, from_ducuments is a method which will convert the chunks into embeddings by using
# embeddings_model which will call the embedding function in the embeddings.py file by using FAISS.


## Save vector store

def save_vector_store(vector_store, path : str = config.VECTOR_STORE_PATH) -> None:
    """Save the FAISS index to disk so we don't have to build it every time"""
    vector_store.save_local(path) # as we are saving into the local machine but not to any database


## Load vector store

def load_vector_store(path : str = config.VECTOR_STORE_PATH):
    """Load previously saved FAISS index from disk."""
    embeddings_model = get_embeddings_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)


## We would make a function check if vector store exists?
def vector_store_exists(path:str = config.VECTOR_STORE_PATH) -> bool:
    """Check if a saved FAISS index is already exists on disk"""
    return os.path.exists(os.path.join(path,"index.faiss"))


## Get retriever - this method will also be used by our AI agent as an input and it will return us the top 3 results
# LLM can interact to retriever only so we need to write it here...
def get_retriever(vector_store, k: int = config.TOP_K_RESULTS):
    """Turns a vector store into a retriever that returns the top-k matching chunks."""
    return vector_store.as_retriever(search_kwargs = {"k":k})



### Here we end with the data ingestion pipeline....
    
