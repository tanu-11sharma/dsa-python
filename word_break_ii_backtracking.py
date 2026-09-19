"""
Word Break II
---------------
Given a string `s` and a dictionary of words, return every way to
insert spaces into `s` so that the resulting sentence is made entirely
of dictionary words. Use backtracking with memoization so overlapping
suffixes are only solved once.

Time:  O(n^3) worst case (n = len(s)); each of the n starting indices
       can branch into up to n substrings, each checked in O(n)
Space: O(n^2) for the memo table of partial sentences
"""

from __future__ import annotations


def word_break_ii(s: str, word_dict: list[str]) -> list[str]:
    words = set(word_dict)
    memo: dict[int, list[str]] = {}

    def backtrack(start: int) -> list[str]:
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]

        sentences: list[str] = []
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece in words:
                for rest in backtrack(end):
                    sentence = piece if not rest else f"{piece} {rest}"
                    sentences.append(sentence)

        memo[start] = sentences
        return sentences

    return backtrack(0)


if __name__ == "__main__":
    print(word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    # expected output: ['cat sand dog', 'cats and dog']

    print(word_break_ii("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
    # expected output: ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple']

    print(word_break_ii("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # expected output: []
