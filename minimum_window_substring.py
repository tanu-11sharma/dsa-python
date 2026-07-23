"""
Minimum Window Substring
-------------------------
Given two strings s and t, find the smallest contiguous window in s that
contains every character of t (including duplicates). Return an empty
string if no such window exists.

Time:  O(n + m) where n = len(s), m = len(t)
Space: O(m)
"""
from collections import Counter
from typing import Dict


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need: Dict[str, int] = Counter(t)
    missing = len(t)
    left = 0
    best_left, best_right = 0, 0

    for right, char in enumerate(s, 1):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        if missing == 0:
            while need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if best_right == 0 or right - left < best_right - best_left:
                best_left, best_right = left, right
            need[s[left]] += 1
            missing += 1
            left += 1

    return s[best_left:best_right]


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # expected output: "BANC"
    print(min_window("a", "a"))                 # expected output: "a"
    print(min_window("a", "aa"))                 # expected output: ""
    print(min_window("ab", "b"))                 # expected output: "b"
