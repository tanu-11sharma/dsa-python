"""
Merge Sorted Array In Place
-----------------------------
Two sorted integer lists are given. The first list has m real values followed
by n placeholder slots (zeros) at the end, and the second list holds n values.
Merge the second list into the first so the first list ends up fully sorted,
without allocating extra storage. Fill from the back with two pointers.

Time:  O(m + n)
Space: O(1)
"""

from typing import List


def merge_sorted_array(first: List[int], m: int, second: List[int], n: int) -> None:
    write = m + n - 1
    i, j = m - 1, n - 1
    while j >= 0:
        if i >= 0 and first[i] > second[j]:
            first[write] = first[i]
            i -= 1
        else:
            first[write] = second[j]
            j -= 1
        write -= 1


if __name__ == "__main__":
    a = [1, 3, 5, 0, 0, 0]
    merge_sorted_array(a, 3, [2, 4, 6], 3)
    print(a)  # expected output: [1, 2, 3, 4, 5, 6]

    b = [0]
    merge_sorted_array(b, 0, [7], 1)
    print(b)  # expected output: [7]

    c = [4, 5, 6, 0, 0, 0]
    merge_sorted_array(c, 3, [1, 2, 3], 3)
    print(c)  # expected output: [1, 2, 3, 4, 5, 6]

    d = [2, 0]
    merge_sorted_array(d, 1, [1], 1)
    print(d)  # expected output: [1, 2]
