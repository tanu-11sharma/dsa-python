"""
Shortest Unique Prefix for Every Word
--------------------------------------
Given a list of distinct words, find the shortest prefix of each word
that is not a prefix of any other word in the list. Build a trie over
all the words, track how many words pass through each node, then walk
each word down the trie until reaching a node used by only one word.

Time:  O(N * L) to build and query, where N is the number of words and
       L is the maximum word length
Space: O(N * L) for the trie nodes
"""

from typing import Dict, List


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.count = 0


def shortest_unique_prefixes(words: List[str]) -> List[str]:
    root = TrieNode()

    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1

    result = []
    for word in words:
        node = root
        prefix = ""
        for ch in word:
            node = node.children[ch]
            prefix += ch
            if node.count == 1:
                break
        result.append(prefix)

    return result


if __name__ == "__main__":
    print(shortest_unique_prefixes(["zebra", "dog", "duck", "dove"]))
    # expected output: ['z', 'dog', 'du', 'dov']
    print(shortest_unique_prefixes(["bat", "ball", "cat"]))
    # expected output: ['bat', 'bal', 'c']
    print(shortest_unique_prefixes(["alone"]))
    # expected output: ['a']
