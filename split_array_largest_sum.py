"""
Split Array Into K Parts With Smallest Largest Sum
--------------------------------------------------
Given a list of non-negative integers and an integer k, split the list into
exactly k non-empty contiguous parts. Among all valid splits we want the one
whose largest part-sum is as small as possible; return that value.
The answer is found by binary searching the candidate sum and greedily
checking how many parts that limit would require.

Time:  O(n * log(sum(nums)))
Space: O(1)
"""

from typing import List


def _parts_needed(nums: List[int], limit: int) -> int:
    """Fewest contiguous parts possible when no part may exceed limit."""
    parts, running = 1, 0
    for value in nums:
        if running + value > limit:
            parts += 1
            running = value
        else:
            running += value
    return parts


def split_array_largest_sum(nums: List[int], k: int) -> int:
    if not nums or k <= 0:
        raise ValueError("nums must be non-empty and k must be positive")

    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if _parts_needed(nums, mid) <= k:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    print(split_array_largest_sum([7, 2, 5, 10, 8], 2))  # expected output: 18
    print(split_array_largest_sum([1, 2, 3, 4, 5], 2))   # expected output: 9
    print(split_array_largest_sum([1, 4, 4], 3))         # expected output: 4
    print(split_array_largest_sum([2, 3, 1, 2, 4, 3], 1))  # expected output: 15
