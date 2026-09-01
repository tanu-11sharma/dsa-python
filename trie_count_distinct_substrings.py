"""
Count Distinct Substrings With a Trie
----------------------------------------
Given a string, count how many distinct (non-empty) substrings it
contains by inserting every suffix into a trie and counting the
number of brand-new nodes created along the way.

Time:  O(n^2)
Space: O(n^2)
"""

from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}


def count_distinct_substrings(s: str) -> int:
    root = TrieNode()
    count = 0

    for start in range(len(s)):
        node = root
        for ch in s[start:]:
            if ch not in node.children:
                node.children[ch] = TrieNode()
                count += 1
            node = node.children[ch]

    return count


if __name__ == "__main__":
    print(count_distinct_substrings("abc"))  # expected output: 6
    print(count_distinct_substrings("aaa"))  # expected output: 3
    print(count_distinct_substrings(""))  # expected output: 0
