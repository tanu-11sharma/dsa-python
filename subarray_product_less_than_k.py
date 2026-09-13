"""
Subarray Product Less Than K
-----------------------------
Given an array of positive integers and an integer k, count the number
of contiguous subarrays whose product of elements is strictly less
than k.

Time:  O(n)
Space: O(1)
"""

from typing import List


def num_subarrays_with_product_less_than_k(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0

    count = 0
    product = 1
    left = 0

    for right, value in enumerate(nums):
        product *= value
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1

    return count


if __name__ == "__main__":
    print(num_subarrays_with_product_less_than_k([10, 5, 2, 6], 100))  # expected output: 8
    print(num_subarrays_with_product_less_than_k([1, 2, 3], 0))  # expected output: 0
    print(num_subarrays_with_product_less_than_k([1, 1, 1], 2))  # expected output: 6
