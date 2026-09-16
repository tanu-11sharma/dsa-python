"""
Top K Frequent Words
---------------------
Given a list of words and an integer k, return the k most frequent
words. Ties in frequency are broken alphabetically, so among equally
frequent words the lexicographically smaller one ranks higher. Solved
with a heap keyed on (-frequency, word) so that popping the smallest k
elements yields the answer in the right order without a full sort.

Time:  O(N log N) where N is the number of distinct words (heap build
       plus popping); can be optimized to O(N log k) with a bounded
       min-heap, but this version favors clarity.
Space: O(N) for the frequency map and heap.
"""

import heapq
from collections import Counter
from typing import List


def top_k_frequent_words(words: List[str], k: int) -> List[str]:
    counts = Counter(words)

    # Min-heap ordered by (frequency, reverse-lexicographic word) so
    # that heapify + heappop naturally yields the top-k in descending
    # frequency / ascending alphabetical order when read via nlargest.
    heap = [(-freq, word) for word, freq in counts.items()]
    heapq.heapify(heap)

    result = []
    for _ in range(min(k, len(heap))):
        freq, word = heapq.heappop(heap)
        result.append(word)

    return result


if __name__ == "__main__":
    print(top_k_frequent_words(["i", "love", "leetcode", "i", "love", "coding"], 2))
    # expected output: ['i', 'love']

    print(top_k_frequent_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    # expected output: ['the', 'is', 'sunny', 'day']

    print(top_k_frequent_words(["a", "aa", "aaa"], 1))
    # expected output: ['a']

    print(top_k_frequent_words(["apple", "banana", "apple", "cherry", "banana", "apple"], 3))
    # expected output: ['apple', 'banana', 'cherry']
