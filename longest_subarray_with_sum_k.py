"""
Longest Subarray With Sum K
------------------------------
Given an array of integers (values may be negative) and a target sum
k, find the length of the longest contiguous subarray whose elements
sum to exactly k. Uses a running prefix sum with a hashmap recording
the earliest index at which each prefix sum was first seen.

Time:  O(n)
Space: O(n)
"""


def longest_subarray_with_sum_k(nums: list[int], k: int) -> int:
    prefix_sum_index: dict[int, int] = {0: -1}
    running_sum = 0
    best_length = 0
    for i, num in enumerate(nums):
        running_sum += num
        needed = running_sum - k
        if needed in prefix_sum_index:
            best_length = max(best_length, i - prefix_sum_index[needed])
        if running_sum not in prefix_sum_index:
            prefix_sum_index[running_sum] = i
    return best_length


if __name__ == "__main__":
    print(longest_subarray_with_sum_k([1, -1, 5, -2, 3], 3))  # expected output: 4
    print(longest_subarray_with_sum_k([-2, -1, 2, 1], 1))  # expected output: 2
    print(longest_subarray_with_sum_k([1, 2, 3], 6))  # expected output: 3
    print(longest_subarray_with_sum_k([1, 2, 3], 10))  # expected output: 0
