"""
Longest Substring With At Most K Distinct Characters
----------------------------------------------------
Given a string and an integer k, find the length of the longest contiguous
substring containing no more than k distinct characters. If k is zero the
answer is zero; if the whole string already has k or fewer distinct
characters, the answer is simply its length.

Time:  O(n)
Space: O(k)
"""

from collections import defaultdict


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    if k <= 0:
        return 0

    counts: dict[str, int] = defaultdict(int)
    left = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] += 1

        while len(counts) > k:
            dropped = s[left]
            counts[dropped] -= 1
            if counts[dropped] == 0:
                del counts[dropped]
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(longest_substring_with_k_distinct("eceba", 2))    # expected output: 3
    print(longest_substring_with_k_distinct("aabbcc", 1))   # expected output: 2
    print(longest_substring_with_k_distinct("aabbcc", 3))   # expected output: 6
    print(longest_substring_with_k_distinct("abc", 0))      # expected output: 0
