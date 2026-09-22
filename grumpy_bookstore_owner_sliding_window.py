"""
Grumpy Bookstore Owner
-----------------------
A bookstore owner has `customers[i]` people entering during minute i,
and `satisfied[i]` marks whether those customers were happy (1) or
upset because the owner was grumpy that minute (0). The owner has one
"stay calm" technique that, if used, keeps them from being grumpy for
a single contiguous window of `minutes` minutes, satisfying everyone
in that window. Return the maximum total number of satisfied
customers achievable. Slide a window of size `minutes` over the
already-upset customers to find the best minute to start staying calm.

Time:  O(n)
Space: O(1)
"""

from typing import List


def max_satisfied(customers: List[int], satisfied: List[int], minutes: int) -> int:
    n = len(customers)
    base = sum(c for c, s in zip(customers, satisfied) if s == 1)

    window_gain = sum(
        customers[i] for i in range(min(minutes, n)) if satisfied[i] == 0
    )
    best_gain = window_gain

    for i in range(minutes, n):
        if satisfied[i] == 0:
            window_gain += customers[i]
        if satisfied[i - minutes] == 0:
            window_gain -= customers[i - minutes]
        best_gain = max(best_gain, window_gain)

    return base + best_gain


if __name__ == "__main__":
    print(max_satisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3))
    # expected output: 16
    print(max_satisfied([1], [0], 1))
    # expected output: 1
    print(max_satisfied([4, 10, 10], [1, 1, 1], 2))
    # expected output: 24
