"""
Kth Missing Positive Number
----------------------------
Given a sorted array of distinct positive integers and an integer k,
determine the k-th positive integer that is missing from the array.

For example, in [2, 3, 4, 7, 11] the missing positive integers in order
are 1, 5, 6, 8, 9, 10, 12, ... so the 3rd missing number is 6.

Time:  O(log n)
Space: O(1)
"""

from typing import List


def find_kth_positive(arr: List[int], k: int) -> int:
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = (lo + hi) // 2
        # Number of missing positives before arr[mid] is arr[mid] - (mid + 1).
        missing_before = arr[mid] - (mid + 1)
        if missing_before < k:
            lo = mid + 1
        else:
            hi = mid

    # lo is the count of array elements that lie before the k-th missing
    # number, so the answer shifts by that many plus the k slots themselves.
    return lo + k


if __name__ == "__main__":
    print(find_kth_positive([2, 3, 4, 7, 11], 5))  # expected output: 9
    print(find_kth_positive([1, 2, 3, 4], 2))  # expected output: 6
    print(find_kth_positive([1, 2, 3, 4, 5, 6], 3))  # expected output: 9
    print(find_kth_positive([5, 6, 7, 8, 9], 4))  # expected output: 4
