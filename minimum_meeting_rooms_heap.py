"""
Minimum Meeting Rooms
---------------------
Given a list of meetings, each described by a start time and an end time, work
out the smallest number of rooms needed so that no two meetings ever occupy the
same room simultaneously. A meeting that ends exactly when another begins is
allowed to hand its room over.

Time:  O(n log n)
Space: O(n)
"""

from __future__ import annotations

import heapq
from typing import List, Tuple


def minimum_meeting_rooms(meetings: List[Tuple[int, int]]) -> int:
    """Return the fewest rooms that can host every meeting without overlap."""
    if not meetings:
        return 0

    # A min-heap of end times, one entry per room currently in use.
    in_use: List[int] = []

    for start, end in sorted(meetings, key=lambda meeting: meeting[0]):
        if in_use and in_use[0] <= start:
            # The earliest-finishing room is free again; reuse it.
            heapq.heapreplace(in_use, end)
        else:
            heapq.heappush(in_use, end)

    return len(in_use)


if __name__ == "__main__":
    print(minimum_meeting_rooms([(0, 30), (5, 10), (15, 20)]))  # expected output: 2
    print(minimum_meeting_rooms([(7, 10), (2, 4)]))  # expected output: 1
    print(minimum_meeting_rooms([(1, 5), (2, 6), (3, 7), (8, 9)]))  # expected output: 3
    print(minimum_meeting_rooms([]))  # expected output: 0
