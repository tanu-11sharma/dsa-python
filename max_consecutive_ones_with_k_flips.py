"""
Max Consecutive Ones With K Flips
------------------------------------
Given a binary array and an integer k, find the length of the longest
contiguous run of 1s that can be produced by flipping at most k zeros
to ones within that run.

Time:  O(n)
Space: O(1)
"""

from typing import List


def longest_ones(nums: List[int], k: int) -> int:
    left = 0
    zeros = 0
    best = 0
    for right, val in enumerate(nums):
        if val == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # expected output: 6
    print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))  # expected output: 10
    print(longest_ones([1, 1, 1], 0))  # expected output: 3
    print(longest_ones([0, 0, 0], 1))  # expected output: 1
