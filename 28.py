def count_peaks_valleys(price_action: list[int]) -> tuple[int, int]:
    peaks = 0
    valleys = 0
    for price_idx in range(1, len(price_action) - 1):
        if (
            price_action[price_idx - 1]
            < price_action[price_idx]
            > price_action[price_idx + 1]
        ):
            peaks += 1
        elif (
            price_action[price_idx - 1]
            > price_action[price_idx]
            < price_action[price_idx + 1]
        ):
            valleys += 1
    return peaks, valleys


print(count_peaks_valleys([1, 2, 3, 2, 1]))
print(count_peaks_valleys([1, 2, 3, 2, 1, 2]))
print(count_peaks_valleys([7, 6, 5, 10, 11, 12, 10, 9, 10]))
