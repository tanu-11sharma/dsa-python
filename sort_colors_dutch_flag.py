"""
Sort Colors (Dutch National Flag)
----------------------------------
Given an array containing only the values 0, 1, and 2, rearrange the
elements in place so that all 0s come first, followed by all 1s, and
then all 2s -- using a single pass and constant extra space.

Time:  O(n)
Space: O(1)
"""

from typing import List


def sort_colors(nums: List[int]) -> List[int]:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


if __name__ == "__main__":
    print(sort_colors([2, 0, 2, 1, 1, 0]))  # expected output: [0, 0, 1, 1, 2, 2]
    print(sort_colors([2, 0, 1]))  # expected output: [0, 1, 2]
    print(sort_colors([0]))  # expected output: [0]
    print(sort_colors([1, 2, 0, 2, 1, 0, 0]))  # expected output: [0, 0, 0, 1, 1, 2, 2]
