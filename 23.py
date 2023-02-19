def xor(s1, s2):
    result = ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            result += "0"
        else:
            result += "1"
    return result


print(xor("1111", "1111"))
print(xor("1111", "0000"))
print(xor("0000", "1111"))
print(xor("0000", "0000"))
print(xor("00000", "0000"))
