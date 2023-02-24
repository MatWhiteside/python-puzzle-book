def censor_python(input_strs: list[str]) -> list[str]:
    censored_input_strs = []
    for input_str in input_strs:
        censored_string = ""
        for character in input_str:
            if character.upper() in ["P", "Y", "T", "H", "O", "N"]:
                censored_string += "X"
            else:
                censored_string += character
        censored_input_strs.append(censored_string)
    return censored_input_strs


print(censor_python(["python", "hello", "HELLO"]))
