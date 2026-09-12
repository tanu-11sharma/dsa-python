"""
Maximum Subarray Sum (Kadane's Algorithm)
-------------------------------------------
Given an integer array that may contain negative numbers, find the
contiguous subarray (containing at least one number) with the largest
possible sum, and return that sum.

Time:  O(n)
Space: O(1)
"""

from __future__ import annotations

from typing import List


def max_subarray(nums: List[int]) -> int:
    best_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        # Either extend the running subarray or start fresh at this
        # element, whichever yields a larger sum.
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # expected output: 6

    print(max_subarray([1]))
    # expected output: 1

    print(max_subarray([5, 4, -1, 7, 8]))
    # expected output: 23

    print(max_subarray([-3, -1, -2]))
    # expected output: -1
