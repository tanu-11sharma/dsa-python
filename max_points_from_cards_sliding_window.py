"""
Maximum Score from Card Piles
-------------------------------
There is a row of cards, each with a point value. You may take exactly k
cards total, and each move takes one card from either the very front or
the very back of the row. Return the maximum total points obtainable.

Time:  O(n)
Space: O(1)
"""

from typing import List


def max_score(card_points: List[int], k: int) -> int:
    n = len(card_points)
    window_size = n - k

    if window_size <= 0:
        return sum(card_points)

    # The cards you *don't* take form one contiguous inner window; taking
    # k cards from the ends is equivalent to leaving behind the minimum
    # sum window of size (n - k).
    total = sum(card_points)
    window_sum = sum(card_points[:window_size])
    min_window = window_sum

    for i in range(window_size, n):
        window_sum += card_points[i] - card_points[i - window_size]
        min_window = min(min_window, window_sum)

    return total - min_window


if __name__ == "__main__":
    print(max_score([1, 2, 3, 4, 5, 6, 1], 3))  # expected output: 12
    print(max_score([2, 2, 2], 2))  # expected output: 4
    print(max_score([9, 7, 7, 9, 7, 7, 9], 7))  # expected output: 55
    print(max_score([1, 1000, 1], 1))  # expected output: 1
