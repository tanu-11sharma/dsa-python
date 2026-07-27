"""
Find Minimum in Rotated Sorted Array
--------------------------------------
An array of distinct integers, originally sorted in ascending order,
has been rotated an unknown number of times. Find the minimum element
in O(log n) time using binary search on the rotation point.

Time:  O(log n)
Space: O(1)
"""

from typing import List


def find_min(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))  # expected output: 1
    print(find_min([4, 5, 6, 7, 0, 1, 2]))  # expected output: 0
    print(find_min([11, 13, 15, 17]))  # expected output: 11
    print(find_min([2, 1]))  # expected output: 1
