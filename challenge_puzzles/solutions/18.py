def get_number_of_digits(input_num: int) -> int:
    if input_num // 10 == 0:
        return 1
    return 1 + get_number_of_digits(input_num // 10)


print(get_number_of_digits(1234))
print(get_number_of_digits(0))
print(get_number_of_digits(123456789))
