def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except Exception:
        return "File not found"