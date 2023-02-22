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


def int_to_roman(num: int) -> str:
    roman = ""
    for key in sorted(roman_map.keys(), reverse=True):
        while num >= key:
            roman += roman_map[key]
            num -= key
    return roman


def roman_to_int(s: str) -> int:
    integer = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i + 2] in roman_map.values():
            integer += [k for k, v in roman_map.items() if v == s[i:i + 2]][0]
            i += 2
        else:
            integer += [k for k, v in roman_map.items() if v == s[i]][0]
            i += 1
    return integer


def int_roman_converter(to_convert: str | int) -> int | str:
    # roman numerals to int
    if isinstance(to_convert, str):
        return roman_to_int(to_convert)
    # int to roman numerals
    return int_to_roman(to_convert)


for i in range(1, 100):
    print(
        f"{i} = {int_roman_converter(i)} = {int_roman_converter(int_roman_converter(i))}"
    )
