"""
Palindrome Partitioning
-----------------------
Cut a string into consecutive pieces so that every piece reads the same
forwards and backwards, and collect every distinct way of doing so.
Backtracking extends the partition built so far with each palindromic prefix of
the untouched suffix, then undoes the choice before trying the next cut. A
precomputed table answers "is this slice a palindrome?" in constant time.

Time:  O(n * 2^n) in the worst case - one partition per subset of cut points
Space: O(n^2) for the palindrome table plus O(n) recursion depth
"""

from typing import List


def build_palindrome_table(text: str) -> List[List[bool]]:
    """table[i][j] is True when text[i:j + 1] is a palindrome."""
    n = len(text)
    table = [[False] * n for _ in range(n)]
    for end in range(n):
        for start in range(end, -1, -1):
            same_ends = text[start] == text[end]
            inner_ok = end - start < 2 or table[start + 1][end - 1]
            table[start][end] = same_ends and inner_ok
    return table


def partition_palindromes(text: str) -> List[List[str]]:
    """Return every partition of text into palindromic substrings."""
    n = len(text)
    is_palindrome = build_palindrome_table(text)

    results: List[List[str]] = []
    current: List[str] = []

    def backtrack(start: int) -> None:
        if start == n:
            results.append(list(current))
            return
        for end in range(start, n):
            if is_palindrome[start][end]:
                current.append(text[start:end + 1])
                backtrack(end + 1)
                current.pop()

    backtrack(0)
    return results


def minimum_cuts(text: str) -> int:
    """Fewest cuts needed so that every remaining piece is a palindrome."""
    if not text:
        return 0
    n = len(text)
    is_palindrome = build_palindrome_table(text)
    cuts = [0] * n
    for end in range(n):
        if is_palindrome[0][end]:
            cuts[end] = 0
            continue
        best = end
        for start in range(1, end + 1):
            if is_palindrome[start][end]:
                best = min(best, cuts[start - 1] + 1)
        cuts[end] = best
    return cuts[n - 1]


if __name__ == "__main__":
    print(partition_palindromes("aab"))
    # expected output: [['a', 'a', 'b'], ['aa', 'b']]

    print(partition_palindromes("abc"))
    # expected output: [['a', 'b', 'c']]

    print(len(partition_palindromes("aaa")))
    # expected output: 4

    print(minimum_cuts("aab"))
    # expected output: 1
