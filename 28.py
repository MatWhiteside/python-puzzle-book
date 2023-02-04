def print_triangle(n, symbol):
    for i in range(1, n + 1):
        print(" " * (n - i) + symbol * (2 * i - 1))


print_triangle(10, "*")
print_triangle(5, "|")
