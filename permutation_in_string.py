"""
Permutation In String
-----------------------
Given a short pattern and a longer text, decide whether any rearrangement of
the pattern appears as a contiguous block inside the text. Slide a window of
the pattern's length across the text and compare character counts, updating
the counts incrementally instead of recounting each window.

Time:  O(n)
Space: O(k), where k is the size of the alphabet
"""

from collections import Counter


def contains_permutation(pattern: str, text: str) -> bool:
    size = len(pattern)
    if size == 0 or size > len(text):
        return False

    need = Counter(pattern)
    window = Counter(text[:size])
    if window == need:
        return True

    for right in range(size, len(text)):
        window[text[right]] += 1
        left_char = text[right - size]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        if window == need:
            return True
    return False


if __name__ == "__main__":
    print(contains_permutation("abc", "lecabxyz"))  # expected output: True
    print(contains_permutation("abc", "lecaxbyz"))  # expected output: False
    print(contains_permutation("aa", "baaz"))  # expected output: True
    print(contains_permutation("abcd", "abc"))  # expected output: False
