"""
Longest Common Prefix via Trie
---------------------------------
Given a list of lowercase words, find the longest string that is a
prefix of every word in the list, returning "" if no common prefix
exists. Build a trie of all the words and walk down from the root
while each node has exactly one child and that child is shared by
every word, which naturally yields the longest common prefix.

Time:  O(N * L), where N is the number of words and L their average length
Space: O(N * L)
"""

from typing import Dict, List


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word_count = 0  # number of words passing through this node


def longest_common_prefix(words: List[str]) -> str:
    if not words:
        return ""

    root = TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.word_count += 1

    prefix_chars = []
    node = root
    while len(node.children) == 1:
        ch, child = next(iter(node.children.items()))
        if child.word_count != len(words):
            break
        prefix_chars.append(ch)
        node = child

    return "".join(prefix_chars)


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))
    # expected output: fl

    print(longest_common_prefix(["dog", "racecar", "car"]))
    # expected output: (empty string)

    print(longest_common_prefix(["interspecies", "interstellar", "interstate"]))
    # expected output: inters

    print(longest_common_prefix(["single"]))
    # expected output: single
