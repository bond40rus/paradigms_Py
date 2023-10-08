from typing import List


def binary_search(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1,3,7,9,3,9,0,2]

res = binary_search(arr, 7)
print(res)

# Структурная процедурная парадигма, функцианальная