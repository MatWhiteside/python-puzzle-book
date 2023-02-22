def string_to_ascii(string: str) -> list[int]:
    return [ord(char) for char in string]


print(string_to_ascii("Programming puzzles!"))


# Bonus Solution
def ascii_to_string(ascii_codes: list[int]) -> str:
    return "".join([chr(char) for char in ascii_codes])


print(ascii_to_string([80, 114, 111, 33]))
