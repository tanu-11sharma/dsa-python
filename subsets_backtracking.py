"""
Generate All Subsets (Power Set)
------------------------------------
Given a list of distinct integers, return every possible subset of that
list (the power set), including the empty subset and the full list
itself. No subset should appear more than once.

Time:  O(n * 2^n), to build and copy each of the 2^n subsets
Space: O(n * 2^n), to store the resulting subsets
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        result.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    print(subsets([1, 2, 3]))
    # expected output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    print(subsets([]))  # expected output: [[]]
    print(subsets([7]))  # expected output: [[], [7]]
