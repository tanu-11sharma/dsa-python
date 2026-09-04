"""
Word Break Using a Trie
-------------------------
Given a string `s` and a dictionary of words `word_dict`, determine whether
`s` can be split into a space-separated sequence of one or more dictionary
words (a word may be reused any number of times). The dictionary is first
loaded into a trie so each attempted split walks the trie one character at
a time instead of re-hashing substrings.

Time:  O(n^2) amortized, where n = len(s) (n possible start positions,
       each walking up to n trie characters)
Space: O(T + n), where T is the total number of characters in word_dict
"""

from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word = False


class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            self._insert(word)

    def _insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True


def word_break(s: str, word_dict: List[str]) -> bool:
    trie = Trie(word_dict)
    n = len(s)
    memo: Dict[int, bool] = {}

    def can_segment(start: int) -> bool:
        if start == n:
            return True
        if start in memo:
            return memo[start]

        node = trie.root
        result = False
        for end in range(start, n):
            ch = s[end]
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.is_word and can_segment(end + 1):
                result = True
                break

        memo[start] = result
        return result

    return can_segment(0)


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))  # expected output: True
    print(word_break("applepenapple", ["apple", "pen"]))  # expected output: True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # expected output: False
    print(word_break("", ["a"]))  # expected output: True
