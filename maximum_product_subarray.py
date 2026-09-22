"""
Maximum Product Subarray
-------------------------
Given an integer array, find the contiguous subarray (containing at
least one number) that has the largest product, and return that
product. Negative numbers can flip a small running product into a
large one, so track both the running max and running min product at
each step.

Time:  O(n)
Space: O(1)
"""

from typing import List


def max_product_subarray(nums: List[int]) -> int:
    if not nums:
        return 0

    best = cur_max = cur_min = nums[0]

    for num in nums[1:]:
        if num < 0:
            cur_max, cur_min = cur_min, cur_max
        cur_max = max(num, cur_max * num)
        cur_min = min(num, cur_min * num)
        best = max(best, cur_max)

    return best


if __name__ == "__main__":
    print(max_product_subarray([2, 3, -2, 4]))    # expected output: 6
    print(max_product_subarray([-2, 0, -1]))       # expected output: 0
    print(max_product_subarray([-2, 3, -4]))       # expected output: 24
    print(max_product_subarray([6]))               # expected output: 6
