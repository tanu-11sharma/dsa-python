"""
Smallest Range Covering Elements From K Lists
----------------------------------------------
You are given k sorted lists of integers. Find the smallest range [lo, hi]
such that at least one number from each of the k lists falls inside it.
If there are multiple ranges with the same (smallest) width, return the
one with the smallest starting value.

Time:  O(N log k), where N is the total number of elements across all lists
Space: O(k)
"""

from __future__ import annotations

import heapq
from typing import List, Tuple


def smallest_range(lists: List[List[int]]) -> Tuple[int, int]:
    # Min-heap of (value, list_index, element_index); track the current max
    # across the heap's frontier so we can measure the window width.
    heap: List[Tuple[int, int, int]] = []
    current_max = float("-inf")

    for i, lst in enumerate(lists):
        if not lst:
            return (0, 0)
        heapq.heappush(heap, (lst[0], i, 0))
        current_max = max(current_max, lst[0])

    best_lo, best_hi = float("-inf"), float("inf")

    while heap:
        current_min, list_idx, elem_idx = heapq.heappop(heap)

        if current_max - current_min < best_hi - best_lo:
            best_lo, best_hi = current_min, current_max

        # Advance the list we just popped from; if it runs out, no wider
        # range can ever cover all k lists again, so we're done.
        if elem_idx + 1 == len(lists[list_idx]):
            break

        next_val = lists[list_idx][elem_idx + 1]
        current_max = max(current_max, next_val)
        heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return (best_lo, best_hi)


if __name__ == "__main__":
    print(smallest_range([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    # expected output: (20, 24)

    print(smallest_range([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    # expected output: (1, 1)

    print(smallest_range([[10, 10], [11, 11]]))
    # expected output: (10, 11)
