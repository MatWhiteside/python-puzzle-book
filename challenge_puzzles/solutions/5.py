def get_longest_string(input_strs: list[str]) -> str:
    longest_str = ""
    for input_str in input_strs:
        if len(input_str) > len(longest_str):
            longest_str = input_str
    return longest_str


print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
print(get_longest_string(["a", "b", "c", "d"]))
