"""
Find Median from a Data Stream
-----------------------------------
Design a structure that accepts a continuous stream of integers one at a
time and can report the median of every number seen so far at any point.
Maintain two heaps: a max-heap holding the smaller half of the numbers
and a min-heap holding the larger half, keeping their sizes balanced.

Time:  O(log n) per insertion, O(1) to read the median
Space: O(n)
"""

import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        self.small: List[int] = []  # max-heap (values negated)
        self.large: List[int] = []  # min-heap

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    print(mf.find_median())  # expected output: 1.5
    mf.add_num(3)
    print(mf.find_median())  # expected output: 2.0
    mf.add_num(10)
    mf.add_num(-5)
    print(mf.find_median())  # expected output: 2.0
