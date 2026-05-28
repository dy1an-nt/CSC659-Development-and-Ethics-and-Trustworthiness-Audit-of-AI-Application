def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
print(binary_search(sorted_list, 23))
print(binary_search(sorted_list, 100))
