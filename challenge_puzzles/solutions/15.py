def filter_palindromes(input_strs: list[str]) -> list[str]:
    return [
        input_str
        for input_str in input_strs
        if input_str.lower() == input_str.lower()[::-1]
    ]


print(filter_palindromes(["cat", "dog", "racecar", "deified", "giraffe"]))
print(filter_palindromes(["kayak", "deified", "rotator", "repaper", "deed", "a"]))
print(filter_palindromes(["ab", "ba", "cd", "ef", "pt"]))
