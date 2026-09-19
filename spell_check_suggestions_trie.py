"""
Spell-Check Suggestions with a Trie
-------------------------------------
Build a dictionary of correctly spelled words into a trie. For a query
word, report whether it is spelled correctly, and if not, suggest every
dictionary word that shares the query's longest valid prefix.

Time:  O(L) per insert/query, plus O(k) to collect k suggestions, where
       L is word length
Space: O(total characters stored in the trie)
"""

from __future__ import annotations
from typing import Optional


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class SpellChecker:
    def __init__(self, dictionary: list[str]) -> None:
        self.root = TrieNode()
        for word in dictionary:
            self._insert(word)

    def _insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def is_correct(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    def _walk(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def suggest(self, word: str, limit: int = 5) -> list[str]:
        if self.is_correct(word):
            return [word]

        # Find the longest prefix of `word` that still exists in the trie.
        node = self.root
        longest_prefix = ""
        for i, ch in enumerate(word):
            if ch not in node.children:
                break
            node = node.children[ch]
            longest_prefix = word[: i + 1]

        results: list[str] = []
        self._collect(node, longest_prefix, results, limit)
        return results

    def _collect(self, node: TrieNode, prefix: str, results: list[str], limit: int) -> None:
        if len(results) >= limit:
            return
        if node.is_word:
            results.append(prefix)
        for ch in sorted(node.children):
            if len(results) >= limit:
                return
            self._collect(node.children[ch], prefix + ch, results, limit)


if __name__ == "__main__":
    checker = SpellChecker(["cat", "car", "cart", "care", "dog", "dodge"])

    print(checker.is_correct("car"))  # expected output: True
    print(checker.is_correct("carrot"))  # expected output: False
    print(checker.suggest("carrot"))  # expected output: ['car', 'care', 'cart']
    print(checker.suggest("do"))  # expected output: ['dodge', 'dog']
