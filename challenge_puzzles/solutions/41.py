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
    roman_map_swapped = {v: k for k, v in roman_map.items()}

    result, prev_value = 0, 0

    for char in input_str:
        value = roman_map_swapped[char]

        if value > prev_value:
            result -= prev_value
            result += value - prev_value
        else:
            result += value

        prev_value = value

    return result


def int_roman_converter(to_convert: str | int) -> int | str:
    # roman numerals to int
    if isinstance(to_convert, str):
        return roman_to_int(to_convert)

    # int to roman numerals
    if isinstance(to_convert, int):
        return int_to_roman(to_convert)

    return None


for i in range(1, 5000):
    is_equal = int_roman_converter(int_roman_converter(i)) == i

    if not is_equal:
        print(f"{i} is incorrect!")
