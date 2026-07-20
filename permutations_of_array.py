"""
Permutations of an Array
-------------------------
Given a list of distinct integers, generate all possible orderings
(permutations) of the elements. Each permutation should use every
element exactly once.

Time:  O(n * n!)
Space: O(n * n!)
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i, num in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(num)
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    print(permute([1, 2, 3]))
    # expected output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] (order may vary)
    print(permute([0, 1]))
    # expected output: [[0,1],[1,0]]
    print(permute([5]))
    # expected output: [[5]]
