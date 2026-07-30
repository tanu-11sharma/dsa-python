"""
Reorganize a String With a Max-Heap
-----------------------------------
Rearrange the letters of a string so that no two neighbouring letters are the
same, returning any valid arrangement or an empty string when the letter counts
make it impossible.
Repeatedly emitting the most frequent letter that is not the one just written
always succeeds whenever a solution exists; a max-heap keyed on the remaining
counts makes "most frequent" cheap to find.

Time:  O(n log a) for a string of length n over an alphabet of size a
Space: O(a)
"""

import heapq
from collections import Counter
from typing import List, Optional, Tuple


def reorganize_string(text: str) -> str:
    """Return a rearrangement with no equal adjacent letters, or an empty string."""
    counts = Counter(text)
    if counts and max(counts.values()) > (len(text) + 1) // 2:
        return ""

    # Negated counts turn Python's min-heap into a max-heap.
    heap: List[Tuple[int, str]] = [(-freq, ch) for ch, freq in counts.items()]
    heapq.heapify(heap)

    result: List[str] = []
    held: Optional[Tuple[int, str]] = None
    while heap:
        freq, ch = heapq.heappop(heap)
        result.append(ch)
        if held is not None:
            heapq.heappush(heap, held)
        # Hold this letter back for one round so it cannot repeat.
        held = (freq + 1, ch) if freq + 1 < 0 else None

    return "".join(result)


def is_valid_arrangement(text: str) -> bool:
    """Check that no two neighbouring characters are equal."""
    return all(a != b for a, b in zip(text, text[1:]))


if __name__ == "__main__":
    print(reorganize_string("aab"))
    # expected output: aba

    print(reorganize_string("aaab"))
    # expected output: (an empty line)

    print(reorganize_string("vvvlo"))
    # expected output: vlvov

    print(is_valid_arrangement(reorganize_string("aabbcc")))
    # expected output: True
