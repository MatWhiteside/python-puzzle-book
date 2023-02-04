def find_strings_containing_a(strings):
    return [s for s in strings if "a" in s]


print(find_strings_containing_a(["apple", "banana", "cherry", "date"]))  # should print ["apple", "banana"]
