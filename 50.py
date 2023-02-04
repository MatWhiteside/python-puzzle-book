def max_number(s):
    if len(s) < 4:
        raise ValueError("Input string should be of length greater than 3")
    nums = list(map(int, s))
    max_num = float('-inf')
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i+1:]):
            for k, num4 in enumerate(nums[i+j+2:]):
                for l, num3 in enumerate(nums[i+j+k+3:]):
                    max_num = max(max_num, num1+num2*num3/num4, num1*num2+num3/num4, num1*num2/num3+num4)
    return max_num

print(max_number("123456789"))