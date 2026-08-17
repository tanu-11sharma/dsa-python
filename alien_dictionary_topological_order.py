"""
Alien Dictionary Letter Order
-----------------------------
A word list from an unknown language is given in that language's own
lexicographic order, but its alphabet is unknown. Recover an ordering of the
letters that is consistent with the list. Return an empty string when the list
contradicts itself, or when a word is followed by a strict prefix of itself.

Time:  O(C) where C is the total number of characters across all words
Space: O(U) for the U distinct letters and the edges between them
"""

from collections import deque
from typing import Dict, List, Set


def alien_order(words: List[str]) -> str:
    """Return a letter ordering consistent with the sorted word list."""
    successors: Dict[str, Set[str]] = {c: set() for word in words for c in word}
    indegree: Dict[str, int] = {c: 0 for c in successors}

    for first, second in zip(words, words[1:]):
        for a, b in zip(first, second):
            if a != b:
                if b not in successors[a]:
                    successors[a].add(b)
                    indegree[b] += 1
                break
        else:
            if len(first) > len(second):
                return ""

    queue = deque(sorted(c for c in indegree if indegree[c] == 0))
    order: List[str] = []
    while queue:
        letter = queue.popleft()
        order.append(letter)
        for nxt in sorted(successors[letter]):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    return "".join(order) if len(order) == len(indegree) else ""


if __name__ == "__main__":
    print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
    # expected output: wertf

    print(alien_order(["cab", "aaa", "aab"]))
    # expected output: cab

    print(alien_order(["abc", "ab"]))
    # expected output: (empty string - prefix follows its extension)

    print(alien_order(["z", "x", "z"]))
    # expected output: (empty string - the constraints form a cycle)
