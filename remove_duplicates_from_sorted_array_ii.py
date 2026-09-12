"""
Remove Duplicates From Sorted Array II
-----------------------------------------
Given a sorted array, remove elements in place so that each distinct value
appears at most twice, preserving relative order. Return the new length;
the first `k` slots of the array should hold the resulting elements.

Time:  O(n)
Space: O(1) extra (in-place)
"""

from __future__ import annotations

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 2:
        return len(nums)

    # `write` marks the next position to fill. A candidate value is kept
    # whenever it differs from the value two slots back at the write
    # cursor, which automatically caps every value's count at two.
    write = 2
    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write


if __name__ == "__main__":
    arr1 = [1, 1, 1, 2, 2, 3]
    length1 = remove_duplicates(arr1)
    print(length1, arr1[:length1])
    # expected output: 5 [1, 1, 2, 2, 3]

    arr2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    length2 = remove_duplicates(arr2)
    print(length2, arr2[:length2])
    # expected output: 7 [0, 0, 1, 1, 2, 3, 3]

    arr3 = [1, 1, 1]
    length3 = remove_duplicates(arr3)
    print(length3, arr3[:length3])
    # expected output: 2 [1, 1]
