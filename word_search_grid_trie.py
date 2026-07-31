"""
Find All Dictionary Words Hidden In A Letter Grid
-------------------------------------------------
Given a grid of letters and a dictionary of words, report every dictionary
word that can be spelled by walking the grid from cell to adjacent cell
(up, down, left, right) without reusing a cell within the same word.
All words are loaded into a trie first, so a single depth-first walk of the
grid can test every candidate word at once instead of one search per word.

Time:  O(rows * cols * 4^L) where L is the longest dictionary word
Space: O(total characters in the dictionary)
"""

from typing import Dict, List


class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str = ""


def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()
    for word in words:
        node = root
        for letter in word:
            node = node.children.setdefault(letter, TrieNode())
        node.word = word
    return root


def find_words_in_grid(grid: List[List[str]], words: List[str]) -> List[str]:
    if not grid or not grid[0] or not words:
        return []

    root = build_trie(words)
    rows, cols = len(grid), len(grid[0])
    found: List[str] = []

    def explore(row: int, col: int, node: TrieNode) -> None:
        letter = grid[row][col]
        child = node.children.get(letter)
        if child is None:
            return

        if child.word:
            found.append(child.word)
            child.word = ""  # report each word only once

        grid[row][col] = "#"
        for next_row, next_col in ((row - 1, col), (row + 1, col),
                                   (row, col - 1), (row, col + 1)):
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if grid[next_row][next_col] != "#":
                    explore(next_row, next_col, child)
        grid[row][col] = letter

        if not child.children:
            node.children.pop(letter, None)  # prune exhausted branches

    for row in range(rows):
        for col in range(cols):
            explore(row, col, root)

    return sorted(found)


if __name__ == "__main__":
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    print(find_words_in_grid(board, ["oath", "pea", "eat", "rain"]))  # expected output: ['eat', 'oath']

    print(find_words_in_grid([["a", "b"], ["c", "d"]], ["abcd", "acdb"]))  # expected output: ['acdb']

    print(find_words_in_grid([["a"]], ["a", "b"]))  # expected output: ['a']
