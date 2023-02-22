def filter_string_type(lst: list[str | int]) -> list[str]:
    return [x for x in lst if isinstance(x, str)]


print(filter_string_type(["hello", 1, 2, "www"]))
