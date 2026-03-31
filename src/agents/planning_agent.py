from src.agents.groq_agent import groq_agent

def planning_agent(query):

    planning_prompt = f"""
    You are an AI Planning Agent.

    Break the task into actionable steps.

    Task:
    {query}

    Return:
    Step 1:
    Step 2:
    Step 3:
    """

    plan = groq_agent(planning_prompt)

    return plan