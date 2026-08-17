"""
Two Sum in a Sorted Array
-------------------------
Given an array of integers already sorted in non-decreasing order and a target
value, locate the one pair of distinct positions whose values add up to the
target and report those positions as one-based indices. Solve it without any
auxiliary data structure. Return an empty tuple when no such pair exists.

Time:  O(n) -- the two ends of the scan never move backwards
Space: O(1)
"""

from typing import List, Tuple


def two_sum_sorted(numbers: List[int], target: int) -> Tuple[int, ...]:
    """Return the 1-based index pair summing to target, or an empty tuple."""
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return (left + 1, right + 1)
        if total < target:
            left += 1
        else:
            right -= 1

    return ()


if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))
    # expected output: (1, 2)

    print(two_sum_sorted([1, 3, 4, 5, 7], 9))
    # expected output: (3, 4)

    print(two_sum_sorted([-3, -1, 0, 2, 6], 3))
    # expected output: (1, 5)

    print(two_sum_sorted([1, 2, 3], 7))
    # expected output: ()
