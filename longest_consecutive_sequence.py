"""
Longest Consecutive Sequence
------------------------------
Given an unsorted array of integers, find the length of the longest
run of consecutive integers that appear in the array (the numbers
do not need to be contiguous in the array itself, just consecutive
in value). Solve it without sorting, in linear time.

Time:  O(n)
Space: O(n)
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start counting from the beginning of a sequence.
        if num - 1 in num_set:
            continue
        length = 1
        while num + length in num_set:
            length += 1
        longest = max(longest, length)

    return longest


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    # expected output: 4  (sequence: 1, 2, 3, 4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    # expected output: 9
    print(longest_consecutive([]))
    # expected output: 0
