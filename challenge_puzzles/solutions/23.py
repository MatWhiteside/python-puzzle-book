def xor(input_a: str, input_b: str) -> str:
    result = ""
    for i in range(min(len(input_a), len(input_b))):
        if input_a[i] == input_b[i]:
            result += "0"
        else:
            result += "1"
    return result


print(xor("1111", "1111"))
print(xor("1111", "0000"))
print(xor("0000", "1111"))
print(xor("1101", "0001"))
print(xor("0000", "0000"))
print(xor("00000", "0000"))
