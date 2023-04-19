def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    # Utilise list comprehension with an if condition to return a new list
    # consisting of strings that contain the letter "a"
    return [input_str for input_str in input_strs if "a" in input_str]


print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))
