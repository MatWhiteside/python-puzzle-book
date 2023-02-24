def has_vowel(input_str: str) -> bool:
    vowels = "aeiouAEIOU"
    for character in input_str:
        if character in vowels:
            return True
    return False


def filter_strings_with_vowels(input_strs: list[str]) -> list[str]:
    return [input_str for input_str in input_strs if has_vowel(input_str)]


print(filter_strings_with_vowels(["apple", "banana", "zyxvb"]))
