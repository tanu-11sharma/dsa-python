"""
Nth Ugly Number (Min-Heap)
---------------------------
An "ugly number" is a positive integer whose only prime factors are
2, 3, and 5. Given n, find the nth ugly number in increasing order
(1 is conventionally the first ugly number). Uses a min-heap to
generate candidates in sorted order without recomputing duplicates.

Time:  O(n log n) -- each of the n pops can push up to 3 heap entries
Space: O(n) for the heap and the seen set
"""

import heapq


def nth_ugly_number(n: int) -> int:
    factors = (2, 3, 5)
    heap = [1]
    seen = {1}
    value = 1
    for _ in range(n):
        value = heapq.heappop(heap)
        for f in factors:
            candidate = value * f
            if candidate not in seen:
                seen.add(candidate)
                heapq.heappush(heap, candidate)
    return value


if __name__ == "__main__":
    print(nth_ugly_number(1))  # expected output: 1
    print(nth_ugly_number(10))  # expected output: 12
    print(nth_ugly_number(15))  # expected output: 24
    print(nth_ugly_number(150))  # expected output: 5832
