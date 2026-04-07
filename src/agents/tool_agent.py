from src.agents.tool_selector_agent import tool_selector_agent
from src.tools.tool_registry import tools


def tool_agent(query):

    tool_name = tool_selector_agent(query)

    if tool_name in tools:

        tool_function = tools[tool_name]["function"]

        return tool_function(query)

    return None