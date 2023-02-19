def split_parentheses(s):
    stack = []
    result = []
    start = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if len(stack) > 0:
                stack.pop()
                if len(stack) == 0:
                    result.append(s[start:i + 1].replace(" ", ""))
                    start = i + 1
    return result


print(split_parentheses("(( ))  ((  ) ) (   ((  )))"))
print(split_parentheses("( ( ( ( ( ( ( ) ) ) ) ) ) )"))
