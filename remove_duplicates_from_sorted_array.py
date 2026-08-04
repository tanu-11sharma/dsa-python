"""
Remove Duplicates From Sorted Array (At Most Twice)
---------------------------------------------------
Given a list sorted in non-decreasing order, compact it in place so that every
distinct value appears at most twice, keeping the original relative order.
Return the length k of the compacted prefix; the elements past index k - 1 may
hold anything. No extra array is allowed.

Time:  O(n)
Space: O(1)
"""

from typing import List


def remove_duplicates_keep_two(nums: List[int]) -> int:
    write = 0
    for value in nums:
        # Keep the value if we have written fewer than two copies of it so far.
        if write < 2 or nums[write - 2] != value:
            nums[write] = value
            write += 1
    return write


def remove_duplicates_keep_one(nums: List[int]) -> int:
    """Variant that allows each distinct value only once."""
    write = 0
    for value in nums:
        if write == 0 or nums[write - 1] != value:
            nums[write] = value
            write += 1
    return write


if __name__ == "__main__":
    a = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates_keep_two(a)
    print(k, a[:k])
    # expected output: 5 [1, 1, 2, 2, 3]

    b = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates_keep_two(b)
    print(k, b[:k])
    # expected output: 7 [0, 0, 1, 1, 2, 3, 3]

    c = [4, 4, 4, 9, 9]
    k = remove_duplicates_keep_one(c)
    print(k, c[:k])
    # expected output: 2 [4, 9]
