def format_number_with_commas(input_num: int) -> str:
    return f"{input_num:,}"


print(format_number_with_commas(1000000))
print(format_number_with_commas(10000))
print(format_number_with_commas(999999999999))
print(format_number_with_commas(0))
