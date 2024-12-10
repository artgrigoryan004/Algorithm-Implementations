
def single_number_ii(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

# Example
print(single_number_ii([2, 2, 3, 2]))  # 3

