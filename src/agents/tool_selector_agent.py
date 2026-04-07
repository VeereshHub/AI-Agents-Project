from src.agents.groq_agent import groq_agent
from src.tools.tool_registry import tools

def tool_selector_agent(query):

    tool_descriptions = "\n".join(
        [f"{name}: {tool['description']}" for name, tool in tools.items()]
    )

    prompt = f"""
    You are a tool selector.

    Available tools:
    {tool_descriptions}

    Based on user query, return tool name only.

    Query:
    {query}
    """

    tool_name = groq_agent(prompt).strip().lower()

    return tool_name