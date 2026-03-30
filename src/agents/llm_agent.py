import os
from groq import Groq
from dotenv import load_dotenv
from src.memory.conversation_memory import add_memory, get_memory

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def llm_agent(query):

    response = client.chat.completions.create(
        
        # model="llama3-8b-8192",
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant"
            },
            {
                "role": "user",
                "content": query
            }
        ]+ get_memory()
        
    )
    
    reply = response.choices[0].message.content

    add_memory("assistant", reply)

    return reply

    # return response.choices[0].message.content


# import os
# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(api_key=os.getenv("ANTHROPIC_API_KEY"))

# def llm_agent(query):

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a helpful AI assistant"},
#             {"role": "user", "content": query}
#         ]
#     )

#     return response.choices[0].message.content
