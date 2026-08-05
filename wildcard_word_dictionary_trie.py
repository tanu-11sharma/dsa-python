"""
Wildcard Word Dictionary (Trie)
-------------------------------
Design a dictionary that stores words and answers membership queries in which
the query pattern may contain '.' as a single-character wildcard. A plain hash
set cannot answer wildcard queries, so words are stored in a trie and a query
containing a wildcard branches into every child at that position.

Time:  O(L) to add a word; O(L) per lookup with no wildcards and O(26^w * L)
       in the worst case for w wildcards, where L is the pattern length
Space: O(total characters stored)
"""

from typing import Dict, List, Optional


class _TrieNode:
    __slots__ = ("children", "is_word")

    def __init__(self) -> None:
        self.children: Dict[str, "_TrieNode"] = {}
        self.is_word = False


class WordDictionary:
    """A dictionary supporting '.' wildcard search over stored words."""

    def __init__(self) -> None:
        self._root = _TrieNode()

    def add(self, word: str) -> None:
        """Insert a word into the dictionary."""
        node = self._root
        for char in word:
            node = node.children.setdefault(char, _TrieNode())
        node.is_word = True

    def search(self, pattern: str) -> bool:
        """Return True if any stored word matches the pattern."""

        def walk(index: int, node: _TrieNode) -> bool:
            if index == len(pattern):
                return node.is_word

            char = pattern[index]
            if char == ".":
                return any(walk(index + 1, child) for child in node.children.values())

            child: Optional[_TrieNode] = node.children.get(char)
            return child is not None and walk(index + 1, child)

        return walk(0, self._root)


if __name__ == "__main__":
    dictionary = WordDictionary()
    for entry in ["bad", "dad", "mad", "bat"]:
        dictionary.add(entry)

    print(dictionary.search("pad"))
    # expected output: False

    print(dictionary.search("bad"))
    # expected output: True

    print(dictionary.search(".ad"))
    # expected output: True

    print(dictionary.search("b.."))
    # expected output: True

    print(dictionary.search("b...."))
    # expected output: False
