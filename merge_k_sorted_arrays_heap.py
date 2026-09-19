"""
Merge K Sorted Arrays
------------------------
Given k arrays that are each individually sorted in ascending order,
merge them into a single sorted array using a min-heap that always
holds the smallest unconsumed element from each array.

Time:  O(N log k), where N is the total number of elements across all
       arrays and k is the number of arrays
Space: O(k) for the heap, plus O(N) for the output array
"""

from __future__ import annotations
import heapq


def merge_k_sorted_arrays(arrays: list[list[int]]) -> list[int]:
    heap: list[tuple[int, int, int]] = []

    # Seed the heap with the first element of every non-empty array.
    for array_index, array in enumerate(arrays):
        if array:
            heapq.heappush(heap, (array[0], array_index, 0))

    merged: list[int] = []
    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        merged.append(value)

        next_index = element_index + 1
        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(heap, (next_value, array_index, next_index))

    return merged


if __name__ == "__main__":
    print(merge_k_sorted_arrays([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
    # expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(merge_k_sorted_arrays([[1, 3], [], [2]]))
    # expected output: [1, 2, 3]

    print(merge_k_sorted_arrays([[5, 10, 15]]))
    # expected output: [5, 10, 15]

    print(merge_k_sorted_arrays([[], []]))
    # expected output: []
