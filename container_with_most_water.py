"""
Container With Most Water
----------------------------------------------------------------
Given a list of non-negative integers representing vertical line
heights placed at each index along the x-axis, find two lines
that, together with the x-axis, form a container holding the most
water. Return the maximum amount of water the container can hold.

Time:  O(n)
Space: O(1)
"""

from typing import List


def max_area(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        best = max(best, width * height)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # expected output: 49

    print(max_area([1, 1]))
    # expected output: 1

    print(max_area([4, 3, 2, 1, 4]))
    # expected output: 16
