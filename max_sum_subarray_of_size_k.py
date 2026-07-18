"""
Maximum Sum Subarray of Size K
----------------------------------------------------------------
Given a list of integers and a positive integer k, find the
maximum possible sum of any contiguous subarray of exactly length
k, using a fixed-size sliding window that slides one element at a
time instead of recomputing the sum from scratch.

Time:  O(n)
Space: O(1)
"""

from typing import List


def max_sum_subarray(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))
    # expected output: 9

    print(max_sum_subarray([2, 3, 4, 1, 5], 2))
    # expected output: 7

    print(max_sum_subarray([5, 5, 5, 5], 1))
    # expected output: 5
