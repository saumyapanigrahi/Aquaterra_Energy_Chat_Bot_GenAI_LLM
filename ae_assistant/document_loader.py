"""Step 1: Read the raw document from the data folder"""

from langchain_community.document_loaders import TextLoader
from ae_assistant import config

def load_document(file_path: str = config.DATA_FILE_PATH): # here, we are initializing the file path (as string and giving the location)
    """Load a .txt file and return it as a list of LangChain document"""
    loader = TextLoader(file_path, encoding="utf-8")
    return loader.load()

