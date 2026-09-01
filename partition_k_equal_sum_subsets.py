"""
Partition Into K Equal Sum Subsets
--------------------------------------
Given an array of positive integers and an integer k, determine
whether the array can be split into k non-empty subsets whose sums
are all equal, using backtracking with bucket assignment.

Time:  O(k^n) worst case
Space: O(n)
"""

from typing import List


def can_partition_k_subsets(nums: List[int], k: int) -> bool:
    total = sum(nums)
    if k <= 0 or total % k != 0:
        return False

    target = total // k
    nums.sort(reverse=True)
    if nums[0] > target:
        return False

    buckets = [0] * k

    def backtrack(index: int) -> bool:
        if index == len(nums):
            return True

        for i in range(k):
            if buckets[i] + nums[index] > target:
                continue

            buckets[i] += nums[index]
            if backtrack(index + 1):
                return True
            buckets[i] -= nums[index]

            if buckets[i] == 0:
                break

        return False

    return backtrack(0)


if __name__ == "__main__":
    print(can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4))  # expected output: True
    print(can_partition_k_subsets([1, 2, 3, 4], 3))  # expected output: False
    print(can_partition_k_subsets([2, 2, 2, 2], 2))  # expected output: True
