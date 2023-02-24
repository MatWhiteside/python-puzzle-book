def filter_strings_containing_a(input_strs: list[str]) -> list[str]:
    return [input_str for input_str in input_strs if "a" in input_str]


print(filter_strings_containing_a(["apple", "banana", "cherry", "date"]))
