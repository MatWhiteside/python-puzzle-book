def even_length_strings(strings):
    return [s for s in strings if len(s) % 2 == 0]


print(even_length_strings(["cat", "dog", "fish", "elephant"]))
