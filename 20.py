def print_triangle(number_of_levels: int, symbol: str) -> None:
    for i in range(1, number_of_levels + 1):
        print(" " * (number_of_levels - i) + symbol * (2 * i - 1))


print_triangle(10, "*")
print_triangle(5, "|")
