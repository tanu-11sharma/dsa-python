"""
Binary Search
-------------
Search a target value in a sorted array and return its index, or -1 if not
found.

Time:  O(log n)
Space: O(1)
"""
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    print(binary_search(nums, 9))   # 4
    print(binary_search(nums, 2))   # -1
