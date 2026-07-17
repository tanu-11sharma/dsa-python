"""
Merge Intervals
----------------
Given a list of intervals, merge all overlapping intervals and return a
list of the non-overlapping intervals that cover all the intervals in the
input.

Time:  O(n log n)
Space: O(n)
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda pair: pair[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(merge([[1, 4], [4, 5]]))                      # [[1,5]]
