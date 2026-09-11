"""
Peak Index in a Mountain Array
--------------------------------
A mountain array strictly increases to a single peak and then strictly
decreases. Given such an array, locate the index of the peak element
without a linear scan.

Time:  O(log n)
Space: O(1)
"""
from typing import List


def peak_index_in_mountain_array(arr: List[int]) -> int:
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    print(peak_index_in_mountain_array([0, 1, 0]))  # expected output: 1
    print(peak_index_in_mountain_array([0, 2, 1, 0]))  # expected output: 1
    print(peak_index_in_mountain_array([0, 10, 5, 2]))  # expected output: 1
    print(peak_index_in_mountain_array([1, 3, 5, 7, 6, 4, 2]))  # expected output: 3
