"""
Shortest Word Transformation Chain
----------------------------------
Given a start word, a target word and a dictionary of allowed words, find the
length of the shortest chain that turns the start into the target by changing a
single letter at a time, where every word after the start must appear in the
dictionary. The chain length counts both endpoints, and 0 means no chain exists.
Treating words as graph nodes turns this into a shortest-path search; grouping
words under wildcard patterns such as "h*t" gives the neighbour lists cheaply
without comparing every pair of words.

Time:  O(n * L^2) for n dictionary words of length L
Space: O(n * L)
"""

from collections import defaultdict, deque
from typing import Dict, List


def build_pattern_buckets(words: List[str]) -> Dict[str, List[str]]:
    """Map each one-letter-wildcard pattern to the words matching it."""
    buckets: Dict[str, List[str]] = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            buckets[word[:i] + "*" + word[i + 1:]].append(word)
    return buckets


def shortest_transformation_length(
    start: str, target: str, dictionary: List[str]
) -> int:
    """Length of the shortest one-letter-at-a-time chain, or 0 if none."""
    words = set(dictionary)
    if target not in words:
        return 0

    buckets = build_pattern_buckets(sorted(words | {start}))

    queue = deque([(start, 1)])
    seen = {start}
    while queue:
        word, steps = queue.popleft()
        if word == target:
            return steps
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            for neighbour in buckets.get(pattern, []):
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append((neighbour, steps + 1))
    return 0


if __name__ == "__main__":
    ladder = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(shortest_transformation_length("hit", "cog", ladder))
    # expected output: 5

    print(shortest_transformation_length("hit", "cog", ladder[:-1]))
    # expected output: 0

    print(shortest_transformation_length("a", "c", ["a", "b", "c"]))
    # expected output: 2

    print(shortest_transformation_length("hit", "hot", ladder))
    # expected output: 2
