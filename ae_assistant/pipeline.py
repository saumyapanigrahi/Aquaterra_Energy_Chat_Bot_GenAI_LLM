"""
Step 8: Wires all the components together into one ready to use agent

This is the single entry point that main.py (CLI) and app.py (streamlit) both call.
Each step is handled by its own small module.

"""

from ae_assistant import config
from ae_assistant.agent import create_ae_agent
from ae_assistant.document_loader import load_document
from ae_assistant.llm import get_llm
from ae_assistant.splitter import split_into_chunks
from ae_assistant.tools import create_search_tool
from ae_assistant.verctor_store import (
    build_vector_store,
    get_retriever,
    load_vector_store,
    save_vector_store,
    vector_store_exists,
)


def build_vector_store_for_document(file_path: str = config.DATA_FILE_PATH):
    """Load + Split + embed the document, reusing a saved index if we gave one."""

    if vector_store_exists():
        print("Found a saved vector store on disk, loading it (fast, no re-embedding).")
        return load_vector_store()
    
    ## above code shows, build a vector store for documents, it will take a data file path and 
    # it would check does my vector store exists, if exists then load the vector store
    # if no vector store exists then build one (below code)

    print("No saved vector store found, building one from scratch...")
    documents = load_document(file_path)
    chunks = split_into_chunks(documents)
    print(f"Loaded'{file_path}' and split it into {len(chunks)} chunks.")

    vector_store = build_vector_store(chunks)
    save_vector_store(vector_store)
    print("Vector store build and saved to disk for next time.")
    return vector_store

    # Note: if the vector store will be exist, then it won't load the above code but the above
    # codes will run and load the already present vector store...

def build_ae_assistant(file_path:str = config.DATA_FILE_PATH):
    """Build the full RAG agent, ready to answer questions."""
    config.check_api_keys()

    vector_store = build_vector_store_for_document(file_path)
    retriever = get_retriever(vector_store)
    search_tool = create_search_tool(retriever)

    llm = get_llm()
    agent = create_ae_agent(llm, [search_tool])

    return agent

def ask(agent, question: str) -> str:
    """Ask the agent a question and return its final answer as plain text."""
    response = agent.invoke({"messages": [{"role":"user", "content": question}]})
    return response["messages"][-1].content
    






