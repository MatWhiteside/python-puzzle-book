def string_to_ascii(string):
    return [ord(char) for char in string]


print(string_to_ascii("Programming puzzles!"))


# BONUS SOLUTION
def ascii_to_string(ascii):
    return "".join([chr(char) for char in ascii])


print(ascii_to_string([80, 114, 111, 33]))
