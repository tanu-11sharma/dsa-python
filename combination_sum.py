"""
Combination Sum
----------------
Given a list of distinct positive integers (candidates) and a target, return
all unique combinations of candidates that sum to target. The same number
may be reused an unlimited number of times.

Time:  O(2^t) worst case, where t = target / min(candidates)
Space: O(t) recursion depth, excluding the output
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    results: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path.copy())
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()

    candidates.sort()
    backtrack(0, target)
    return results


if __name__ == "__main__":
    print(combination_sum([2, 3, 6, 7], 7))  # expected output: [[2, 2, 3], [7]]
    print(combination_sum([2, 3, 5], 8))
    # expected output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(combination_sum([2], 1))  # expected output: []
