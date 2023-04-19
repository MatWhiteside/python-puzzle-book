def remove_vowels(input_str: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(char for char in input_str if char not in vowels)


print(remove_vowels("Hello, World!"))
print(remove_vowels("aeiouAEIOU"))
print(remove_vowels("zzxxxccvvvbbnnmmmLLKKJJHH"))
