"""
Quicksort
---------
In-place quicksort using Lomuto partition scheme with the last element as
pivot.

Time:  O(n log n) average, O(n^2) worst case
Space: O(log n) (recursion stack)
"""
from typing import List


def quicksort(arr: List[int], lo: int = 0, hi: int = None) -> List[int]:
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = _partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)
    return arr


def _partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [9, 3, 7, 1, 8, 2, 5]
    print(quicksort(data))  # [1, 2, 3, 5, 7, 8, 9]
