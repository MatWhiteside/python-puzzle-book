roman_map = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def int_to_roman(input_num: int) -> str:
    result = ""
    for roman_int_value in sorted(roman_map.keys(), reverse=True):
        while input_num >= roman_int_value:
            result += roman_map[roman_int_value]
            input_num -= roman_int_value
    return result


def roman_to_int(input_str: str) -> int:
    result = 0
    input_idx = 0
    while input_idx < len(input_str):
        if input_idx + 1 < len(input_str) and input_str[input_idx:input_idx + 2] in roman_map.values():
            result += [k for k, v in roman_map.items() if v == input_str[input_idx:input_idx + 2]][0]
            input_idx += 2
        else:
            result += [k for k, v in roman_map.items() if v == input_str[input_idx]][0]
            input_idx += 1
    return result


def int_roman_converter(to_convert: str | int) -> int | str:
    # roman numerals to int
    if isinstance(to_convert, str):
        return roman_to_int(to_convert)
    # int to roman numerals
    if isinstance(to_convert, int):
        return int_to_roman(to_convert)

    return None


for i in range(1, 100):
    print(
        f"{i} = {int_roman_converter(i)} = {int_roman_converter(int_roman_converter(i))}"
    )
