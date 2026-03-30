from src.agents.orchestrator import route_agent
from src.memory.conversation_memory import clear_memory

def main():

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "reset":
            clear_memory()
            print("Memory Cleared")
            continue

        response = route_agent(user_input)

        print("AI:", response)


if __name__ == "__main__":
    main()