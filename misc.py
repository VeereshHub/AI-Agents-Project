def reverse_and_remove_duplicates(s):
    # Reverse the string
    reversed_s = s[::-1]
    
    # Remove duplicates while preserving order
    seen = set()
    result = []
    for char in reversed_s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

strUserInput=input("Enter a string: ")
result = reverse_and_remove_duplicates(strUserInput)
print("Reversed string with duplicates removed:", result)