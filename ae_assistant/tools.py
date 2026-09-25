"""Step 5: Wrap the retriever as a tool the agent can call."""

from langchain.tools import tool
# Converts a python function into a langchain tool

def create_search_tool(retriever):
    """Return a @tool function that searches ae contract document."""

    @tool
    def search_ae_contract(question: str) -> str:
        """Search the AE contract document for information about Contract value & currency, Effective & expiry dates, Scope of work summary, Payment terms & milestones, Liability cap & exclusions, Insurance requirements, Liquidated damages rate & cap, Termination terms (breach & convenience), Governing law & dispute resolution, HSE & incident reporting requirements.."""
        matching_chunks = retriever.invoke(question) # its going to invoke the questions which is going to come form the user
        return "\n\n".join(chunk.page_content for chunk in matching_chunks) # this is to retrieve all the chunks for the matching chunks
    return search_ae_contract