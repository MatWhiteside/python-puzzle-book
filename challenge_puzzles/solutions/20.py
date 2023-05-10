def print_triangle(number_of_levels: int, symbol: str) -> None:
    for level in range(1, number_of_levels + 1):
        print(" " * (number_of_levels - level) + symbol * (2 * level - 1))


print_triangle(3, "*")
print_triangle(1, "|")
print_triangle(5, ":")
