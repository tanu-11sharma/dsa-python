"""
Autocomplete Suggestions With a Trie
------------------------------------
A shop wants to show search suggestions while a customer types. Given the
catalogue of product names, report the products offered after each keystroke:
for every prefix of the query, list up to three catalogue entries that start
with that prefix, in lexicographic order.
Sorting once and caching the first three matches at each trie node makes every
lookup proportional to the length of the prefix.

Time:  O(m log m + C) to build for m products with C total characters,
       O(len(prefix)) per lookup
Space: O(C)
"""

from typing import Dict, List, Optional


class TrieNode:
    __slots__ = ("children", "suggestions")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.suggestions: List[str] = []


class AutocompleteIndex:
    """Prefix index that remembers the best few completions per node."""

    def __init__(self, products: List[str], limit: int = 3) -> None:
        self.limit = limit
        self.root = TrieNode()
        for product in sorted(products):
            self._insert(product)

    def _insert(self, product: str) -> None:
        node = self.root
        for letter in product:
            node = node.children.setdefault(letter, TrieNode())
            if len(node.suggestions) < self.limit:
                node.suggestions.append(product)

    def _descend(self, prefix: str) -> Optional[TrieNode]:
        node: Optional[TrieNode] = self.root
        for letter in prefix:
            if node is None:
                return None
            node = node.children.get(letter)
        return node

    def suggest(self, prefix: str) -> List[str]:
        """Return up to limit products starting with prefix."""
        node = self._descend(prefix)
        return list(node.suggestions) if node is not None else []

    def suggest_per_keystroke(self, query: str) -> List[List[str]]:
        """Return the suggestion list shown after each character of query."""
        results: List[List[str]] = []
        node: Optional[TrieNode] = self.root
        for letter in query:
            node = node.children.get(letter) if node is not None else None
            results.append(list(node.suggestions) if node is not None else [])
        return results


if __name__ == "__main__":
    index = AutocompleteIndex(["mouse", "mousepad", "monitor", "mop", "mango"])

    print(index.suggest("mo"))
    # expected output: ['monitor', 'mop', 'mouse']

    print(index.suggest("mou"))
    # expected output: ['mouse', 'mousepad']

    print(index.suggest("moz"))
    # expected output: []

    print(index.suggest_per_keystroke("mou"))
    # expected output: [['mango', 'monitor', 'mop'], ['monitor', 'mop', 'mouse'], ['mouse', 'mousepad']]
