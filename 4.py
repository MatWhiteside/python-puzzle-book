def remove_vowels(input_str: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(character for character in input_str if character not in vowels)


print(remove_vowels("Hello, World!"))
