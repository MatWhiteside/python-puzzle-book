def get_parentheses_groups(input_str: str) -> list[str]:
    stack = []
    result = []
    start = 0
    for i, char in enumerate(input_str):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
                if len(stack) == 0:
                    result.append(input_str[start:i + 1].replace(" ", ""))
                    start = i + 1
    return result


print(get_parentheses_groups("(( ))  ((  ) ) (   ((  )))"))
print(get_parentheses_groups("( ( ( ( ( ( ( ) ) ) ) ) ) )"))
