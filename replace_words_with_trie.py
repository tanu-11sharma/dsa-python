"""
Replace Words With Trie
--------------------------
Given a dictionary of word roots and a sentence, replace every word in
the sentence with the shortest root from the dictionary that forms a
prefix of that word. Words with no matching root are left unchanged.
Solved by inserting all roots into a trie and walking each sentence word
down the trie until a root marker or mismatch is found.

Time:  O(R + S) where R is total root characters and S is total sentence characters
Space: O(R)
"""

from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_root_end = False


def replace_words(roots: List[str], sentence: str) -> str:
    trie_root = TrieNode()
    for word in roots:
        node = trie_root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_root_end = True

    def shortest_root(word: str) -> str:
        node = trie_root
        prefix = []
        for ch in word:
            if ch not in node.children:
                return word
            prefix.append(ch)
            node = node.children[ch]
            if node.is_root_end:
                return "".join(prefix)
        return word

    return " ".join(shortest_root(w) for w in sentence.split())


if __name__ == "__main__":
    print(replace_words(["cat", "bat", "rat"], "the cattle was rattled by the battery"))  # expected output: the cat was rat by the bat
    print(replace_words(["a", "b", "c"], "aadsfasf absfasf ac"))  # expected output: a a a
    print(replace_words(["catt", "cat", "bat", "rat"], "the cattle was rattled by the battery"))  # expected output: the cat was rat by the bat
    print(replace_words([], "no roots here"))  # expected output: no roots here
