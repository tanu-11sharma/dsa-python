"""
Trapping Rain Water
--------------------
Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much rainwater the map can trap between the
bars after it rains.

Time:  O(n)
Space: O(1)
"""

from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    trapped = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            trapped += right_max - height[right]

    return trapped


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected output: 6
    print(trap([4, 2, 0, 3, 2, 5]))  # expected output: 9
    print(trap([]))  # expected output: 0
