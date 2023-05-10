def censor_python(input_strs: list[str]) -> list[str]:
    censored_chars = ["P", "Y", "T", "H", "O", "N"]
    return [
        "".join(
            ["X" if char.upper() in censored_chars else char for char in input_str]
        ) for input_str in input_strs
    ]


print(censor_python(["python", "hello", "HELLO"]))
print(censor_python(["abcdefg"]))
print(censor_python([]))
