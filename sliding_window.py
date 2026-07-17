"""
Sliding Window: Longest Substring Without Repeating Characters
----------------------------------------------------------------
Given a string, find the length of the longest substring without
repeating characters, using a variable-size sliding window.

Time:  O(n)
Space: O(min(n, charset size))
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
    print(length_of_longest_substring("bbbbb"))      # 1 ("b")
    print(length_of_longest_substring("pwwkew"))     # 3 ("wke")
    print(length_of_longest_substring(""))           # 0
