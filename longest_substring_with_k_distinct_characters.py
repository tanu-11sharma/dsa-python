"""
Longest Substring with At Most K Distinct Characters
------------------------------------------------------
Given a string s and an integer k, find the length of the longest
contiguous substring that contains at most k distinct characters. Expand
a sliding window to the right, and shrink it from the left whenever the
number of distinct characters inside the window exceeds k.

Time:  O(n), each character is added to and removed from the window at
       most once.
Space: O(k), for the hashmap tracking counts of characters in the window.
"""

from collections import defaultdict


def longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    char_counts = defaultdict(int)
    left = 0
    best = 0

    for right, char in enumerate(s):
        char_counts[char] += 1

        while len(char_counts) > k:
            left_char = s[left]
            char_counts[left_char] -= 1
            if char_counts[left_char] == 0:
                del char_counts[left_char]
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(longest_substring_k_distinct("eceba", 2))
    # expected output: 3

    print(longest_substring_k_distinct("aa", 1))
    # expected output: 2

    print(longest_substring_k_distinct("abcadcacacaca", 3))
    # expected output: 11

    print(longest_substring_k_distinct("abc", 0))
    # expected output: 0
