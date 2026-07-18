"""
Kth Largest Element in a Stream
-----------------------------------
Maintain a running collection of integers and efficiently report, after
each new value is added, what the k-th largest element currently in the
collection is.

Time:  O(log k) per insertion, using a min-heap capped at size k
Space: O(k)
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap: List[int] = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))  # expected output: 4
    print(kth.add(5))  # expected output: 5
    print(kth.add(10))  # expected output: 5
    print(kth.add(9))  # expected output: 8
