
import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i
    return -1

# Example
print(jump_search([1, 2, 3, 4, 5], 3))  # 2
print(jump_search([1, 2, 3, 4, 5], 6))  # -1

