def filter_string_type(lst):
    return [x for x in lst if isinstance(x, str)]


print(filter_string_type(["hello", 1, 2, "www"]))
