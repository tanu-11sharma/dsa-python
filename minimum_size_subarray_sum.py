"""
Shortest Subarray With Sum At Least Target
------------------------------------------
Given an array of positive integers and a target value, find the length of the
shortest contiguous block of the array whose elements add up to the target or
more. Return 0 when no block reaches the target. Because every value is
positive, a window can be grown on the right and shrunk on the left greedily.

Time:  O(n) -- each index enters and leaves the window at most once
Space: O(1)
"""

from typing import List


def min_subarray_length(nums: List[int], target: int) -> int:
    """Return the length of the shortest subarray summing to at least target."""
    left = 0
    window_sum = 0
    best = len(nums) + 1

    for right, value in enumerate(nums):
        window_sum += value
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return best if best <= len(nums) else 0


if __name__ == "__main__":
    print(min_subarray_length([2, 3, 1, 2, 4, 3], 7))
    # expected output: 2

    print(min_subarray_length([1, 4, 4], 4))
    # expected output: 1

    print(min_subarray_length([1, 1, 1, 1], 7))
    # expected output: 0

    print(min_subarray_length([], 5))
    # expected output: 0
