def censor(strings: list[str]) -> list[str]:
    censored_strings = []
    for string in strings:
        censored_string = ""
        for letter in string:
            if letter.upper() in ["P", "Y", "T", "H", "O", "N"]:
                censored_string += "X"
            else:
                censored_string += letter
        censored_strings.append(censored_string)
    return censored_strings


print(censor(["python", "hello", "HELLO"]))
