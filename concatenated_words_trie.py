"""
Concatenated Words
---------------------
Given a list of distinct lowercase words, find every word that can be built
entirely by concatenating two or more other words from the same list. All
words are loaded into a trie so each candidate can be checked by walking the
trie and branching whenever a full word boundary is reached.

Time:  O(sum of word_length^2) across all words
Space: O(total characters)
"""
from typing import Dict, List


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

    def can_form(self, word: str) -> bool:
        n = len(word)

        def dfs(start: int, parts_used: int) -> bool:
            if start == n:
                return parts_used >= 2
            node = self.root
            for i in range(start, n):
                node = node.children.get(word[i])
                if node is None:
                    return False
                if node.is_word and dfs(i + 1, parts_used + 1):
                    return True
            return False

        return dfs(0, 0)


def find_all_concatenated_words(words: List[str]) -> List[str]:
    trie = Trie()
    for w in words:
        if w:
            trie.insert(w)
    return [w for w in words if w and trie.can_form(w)]


if __name__ == "__main__":
    words1 = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    print(sorted(find_all_concatenated_words(words1)))
    # expected output: ['catsdogcats', 'dogcatsdog', 'ratcatdogcat']

    words2 = ["cat", "dog", "catdog"]
    print(sorted(find_all_concatenated_words(words2)))
    # expected output: ['catdog']

    words3 = ["a", "b", "ab"]
    print(sorted(find_all_concatenated_words(words3)))
    # expected output: ['ab']
