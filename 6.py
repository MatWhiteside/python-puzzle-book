def even_length_strings(strings: list[str]) -> list[str]:
    return [s for s in strings if len(s) % 2 == 0]


print(even_length_strings(["cat", "dog", "fish", "elephant"]))
