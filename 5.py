def get_longest_string(input_strs: list[str]) -> str:
    longest_string = ""
    for input_str in input_strs:
        if len(input_str) > len(longest_string):
            longest_string = input_str
    return longest_string


print(get_longest_string(["cat", "dog", "bird", "lizard"]))
print(get_longest_string(["cat", "dog", "bird", "wolf"]))
