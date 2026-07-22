"""
Product of Array Except Self
------------------------------
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all elements of nums except nums[i]. Division is
not allowed, and the solution must run in O(n) time.

Time:  O(n)
Space: O(1) extra, excluding the output array
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer


if __name__ == "__main__":
    print(product_except_self([1, 2, 3, 4]))  # expected output: [24, 12, 8, 6]
    print(product_except_self([-1, 1, 0, -3, 3]))  # expected output: [0, 0, 9, 0, 0]
    print(product_except_self([2, 3]))  # expected output: [3, 2]
