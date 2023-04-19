def harmonic_sum(n: int) -> float:
    if n < 2:
        return 1
    return 1 / n + harmonic_sum(n - 1)


print(harmonic_sum(5))
print(harmonic_sum(2))
print(harmonic_sum(0))
