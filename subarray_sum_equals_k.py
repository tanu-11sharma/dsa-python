"""
Subarray Sum Equals K
-----------------------------------
Given an array of integers and a target integer k, count how many
contiguous subarrays sum exactly to k. Track a running prefix sum and a
hashmap of how many times each prefix sum has occurred; a subarray
ending at the current index sums to k whenever (running_sum - k) has
been seen before.

Time:  O(n)
Space: O(n)
"""

from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1

    running_sum = 0
    count = 0

    for num in nums:
        running_sum += num
        count += prefix_counts[running_sum - k]
        prefix_counts[running_sum] += 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))  # expected output: 2
    print(subarray_sum([1, 2, 3], 3))  # expected output: 2
    print(subarray_sum([1, -1, 0], 0))  # expected output: 3
    print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # expected output: 4
