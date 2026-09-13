"""
Smallest Divisor Given a Threshold
---------------------------------------
Given an array of positive integers and a threshold, find the smallest
positive integer divisor such that dividing every element by it
(rounding each result up) and summing the results yields a value less
than or equal to the threshold.

Time:  O(n log m), m = maximum value in nums
Space: O(1)
"""

import math
from typing import List


def smallest_divisor(nums: List[int], threshold: int) -> int:
    def sum_with_divisor(divisor: int) -> int:
        return sum(math.ceil(num / divisor) for num in nums)

    low, high = 1, max(nums)

    while low < high:
        mid = (low + high) // 2
        if sum_with_divisor(mid) <= threshold:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    print(smallest_divisor([1, 2, 5, 9], 6))  # expected output: 5
    print(smallest_divisor([44, 22, 33, 11, 1], 5))  # expected output: 44
    print(smallest_divisor([1, 1, 1], 3))  # expected output: 1
