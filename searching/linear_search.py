
def linear_search(arr, x):
    for i, val in enumerate(arr):
        if val == x:
            return i
    return -1

# Example
print(linear_search([1, 2, 3, 4, 5], 3))  # 2
print(linear_search([1, 2, 3, 4, 5], 6))  # -1

