def filter_even_length_strings(input_strs: list[str]) -> list[str]:
    return [input_str for input_str in input_strs if len(input_str) % 2 == 0]


print(filter_even_length_strings(["cat", "dog", "fish", "elephant"]))
print(filter_even_length_strings(["q", "w", "e", "r", "t", "y"]))
print(filter_even_length_strings(["qq", "ww", "ee", "rr", "t", "yy"]))
