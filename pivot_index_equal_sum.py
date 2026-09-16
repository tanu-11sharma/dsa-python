"""
Pivot Index (Equilibrium Point)
----------------------------------
Given an array of integers, find the leftmost index whose left-hand sum
(all elements strictly before it) equals its right-hand sum (all
elements strictly after it). Return -1 if no such index exists. Solved
in a single pass by keeping a running "left sum" and deriving the right
sum on the fly from the array's total, avoiding any nested summation.

Time:  O(n), one pass to total the array and one pass to scan for the
       pivot.
Space: O(1) beyond the input array.
"""

from typing import List


def pivot_index(nums: List[int]) -> int:
    total = sum(nums)
    left_sum = 0

    for i, value in enumerate(nums):
        right_sum = total - left_sum - value
        if left_sum == right_sum:
            return i
        left_sum += value

    return -1


if __name__ == "__main__":
    print(pivot_index([1, 7, 3, 6, 5, 6]))
    # expected output: 3

    print(pivot_index([1, 2, 3]))
    # expected output: -1

    print(pivot_index([2, 1, -1]))
    # expected output: 0

    print(pivot_index([-1, -1, -1, 0, 1, 1]))
    # expected output: 0
