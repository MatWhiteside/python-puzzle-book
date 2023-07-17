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
    # Your implementation here


def roman_to_int(input_str: str) -> int:
    # Your implementation here

def int_roman_converter(to_convert: str | int) -> int | str:
    # Your implementation here


for i in range(1, 5000):
    is_equal = int_roman_converter(int_roman_converter(i)) == i

    if not is_equal:
        print(f"{i} is incorrect!")
