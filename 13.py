def filter_vowels(strings):
    def has_vowel(string):
        vowels = "aeiouAEIOU"
        for char in string:
            if char in vowels:
                return True
        return False

    return [s for s in strings if has_vowel(s)]


print(filter_vowels(["apple", "banana", "zyxvb"]))
