def sum_if_less_than_fifty(num_one: int, num_two: int) -> int | None:
    # Calculate the sum of num_one and num_two, this avoids calculating
    # it twice on the return line
    summed_value = num_one + num_two

    # Return the summed value if it's less than 50, else return None
    return summed_value if summed_value < 50 else None


print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 30))
