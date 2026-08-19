"""
Median of Two Sorted Arrays
---------------------------
Two arrays are already sorted in non-decreasing order. Report the median
of their combined contents without merging them. Binary searching the
split point of the shorter array finds the partition where every value
on the left side is no larger than every value on the right side, and
the median falls straight out of the four values around that cut.

Time:  O(log min(m, n))
Space: O(1)
"""

from typing import List


def find_median_sorted_arrays(a: List[int], b: List[int]) -> float:
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    if m + n == 0:
        raise ValueError("at least one array must be non-empty")

    half = (m + n + 1) // 2
    low, high = 0, m

    while low <= high:
        i = (low + high) // 2
        j = half - i

        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < m else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < n else float("inf")

        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 1:
                return float(max(left_a, left_b))
            return (max(left_a, left_b) + min(right_a, right_b)) / 2

        if left_a > right_b:
            high = i - 1
        else:
            low = i + 1

    raise ValueError("both inputs must be sorted in non-decreasing order")


if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 3], [2]))     # expected output: 2.0
    print(find_median_sorted_arrays([1, 2], [3, 4]))  # expected output: 2.5
    print(find_median_sorted_arrays([], [5, 6, 7]))   # expected output: 6.0
    print(find_median_sorted_arrays([1, 1], [1, 1]))  # expected output: 1.0
