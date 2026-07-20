"""
Find Peak Element
------------------
A peak element is one that is strictly greater than both of its
neighbors (out-of-bounds neighbors are treated as negative infinity).
Given an array of integers where adjacent elements are never equal,
return the index of any one peak element. Aim for better than linear
time.

Time:  O(log n)
Space: O(1)
"""

from typing import List


def find_peak_element(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    print(find_peak_element([1, 2, 3, 1]))
    # expected output: 2

    print(find_peak_element([1, 2, 1, 3, 5, 6, 4]) in (1, 5))
    # expected output: True

    print(find_peak_element([5]))
    # expected output: 0

    print(find_peak_element([1, 2]))
    # expected output: 1
