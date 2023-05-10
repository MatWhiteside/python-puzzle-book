def is_valid_equation(input_equation: str) -> bool:
    try:
        left_num, operator, right_num, _, result_num = input_equation.split()
        if operator == "+":
            return int(left_num) + int(right_num) == int(result_num)
        if operator == "-":
            return int(left_num) - int(right_num) == int(result_num)
        return False
    except ValueError:
        return False


print(is_valid_equation("2 + 3 = 5"))
print(is_valid_equation("-5 + -6 = -11"))
print(is_valid_equation("-2 - 3 = -5"))
print(is_valid_equation("-2 + 3 = -5"))
print(is_valid_equation("not a valid equation !"))
