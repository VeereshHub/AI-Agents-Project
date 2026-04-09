import os
from groq import Groq
from dotenv import load_dotenv
from src.memory.conversation_memory import add_memory, get_memory

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def groq_agent(query):

    add_memory("user", query)

    messages = [
        {
         "role": "system",
         "content": "You are a helpful AI assistant"
        }
    ] + get_memory()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content

    add_memory("assistant", reply)

    return reply