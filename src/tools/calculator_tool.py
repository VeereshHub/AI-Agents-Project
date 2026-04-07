import re

def calculator(query):

    try:
        expression = re.findall(r"[0-9+\-*/().]+", query)[0]
        result = eval(expression)
        return f"Result: {result}"
    except:
        return "Unable to calculate"