"""
Subarray Sums Divisible by K
-----------------------------
Given an integer array and an integer k, count how many contiguous
subarrays have a sum that is evenly divisible by k. Use running prefix
sums combined with the pigeonhole principle: two prefixes with the same
remainder mod k mean the subarray between them sums to a multiple of k.

Time:  O(n), a single pass over the array using a remainder-count hashmap.
Space: O(k), for the hashmap of prefix-sum remainders (at most k distinct
       remainders).
"""

from collections import defaultdict
from typing import List


def subarrays_div_by_k(nums: List[int], k: int) -> int:
    remainder_counts = defaultdict(int)
    remainder_counts[0] = 1  # empty prefix has remainder 0

    running_sum = 0
    count = 0
    for num in nums:
        running_sum += num
        remainder = running_sum % k  # Python's % always returns a non-negative result for positive k
        count += remainder_counts[remainder]
        remainder_counts[remainder] += 1

    return count


if __name__ == "__main__":
    print(subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))
    # expected output: 7

    print(subarrays_div_by_k([5], 9))
    # expected output: 0

    print(subarrays_div_by_k([-1, 2, 9], 2))
    # expected output: 2

    print(subarrays_div_by_k([2, 2, 2, 2], 2))
    # expected output: 10
