from src.tools.calculator_tool import calculator
from src.tools.file_reader_tool import read_file

tools = {
    "calculator": {
        "description": "Use for mathematical calculations",
        "function": calculator
    },
    "file_reader": {
        "description": "Use to read files",
        "function": read_file
    }
}