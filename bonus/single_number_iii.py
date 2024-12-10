
def single_number_iii(nums):
    xor = 0
    for num in nums:
        xor ^= num
    rightmost_bit = xor & -xor
    a, b = 0, 0
    for num in nums:
        if num & rightmost_bit:
            a ^= num
        else:
            b ^= num
    return a, b

# Example
print(single_number_iii([1, 2, 1, 3, 2, 5]))  # (3, 5)

