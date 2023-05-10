def fibonacci(sequence_number: int) -> int:
    if sequence_number in (0, 1):
        return sequence_number
    return fibonacci(sequence_number - 1) + fibonacci(sequence_number - 2)


print(fibonacci(4))
print(fibonacci(0))
print(fibonacci(6))
