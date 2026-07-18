"""
Top K Frequent Elements
---------------------------
Given an integer array and an integer k, return the k values that occur
most frequently in the array, ordered from most to least frequent. Ties
in frequency may be broken arbitrarily.

Time:  O(n log k), using a heap capped at size k
Space: O(n)
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    counts = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, counts.items(), key=lambda pair: pair[1])]


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # expected output: [1, 2]
    print(top_k_frequent([1], 1))  # expected output: [1]
    print(top_k_frequent([4, 4, 4, 6, 6, 7, 7, 7, 7], 2))  # expected output: [7, 4]
