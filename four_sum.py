"""
Four Sum
--------
Given an array of integers and a target value, find all unique
quadruples [a, b, c, d] drawn from the array whose sum equals the
target. Sort the array first, fix the outer two indices with nested
loops, then use the two-pointer technique on the remaining window to
find matching pairs while skipping duplicates.

Time:  O(n^3)
Space: O(1) extra, not counting the output list
"""

from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    results = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    results.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return results


if __name__ == "__main__":
    print(four_sum([1, 0, -1, 0, -2, 2], 0))
    # expected output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    print(four_sum([2, 2, 2, 2, 2], 8))
    # expected output: [[2, 2, 2, 2]]
    print(four_sum([1, 2, 3], 100))
    # expected output: []
