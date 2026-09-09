"""
Aggressive Cows
-----------------------------------
Given the positions of stalls along a line and a number of cows, place
all the cows into stalls so that the minimum distance between any two
cows is as large as possible. Return that largest possible minimum
distance. Binary search on the answer: for a candidate distance, greedily
check whether all cows can be placed at least that far apart.

Time:  O(n log n) for the sort plus O(n log(max_position)) for the search
Space: O(1) extra beyond the sorted positions
"""

from typing import List


def can_place(positions: List[int], cows: int, min_dist: int) -> bool:
    placed = 1
    last_position = positions[0]
    for pos in positions[1:]:
        if pos - last_position >= min_dist:
            placed += 1
            last_position = pos
            if placed == cows:
                return True
    return placed >= cows


def largest_minimum_distance(positions: List[int], cows: int) -> int:
    positions = sorted(positions)
    low, high = 1, positions[-1] - positions[0]
    best = 0
    while low <= high:
        mid = (low + high) // 2
        if can_place(positions, cows, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    return best


if __name__ == "__main__":
    print(largest_minimum_distance([1, 2, 4, 8, 9], 3))  # expected output: 3
    print(largest_minimum_distance([1, 2, 3, 4, 5], 2))  # expected output: 4
    print(largest_minimum_distance([10, 1, 2, 7, 5], 3))  # expected output: 4
    print(largest_minimum_distance([5, 5, 5, 5], 2))  # expected output: 0
