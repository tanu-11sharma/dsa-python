"""
Shortest Unique Prefix For Words
---------------------------------
Given a list of distinct lowercase words, find, for every word, the
shortest prefix of that word which does not occur as a prefix of any
other word in the list. Solved by building a trie over all words where
each node tracks how many words pass through it, then walking each word
down the trie until a node with a pass-through count of 1 is reached.

Time:  O(N * L) to build the trie and O(N * L) to answer all queries,
       where N is the number of words and L is the average word length.
Space: O(N * L) for the trie nodes.
"""

from typing import Dict, List


class _TrieNode:
    __slots__ = ("children", "count")

    def __init__(self) -> None:
        self.children: Dict[str, "_TrieNode"] = {}
        self.count = 0


def shortest_unique_prefixes(words: List[str]) -> List[str]:
    root = _TrieNode()

    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _TrieNode()
            node = node.children[ch]
            node.count += 1

    result = []
    for word in words:
        node = root
        prefix_chars = []
        for ch in word:
            node = node.children[ch]
            prefix_chars.append(ch)
            if node.count == 1:
                break
        result.append("".join(prefix_chars))

    return result


if __name__ == "__main__":
    print(shortest_unique_prefixes(["zebra", "dog", "duck", "dove"]))
    # expected output: ['z', 'dog', 'du', 'dov']

    print(shortest_unique_prefixes(["bat", "ball", "batman"]))
    # expected output: ['bat', 'bal', 'batm']

    print(shortest_unique_prefixes(["cat"]))
    # expected output: ['c']

    print(shortest_unique_prefixes(["alpha", "beta", "gamma"]))
    # expected output: ['a', 'b', 'g']
