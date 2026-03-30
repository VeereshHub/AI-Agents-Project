conversation_history = []

def add_memory(role, message):
    conversation_history.append({
        "role": role,
        "content": message
    })


def get_memory():
    return conversation_history


def clear_memory():
    conversation_history.clear()