"""
Longest Repeating Character Replacement
--------------------------------------------
Given a string of uppercase letters and an integer k, you may replace at
most k characters in the string with any other uppercase letter. Return
the length of the longest substring you can obtain that consists of a
single repeated character after making at most k replacements.

Time:  O(n)
Space: O(1), since the alphabet size is fixed
"""

from collections import Counter


def character_replacement(s: str, k: int) -> int:
    counts: Counter = Counter()
    left = 0
    max_count = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] += 1
        max_count = max(max_count, counts[ch])

        window_size = right - left + 1
        if window_size - max_count > k:
            counts[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))  # expected output: 4
    print(character_replacement("AABABBA", 1))  # expected output: 4
    print(character_replacement("AAAA", 0))  # expected output: 4
