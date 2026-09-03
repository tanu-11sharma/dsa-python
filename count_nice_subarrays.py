"""
Count Subarrays With Exactly K Odd Numbers
---------------------------------------------
Given an array of integers and an integer k, count the number of
contiguous subarrays that contain exactly k odd numbers. A subarray
qualifies purely by its odd-value count matching k, regardless of
the even values mixed in.

Time:  O(n)
Space: O(n) for the prefix-count map
"""

from collections import defaultdict


def count_nice_subarrays(nums: list[int], k: int) -> int:
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    odd_count = 0
    result = 0
    for num in nums:
        odd_count += num % 2
        result += prefix_counts[odd_count - k]
        prefix_counts[odd_count] += 1
    return result


if __name__ == "__main__":
    print(count_nice_subarrays([1, 1, 2, 1, 1], 3))  # expected output: 2
    print(count_nice_subarrays([2, 4, 6], 1))  # expected output: 0
    print(count_nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # expected output: 16
