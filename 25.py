def validate_equation(equation: str) -> bool:
    try:
        num1, operator, num2, _, result = equation.split()
        num1, num2, result = int(num1), int(num2), int(result)
        if operator == "+":
            return num1 + num2 == result
        if operator == "-":
            return num1 - num2 == result
        return False
    except ValueError:
        return False


print(validate_equation("2 + 3 = 5"))
print(validate_equation("-5 + -6 = -11"))
print(validate_equation("-2 - 3 = -5"))
print(validate_equation("-2 + 3 = -5"))
print(validate_equation("not a valid equation fgd"))
