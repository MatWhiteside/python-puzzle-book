def remove_vowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    return "".join(c for c in s if c not in vowels)


print(remove_vowels("Hello, World!"))  # should print "Hll, Wrd!"
