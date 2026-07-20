"""
Longest Substring Without Repeating Characters
--------------------------------------------------
Given a string, find the length of the longest contiguous substring
that contains no repeated characters. Use a sliding window with a
hash map tracking the most recent index of each character.

Time:  O(n)
Space: O(min(n, alphabet size))
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
    # expected output: 3
    print(length_of_longest_substring("bbbbb"))
    # expected output: 1
    print(length_of_longest_substring("pwwkew"))
    # expected output: 3
    print(length_of_longest_substring(""))
    # expected output: 0
