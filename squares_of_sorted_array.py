"""
Squares of a Sorted Array
-------------------------
Given a list of integers already sorted in non-decreasing order (it may contain
negative values), produce a new sorted list holding the square of every element.
Squaring destroys the original ordering, but the largest square always sits at
one of the two ends, so a pair of converging pointers can fill the answer from
the back without any sorting step.

Time:  O(n)
Space: O(n)
"""

from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1

    for write in range(n - 1, -1, -1):
        left_sq = nums[left] * nums[left]
        right_sq = nums[right] * nums[right]
        if left_sq > right_sq:
            result[write] = left_sq
            left += 1
        else:
            result[write] = right_sq
            right -= 1

    return result


if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))
    # expected output: [0, 1, 9, 16, 100]

    print(sorted_squares([-7, -3, 2, 3, 11]))
    # expected output: [4, 9, 9, 49, 121]

    print(sorted_squares([1, 2, 3]))
    # expected output: [1, 4, 9]

    print(sorted_squares([]))
    # expected output: []
