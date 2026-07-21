"""
Koko Eating Bananas
--------------------
Koko has piles of bananas and h hours before the guards return. Each hour
she chooses a pile and eats up to k bananas from it (if the pile has
fewer than k, she finishes it and stops for that hour). Find the minimum
integer eating speed k such that she can finish all piles within h hours.
Solved by binary searching over the answer space of possible speeds.

Time:  O(n log m) where m is the size of the largest pile
Space: O(1)
"""

import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    lo, hi = 1, max(piles)

    def hours_needed(speed: int) -> int:
        return sum(math.ceil(p / speed) for p in piles)

    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    print(min_eating_speed([3, 6, 7, 11], 8))  # expected output: 4
    print(min_eating_speed([30, 11, 23, 4, 20], 5))  # expected output: 30
    print(min_eating_speed([30, 11, 23, 4, 20], 6))  # expected output: 23
    print(min_eating_speed([1, 1, 1, 1], 4))  # expected output: 1
