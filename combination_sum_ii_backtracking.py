"""
Combination Sum II
---------------------
Given a collection of candidate numbers that may contain duplicates and a
target value, find every unique combination of candidates that sums to the
target. Each number from the collection may be used at most once per
combination, and the result must not contain duplicate combinations.

Time:  O(2^n) worst case for the search, with sorting adding O(n log n)
Space: O(n) for the recursion stack, plus O(2^n) for the output in the worst case
"""

from typing import List


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    results: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            results.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicate values at the same recursion depth to avoid
            # generating the same combination more than once.
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break

            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return results


if __name__ == "__main__":
    print(combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8))
    # expected output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

    print(combination_sum_ii([2, 5, 2, 1, 2], 5))
    # expected output: [[1, 2, 2], [5]]

    print(combination_sum_ii([2, 3, 6, 7], 7))
    # expected output: [[7]]
