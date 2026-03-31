from src.agents.groq_agent import groq_agent
from src.agents.tool_agent import tool_agent


def execution_agent(plan):

    steps = plan.split("\n")

    results = []

    for step in steps:

        if step.strip() == "":
            continue

        tool_response = tool_agent(step)

        if tool_response:
            results.append(tool_response)
        else:
            llm_response = groq_agent(step)
            results.append(llm_response)

    return "\n".join(results)