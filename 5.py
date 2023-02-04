def longest_string(strings):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


print(longest_string(["cat", "dog", "bird", "lizard"]))
print(longest_string(["cat", "dog", "bird", "wolf"]))