"""
Find All Anagrams in a String
------------------------------
Given a text string and a pattern string, find the starting indices of
every substring of text that is an anagram of pattern (same letters,
any order). Slide a fixed-size window across text and track letter
frequency counts to detect matches efficiently.

Time:  O(n)
Space: O(1) (bounded alphabet size)
"""

from collections import Counter
from typing import List


def find_anagrams(text: str, pattern: str) -> List[int]:
    if len(pattern) > len(text):
        return []

    result = []
    pattern_count = Counter(pattern)
    window_count = Counter(text[: len(pattern)])

    if window_count == pattern_count:
        result.append(0)

    for i in range(len(pattern), len(text)):
        start_char = text[i - len(pattern)]
        window_count[start_char] -= 1
        if window_count[start_char] == 0:
            del window_count[start_char]

        window_count[text[i]] += 1

        if window_count == pattern_count:
            result.append(i - len(pattern) + 1)

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # expected output: [0, 6]
    print(find_anagrams("abab", "ab"))  # expected output: [0, 1, 2]
    print(find_anagrams("af", "be"))  # expected output: []
