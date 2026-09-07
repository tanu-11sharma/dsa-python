"""
Count Triplets with Sum Less Than Target
------------------------------------------
Given an array of integers and a target value, count how many triplets
(i, j, k) with i < j < k satisfy nums[i] + nums[j] + nums[k] < target.

Time:  O(n^2)
Space: O(1) extra (excluding the sort)
"""

from typing import List


def three_sum_smaller(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    n = len(nums)
    count = 0

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < target:
                # Every pair between left and right (inclusive of left,
                # up to right - 1) paired with `left` also works, since
                # the array is sorted.
                count += right - left
                left += 1
            else:
                right -= 1

    return count


if __name__ == "__main__":
    print(three_sum_smaller([-2, 0, 1, 3], 2))  # expected output: 2
    print(three_sum_smaller([], 0))  # expected output: 0
    print(three_sum_smaller([0, 0, 0], 1))  # expected output: 1
