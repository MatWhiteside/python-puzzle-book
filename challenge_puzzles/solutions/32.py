def contains_python_chars(input_str: str) -> bool:
    input_str = input_str.lower()
    python_chars = set("python")

    for i in range(len(input_str) - len(python_chars) + 1):
        if set(input_str[i:i + len(python_chars)]) == python_chars:
            return True
    return False


print(contains_python_chars("pYThon"))
print(contains_python_chars("Nohtyp"))
print(contains_python_chars("pythZon"))
print(contains_python_chars("AAApythonAAA"))
print(contains_python_chars("AAApythoAnAA"))
