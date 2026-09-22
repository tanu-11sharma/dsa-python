"""
Online Stock Span
------------------
Design a class that receives a stock's daily price one day at a time
and, for each new price, returns its "span": the number of
consecutive days up to and including today where the price stayed
less than or equal to today's price. Maintain a monotonic decreasing
stack of (price, span) pairs so each call runs in amortized O(1) by
folding in any past spans that today's price outlasts.

Time:  O(1) amortized per call to next, O(n) total for n calls
Space: O(n)
"""

from typing import List, Tuple


class StockSpanner:
    def __init__(self) -> None:
        self._stack: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        span = 1
        while self._stack and self._stack[-1][0] <= price:
            span += self._stack.pop()[1]
        self._stack.append((price, span))
        return span


if __name__ == "__main__":
    spanner = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    print([spanner.next(p) for p in prices])  # expected output: [1, 1, 1, 2, 1, 4, 6]

    spanner2 = StockSpanner()
    print(spanner2.next(10))  # expected output: 1
    print(spanner2.next(10))  # expected output: 2
