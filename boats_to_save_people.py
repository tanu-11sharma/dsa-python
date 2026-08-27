"""
Boats to Save People
---------------------
Given the weights of people and a boat weight limit, pair the lightest
person with the heaviest person whenever their combined weight fits
within the limit, otherwise send the heavy person alone. Determine the
minimum number of boats needed to carry everyone across, where each
boat carries at most two people.

Time:  O(n log n)
Space: O(1) (excluding sort)
"""

from typing import List


def num_rescue_boats(people: List[int], limit: int) -> int:
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats


if __name__ == "__main__":
    print(num_rescue_boats([1, 2], 3))  # expected output: 1
    print(num_rescue_boats([3, 2, 2, 1], 3))  # expected output: 3
    print(num_rescue_boats([3, 5, 3, 4], 5))  # expected output: 4
    print(num_rescue_boats([5, 1, 4, 2], 6))  # expected output: 2
