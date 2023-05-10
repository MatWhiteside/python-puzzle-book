def get_parentheses_groups(input_str: str) -> list[str]:
    open_indices = []
    groups = []
    start_index = 0

    for i, char in enumerate(input_str):
        if char == "(":
            open_indices.append(i)
        elif char == ")":
            if open_indices:
                open_indices.pop()
                if not open_indices:
                    group = input_str[start_index:i + 1].replace(" ", "")
                    groups.append(group)
                    start_index = i + 1

    return groups


print(get_parentheses_groups("(( ))  ((  ) ) (   ((  )))"))
print(get_parentheses_groups("( ( ( ( ( ( ( ) ) ) ) ) ) )"))
print(get_parentheses_groups(""))
