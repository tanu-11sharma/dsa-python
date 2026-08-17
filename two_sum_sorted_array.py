"""
Two Sum in a Sorted Array
-------------------------
Given an array sorted in non-decreasing order and a target value, locate the two
positions whose values add up to the target. The same element may not be used
twice. Positions are reported as 1-based indices in increasing order, and an
empty list is returned when no pair qualifies.

Time:  O(n)  -- one inward sweep from both ends
Space: O(1)
"""

from typing import List


def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """Return the 1-based indices of the pair summing to target, or []."""
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))
    # expected output: [1, 2]

    print(two_sum_sorted([1, 3, 4, 5, 7, 11], 9))
    # expected output: [3, 4]

    print(two_sum_sorted([-3, 1, 4, 8], 5))
    # expected output: [1, 4]

    print(two_sum_sorted([-5, -2, 0, 6], 100))
    # expected output: []
