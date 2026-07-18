"""
3Sum
-------
Given an array of integers, find all unique triplets [a, b, c] such that
a + b + c equals zero. The returned list of triplets must not contain
duplicates.

Time:  O(n^2), after an O(n log n) sort
Space: O(1) extra space, excluding the output
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result: List[List[int]] = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    # expected output: [[-1, -1, 2], [-1, 0, 1]]
    print(three_sum([0, 1, 1]))  # expected output: []
    print(three_sum([0, 0, 0]))  # expected output: [[0, 0, 0]]
