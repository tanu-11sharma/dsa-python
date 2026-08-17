"""
First Missing Positive
----------------------
Given an unsorted array of integers, find the smallest positive integer that
does not appear anywhere in it. The array is rearranged in place so that, where
possible, the value v ends up at index v - 1; the first slot that breaks this
pattern reveals the answer.

Time:  O(n)  -- every swap places one value permanently
Space: O(1) beyond the input array, which is modified in place
"""

from typing import List


def first_missing_positive(nums: List[int]) -> int:
    """Return the smallest positive integer absent from nums."""
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            target = nums[i] - 1
            nums[i], nums[target] = nums[target], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == "__main__":
    print(first_missing_positive([1, 2, 0]))
    # expected output: 3

    print(first_missing_positive([3, 4, -1, 1]))
    # expected output: 2

    print(first_missing_positive([7, 8, 9, 11, 12]))
    # expected output: 1

    print(first_missing_positive([]))
    # expected output: 1
