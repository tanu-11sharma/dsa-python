"""
Next Greater Element
----------------------
Given an array of integers, find, for each element, the first value to
its right that is strictly greater than it. If no such value exists,
report -1 for that position. Solve using a monotonic stack in a single
pass.

Time:  O(n)
Space: O(n)
"""

from typing import List


def next_greater_elements(nums: List[int]) -> List[int]:
    result = [-1] * len(nums)
    stack: List[int] = []  # indices whose next greater element is unresolved
    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            result[stack.pop()] = val
        stack.append(i)
    return result


if __name__ == "__main__":
    print(next_greater_elements([2, 1, 2, 4, 3]))  # expected output: [4, 2, 4, -1, -1]
    print(next_greater_elements([1, 2, 3, 4]))  # expected output: [2, 3, 4, -1]
    print(next_greater_elements([4, 3, 2, 1]))  # expected output: [-1, -1, -1, -1]
    print(next_greater_elements([5]))  # expected output: [-1]
