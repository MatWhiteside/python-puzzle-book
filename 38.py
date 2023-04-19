def find_pairs_summing_to_target(
    input_nums: list[int], target: int
) -> list[tuple[int, int]]:

    pairs = []

    for left_idx, left_num in enumerate(input_nums):
        for _, right_num in enumerate(input_nums[left_idx + 1:]):

            if left_num + right_num == target:
                if (left_num, right_num) not in pairs:
                    pairs.append((left_num, right_num))

    return pairs


print(find_pairs_summing_to_target([5, 5, 5, 5], 10))
print(find_pairs_summing_to_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(find_pairs_summing_to_target([11, 12, 13, 14, 15], 5))


# Bonus solution
def find_pairs_summing_to_target_bonus(
    input_nums: list[int], target: int
) -> list[tuple[int, int]]:

    pairs = []
    seen = set()

    for input_num in input_nums:

        if target - input_num in seen:
            pairs.append((input_num, target - input_num))
        else:
            seen.add(input_num)

    return pairs


print(find_pairs_summing_to_target([5, 5, 5, 5], 10))
print(find_pairs_summing_to_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
print(find_pairs_summing_to_target([11, 12, 13, 14, 15], 5))
