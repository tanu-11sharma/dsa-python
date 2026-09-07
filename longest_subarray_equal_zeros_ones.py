"""
Longest Subarray with Equal Zeros and Ones
-------------------------------------------
Given a binary array (containing only 0s and 1s), find the length of the
longest contiguous subarray that contains an equal number of 0s and 1s.

Time:  O(n)
Space: O(n)
"""

from typing import List


def find_max_length(nums: List[int]) -> int:
    # Treat 0 as -1 so "equal counts" becomes "prefix sum returns to a
    # previously seen value".
    first_seen_at = {0: -1}
    running_sum = 0
    best = 0

    for i, num in enumerate(nums):
        running_sum += 1 if num == 1 else -1
        if running_sum in first_seen_at:
            best = max(best, i - first_seen_at[running_sum])
        else:
            first_seen_at[running_sum] = i

    return best


if __name__ == "__main__":
    print(find_max_length([0, 1]))  # expected output: 2
    print(find_max_length([0, 1, 0]))  # expected output: 2
    print(find_max_length([0, 0, 1, 0, 0, 1, 1]))  # expected output: 6
    print(find_max_length([1, 1, 1, 1]))  # expected output: 0
