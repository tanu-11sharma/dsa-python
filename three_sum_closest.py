"""
Three Sum Closest
-----------------
Given an array of integers and a target value, choose exactly three of the
numbers so that their sum lands as close to the target as possible, and return
that sum. Sorting the array first lets a pair of converging pointers sweep the
remaining candidates for each fixed first element.

Time:  O(n^2)
Space: O(n) for the sorted copy
"""

from __future__ import annotations

from typing import List


def three_sum_closest(numbers: List[int], target: int) -> int:
    """Return the sum of the triple whose total is nearest to ``target``."""
    if len(numbers) < 3:
        raise ValueError("at least three numbers are required")

    ordered = sorted(numbers)
    best = ordered[0] + ordered[1] + ordered[2]

    for i in range(len(ordered) - 2):
        if i > 0 and ordered[i] == ordered[i - 1]:
            continue  # This first element was already explored.

        left, right = i + 1, len(ordered) - 1
        while left < right:
            total = ordered[i] + ordered[left] + ordered[right]
            if abs(total - target) < abs(best - target):
                best = total

            if total == target:
                return total
            if total < target:
                left += 1
            else:
                right -= 1

    return best


if __name__ == "__main__":
    print(three_sum_closest([-1, 2, 1, -4], 1))  # expected output: 2
    print(three_sum_closest([0, 0, 0], 1))  # expected output: 0
    print(three_sum_closest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))  # expected output: -2
