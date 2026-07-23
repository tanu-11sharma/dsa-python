"""
Largest Rectangle in Histogram
--------------------------------
Given an array of non-negative integers representing the height of bars
in a histogram (each bar has width 1), find the area of the largest
rectangle that fits entirely under the skyline.

Time:  O(n)
Space: O(n)
"""
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    stack: List[int] = []  # indices of bars with increasing height
    max_area = 0
    bars = heights + [0]  # sentinel to flush any bars left on the stack

    for i, h in enumerate(bars):
        while stack and bars[stack[-1]] > h:
            height = bars[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # expected output: 10
    print(largest_rectangle_area([2, 4]))                # expected output: 4
    print(largest_rectangle_area([1, 1, 1, 1]))          # expected output: 4
    print(largest_rectangle_area([]))                    # expected output: 0
