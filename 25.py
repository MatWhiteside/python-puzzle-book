def validate_equation(equation: str) -> bool:
    try:
        num1, operator, num2, _, result = equation.split()
        if operator == "+":
            return int(num1) + int(num2) == int(result)
        if operator == "-":
            return int(num1) - int(num2) == int(result)
        return False
    except ValueError:
        return False


print(validate_equation("2 + 3 = 5"))
print(validate_equation("-5 + -6 = -11"))
print(validate_equation("-2 - 3 = -5"))
print(validate_equation("-2 + 3 = -5"))
print(validate_equation("not a valid equation fgd"))
