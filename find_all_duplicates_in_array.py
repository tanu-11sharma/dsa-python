"""
Find All Duplicates in an Array
-------------------------------
An array of length n contains integers drawn from the range 1..n, and every
value appears either once or twice. Report each value that appears twice. The
array itself doubles as the bookkeeping structure: the sign of the slot a value
points at records whether that value has been seen before.

Time:  O(n)
Space: O(1) beyond the returned list
"""

from __future__ import annotations

from typing import List


def find_all_duplicates(numbers: List[int]) -> List[int]:
    """Return every value that occurs twice, in order of its second sighting."""
    duplicates: List[int] = []

    for value in numbers:
        slot = abs(value) - 1
        if numbers[slot] < 0:
            duplicates.append(abs(value))
        else:
            numbers[slot] = -numbers[slot]

    # Restore the caller's array to the state we found it in.
    for i, value in enumerate(numbers):
        numbers[i] = abs(value)

    return duplicates


if __name__ == "__main__":
    print(find_all_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # expected output: [2, 3]
    print(find_all_duplicates([1, 1, 2]))  # expected output: [1]
    print(find_all_duplicates([1, 2, 3, 4]))  # expected output: []
