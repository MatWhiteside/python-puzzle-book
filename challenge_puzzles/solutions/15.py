def filter_palindromes(input_strs: list[str]) -> list[str]:
    filtered_input_strs = []

    for input_str in input_strs:
        if input_str == input_str[::-1]:
            filtered_input_strs.append(input_str)

    return filtered_input_strs


print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
print(filter_palindromes(["kayak", "deified", "rotator", "repaper", "deed", "a"]))
print(filter_palindromes(["ab", "ba", "cd", "ef", "pt"]))
