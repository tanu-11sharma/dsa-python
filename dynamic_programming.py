"""
Dynamic Programming: 0/1 Knapsack
-----------------------------------
Given item weights, values, and a capacity, find the maximum total value
that fits in the knapsack without exceeding capacity (each item used at
most once). Bottom-up DP with a 1D rolling array.

Time:  O(n * capacity)
Space: O(capacity)
"""
from typing import List


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        w, v = weights[i], values[i]
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)

    return dp[capacity]


if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    print(knapsack(weights, values, capacity))  # 9 (items with weight 3+4)
