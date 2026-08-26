"""
Prefix Frequency Counter (Trie)
--------------------------------
Given a list of words, build a structure that can answer, for any prefix
string, how many words in the list start with that prefix. Also support
inserting new words on the fly. Uses a trie where each node stores a
count of how many inserted words pass through it.

Time:  O(L) per insert/query, where L is the length of the word/prefix
Space: O(N * L) for N words of average length L
"""


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.passing_count: int = 0
        self.end_count: int = 0


class PrefixCounter:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.passing_count += 1
        node.end_count += 1

    def count_prefix(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.passing_count

    def count_exact(self, word: str) -> int:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.end_count


if __name__ == "__main__":
    counter = PrefixCounter()
    for w in ["apple", "app", "application", "apt", "bat"]:
        counter.insert(w)

    print(counter.count_prefix("app"))  # expected output: 3
    print(counter.count_prefix("ap"))  # expected output: 4
    print(counter.count_exact("app"))  # expected output: 1
    print(counter.count_prefix("bat"))  # expected output: 1
    print(counter.count_prefix("cat"))  # expected output: 0
