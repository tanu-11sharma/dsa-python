"""
Search in a Rotated Sorted Array
---------------------------------
Given an array that was originally sorted in ascending order but has since
been rotated at some unknown pivot, and a target value, return the index of
the target if it exists, otherwise -1. The array contains no duplicates.

Time:  O(log n)
Space: O(1)
"""

from typing import List


def search_rotated(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            # Left half is sorted.
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # Right half is sorted.
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))  # expected output: 4
    print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))  # expected output: -1
    print(search_rotated([1], 0))  # expected output: -1
    print(search_rotated([5, 1, 3], 3))  # expected output: 2
