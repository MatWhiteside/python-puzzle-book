def is_happy(s: str) -> bool:
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True


print(is_happy("abcdefg"))
print(is_happy("aaabcdef"))
