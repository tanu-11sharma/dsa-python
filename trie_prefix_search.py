"""
Trie with Prefix Search
-------------------------
Design a trie (prefix tree) that supports inserting words, checking
whether an exact word has been inserted, and checking whether any
inserted word starts with a given prefix.

Time:  O(k) per operation, where k is the length of the word or prefix
Space: O(total characters inserted across all words)
"""

from typing import Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # expected output: True
    print(trie.search("app"))  # expected output: False
    print(trie.starts_with("app"))  # expected output: True
    trie.insert("app")
    print(trie.search("app"))  # expected output: True
