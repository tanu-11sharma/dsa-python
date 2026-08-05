"""
First and Last Position of a Target in a Sorted Array
-----------------------------------------------------
Given an array sorted in non-decreasing order and a target value, report the
index of the first occurrence of the target and the index of its last
occurrence. Return (-1, -1) when the target is absent. A linear scan would be
too slow, so both boundaries are located with binary search.

Time:  O(log n)
Space: O(1)
"""

from typing import List, Tuple


def _bound(nums: List[int], target: int, leftmost: bool) -> int:
    """Return the index of the first (or last) occurrence of target, else -1."""
    low, high = 0, len(nums) - 1
    found = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            found = mid
            # Keep searching the side that may hold a further occurrence.
            if leftmost:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return found


def search_range(nums: List[int], target: int) -> Tuple[int, int]:
    """Return (first_index, last_index) of target, or (-1, -1) if missing."""
    first = _bound(nums, target, leftmost=True)
    if first == -1:
        return (-1, -1)
    return (first, _bound(nums, target, leftmost=False))


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10], 8))
    # expected output: (3, 4)

    print(search_range([5, 7, 7, 8, 8, 10], 6))
    # expected output: (-1, -1)

    print(search_range([2, 2, 2, 2], 2))
    # expected output: (0, 3)

    print(search_range([], 1))
    # expected output: (-1, -1)
