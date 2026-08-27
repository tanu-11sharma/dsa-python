"""
Single Element in a Sorted Array
-----------------------------------
Given a sorted array where every element appears exactly twice except
for one element that appears only once, find that single element.
Binary search on the pair boundaries works here: before the lone
element each pair starts at an even index, and that pattern flips
right after it.

Time:  O(log n)
Space: O(1)
"""

from typing import List


def single_non_duplicate(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return nums[low]


if __name__ == "__main__":
    print(single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # expected output: 2
    print(single_non_duplicate([3, 3, 7, 7, 10, 11, 11]))  # expected output: 10
    print(single_non_duplicate([1, 1, 2]))  # expected output: 2
