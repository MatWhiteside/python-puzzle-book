def rot13(text: str) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            a_code = ord('A') if char.isupper() else ord('a')
            char = chr((ord(char) - a_code + 13) % 26 + a_code)
        result += char
    return result

print(rot13("Hello world!"))
print(rot13("12345!@£$%"))