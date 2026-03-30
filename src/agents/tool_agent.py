from src.tools.calculator_tool import calculator
from src.tools.file_reader_tool import read_file


def tool_agent(query):

    if "calculate" in query.lower():
        expression = query.lower().replace("calculate", "")
        return calculator(expression)

    if "read file" in query.lower():
        file_name = query.lower().replace("read file", "").strip()
        return read_file(file_name)

    return None