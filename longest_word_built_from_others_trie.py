"""
Longest Word Built One Letter at a Time
---------------------------------------
Given a list of words, find the longest word that can be grown from a
single letter by appending one character at a time, where every
intermediate prefix is itself a word in the list. If several words tie in
length, return the one that comes first alphabetically; if no word
qualifies, return the empty string. Storing the words in a trie turns the
search into one depth-first walk that stops wherever a prefix is missing.

Time:  O(total characters)
Space: O(total characters)
"""

from typing import Dict, List, Optional


class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word: Optional[str] = None


def longest_buildable_word(words: List[str]) -> str:
    root = TrieNode()
    for word in words:
        node = root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.word = word

    best = ""

    def walk(node: TrieNode) -> None:
        nonlocal best
        for letter in sorted(node.children):
            child = node.children[letter]
            if child.word is None:
                continue
            if len(child.word) > len(best):
                best = child.word
            walk(child)

    walk(root)
    return best


if __name__ == "__main__":
    print(longest_buildable_word(["w", "wo", "wor", "worl", "world"]))
    # expected output: world

    print(longest_buildable_word(["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    # expected output: apple

    print(repr(longest_buildable_word(["cat", "dog", "bird"])))
    # expected output: ''
