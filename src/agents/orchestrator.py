from src.agents.groq_agent import groq_agent
from src.agents.tool_agent import tool_agent


def route_agent(query):

    tool_response = tool_agent(query)

    if tool_response:
        return tool_response

    return groq_agent(query)