def filter_type_str(input_list: list[str | int]) -> list[str]:
    return [list_item for list_item in input_list if isinstance(list_item, str)]


print(filter_type_str(["hello", 1, 2, "www"]))
print(filter_type_str([]))
print(filter_type_str([1, 2, 3, 4, 5]))
