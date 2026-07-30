"""
Contains Nearby Duplicate
---------------------------
Given a list of integers and a window size k, decide whether the list has
two equal values that sit within k positions of each other. Formally, look
for indices i != j such that nums[i] == nums[j] and abs(i - j) <= k.
Track the most recent index of every value in a hash map.

Time:  O(n)
Space: O(n)
"""

from typing import Dict, List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    if k <= 0:
        return False
    last_seen: Dict[int, int] = {}
    for i, val in enumerate(nums):
        if val in last_seen and i - last_seen[val] <= k:
            return True
        last_seen[val] = i
    return False


if __name__ == "__main__":
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))  # expected output: True
    print(contains_nearby_duplicate([1, 2, 3, 1], 2))  # expected output: False
    print(contains_nearby_duplicate([1, 0, 1, 1], 1))  # expected output: True
    print(contains_nearby_duplicate([4, 5, 6, 7], 10))  # expected output: False
