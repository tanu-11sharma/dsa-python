"""
Sliding Window Median
-----------------------------------
Given an array of integers and a window size k, return the median of
each contiguous window of size k as it slides from the start of the
array to the end. Maintain two heaps (a max-heap of the smaller half
and a min-heap of the larger half) plus lazy deletion so elements that
fall out of the window are removed without rescanning the whole window.

Time:  O(n log k), each of the n slide steps does O(log k) heap work
Space: O(k) for the two heaps and the lazy-deletion bookkeeping
"""

import heapq
from collections import defaultdict
from typing import List


class SlidingWindowMedian:
    def __init__(self):
        self.small: List[int] = []  # max-heap (stored negated)
        self.large: List[int] = []  # min-heap
        self.delayed: dict = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def _prune(self, heap: List[int], is_small: bool) -> None:
        while heap:
            top = -heap[0] if is_small else heap[0]
            if self.delayed[top] > 0:
                self.delayed[top] -= 1
                heapq.heappop(heap)
            else:
                break

    def _rebalance(self) -> None:
        if self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            self.small_size -= 1
            heapq.heappush(self.large, val)
            self.large_size += 1
            self._prune(self.small, True)
        elif self.small_size < self.large_size:
            val = heapq.heappop(self.large)
            self.large_size -= 1
            heapq.heappush(self.small, -val)
            self.small_size += 1
            self._prune(self.large, False)

    def _add(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self._rebalance()

    def _remove(self, num: int) -> None:
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self._prune(self.small, True)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self._prune(self.large, False)
        self._rebalance()

    def _median(self, k: int) -> float:
        if k % 2 == 1:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


def median_sliding_window(nums: List[int], k: int) -> List[float]:
    tracker = SlidingWindowMedian()
    result = []
    for i, num in enumerate(nums):
        tracker._add(num)
        if i >= k:
            tracker._remove(nums[i - k])
        if i >= k - 1:
            result.append(tracker._median(k))
    return result


if __name__ == "__main__":
    print(median_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # expected output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]

    print(median_sliding_window([1, 2, 3, 4, 2, 3, 1, 4, 2], 3))
    # expected output: [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]

    print(median_sliding_window([1, 4, 2, 3], 4))
    # expected output: [2.5]
