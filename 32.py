def contains_python(string: str) -> bool:
    string = string.lower()
    python_chars = "python"
    for i in range(len(string) - len(python_chars) + 1):
        if sorted(string[i:i + len(python_chars)]) == sorted(python_chars):
            return True
    return False


print(contains_python("pYThon"))
print(contains_python("Nohtyp"))
print(contains_python("pythZon"))
print(contains_python("AAApythonAAA"))
print(contains_python("AAApythoAnAA"))
