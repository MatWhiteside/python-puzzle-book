def check_if_string_is_happy(input_str: str) -> bool:
    for i in range(len(input_str) - 2):
        if (
            input_str[i] == input_str[i + 1]
            or input_str[i] == input_str[i + 2]
            or input_str[i + 1] == input_str[i + 2]
        ):
            return False
    return True


print(check_if_string_is_happy("abcdefg"))
print(check_if_string_is_happy("aaabcdef"))
