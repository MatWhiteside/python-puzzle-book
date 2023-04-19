def check_if_string_is_happy(input_str: str) -> bool:
    return not any(
        a == b or a == c or b == c
        for a, b, c in zip(input_str, input_str[1:], input_str[2:])
    )


print(check_if_string_is_happy("abcdefg"))
print(check_if_string_is_happy("abcabcabcabc"))
print(check_if_string_is_happy("hello"))
