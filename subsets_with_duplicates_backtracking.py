"""
Subsets With Duplicates
------------------------
Given an integer array that may contain duplicate values, return all
possible distinct subsets (the power set), without repeating the same
subset twice.

Time:  O(2^n) subsets, each built in O(n) -> O(n * 2^n)
Space: O(n) recursion depth, plus O(n * 2^n) for the output
"""

from __future__ import annotations

from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    nums.sort()
    results: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        results.append(path[:])
        for i in range(start, len(nums)):
            # Skip a value that is identical to the one just before it at
            # this same recursion depth, so we don't emit duplicate subsets.
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return results


if __name__ == "__main__":
    print(subsets_with_dup([1, 2, 2]))
    # expected output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

    print(subsets_with_dup([0]))
    # expected output: [[], [0]]

    print(subsets_with_dup([4, 4, 4, 1]))
    # expected output: [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [4], [4, 4], [4, 4, 4]]
