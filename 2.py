def sum_with_none(x: int, y: int) -> int | None:
    if x + y < 50:
        return None
    return x + y


print(sum_with_none(20, 20))
print(sum_with_none(20, 30))
