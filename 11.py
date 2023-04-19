def format_number_with_commas(input_num: int) -> str:
    return f"{input_num:,}"


print(format_number_with_commas(1000000))
print(format_number_with_commas(12345))
print(format_number_with_commas(-99999999))
