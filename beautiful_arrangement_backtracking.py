"""
Beautiful Arrangement
-----------------------
Suppose you have n integers labeled 1 through n arranged in some order.
An arrangement is called "beautiful" if, for every position i (1-indexed),
at least one of these is true: the number at position i is divisible by
i, or i is divisible by the number at position i. Count how many
beautiful arrangements exist for a given n, using backtracking with
pruning: numbers are placed one position at a time, and a branch is
abandoned the moment the divisibility rule is violated.

Time:  O(k) in practice where k is the count of valid arrangements
       explored, bounded above by O(n!) in the worst case before pruning.
Space: O(n) for the recursion stack and the "used" tracking array.
"""

from typing import List


def count_beautiful_arrangements(n: int) -> int:
    used = [False] * (n + 1)

    def backtrack(position: int) -> int:
        if position > n:
            return 1

        total = 0
        for candidate in range(1, n + 1):
            if used[candidate]:
                continue
            if candidate % position == 0 or position % candidate == 0:
                used[candidate] = True
                total += backtrack(position + 1)
                used[candidate] = False

        return total

    return backtrack(1)


def list_beautiful_arrangements(n: int) -> List[List[int]]:
    used = [False] * (n + 1)
    arrangements: List[List[int]] = []
    current: List[int] = []

    def backtrack(position: int) -> None:
        if position > n:
            arrangements.append(current.copy())
            return

        for candidate in range(1, n + 1):
            if used[candidate]:
                continue
            if candidate % position == 0 or position % candidate == 0:
                used[candidate] = True
                current.append(candidate)
                backtrack(position + 1)
                current.pop()
                used[candidate] = False

    backtrack(1)
    return arrangements


if __name__ == "__main__":
    print(count_beautiful_arrangements(2))
    # expected output: 2

    print(count_beautiful_arrangements(1))
    # expected output: 1

    print(count_beautiful_arrangements(4))
    # expected output: 8

    print(list_beautiful_arrangements(3))
    # expected output: [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
