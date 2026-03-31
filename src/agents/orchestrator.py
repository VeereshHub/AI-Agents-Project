from src.agents.groq_agent import groq_agent
from src.agents.tool_agent import tool_agent
from src.agents.planning_agent import planning_agent
from src.agents.execution_agent import execution_agent

def route_agent(query):

  # If complex task use planning
    if "create" in query.lower() or "build" in query.lower():
         plan = planning_agent(query)
         execution = execution_agent(plan)
         return f"Plan:\n{plan}\n\nExecution:\n{execution}"
    
    tool_response = tool_agent(query)

    if tool_response:
        return tool_response

    return groq_agent(query)