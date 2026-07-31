"""
CPU Task Scheduling With A Cooldown Gap
---------------------------------------
A CPU runs one task per time unit. Two runs of the same task type must be
separated by at least n time units, and the CPU may sit idle to satisfy that.
Given the list of task labels and the cooldown n, return the shortest total
time needed to finish every task.
A max-heap always picks the most frequent task still available, while a queue
holds tasks that are cooling down until they become eligible again.

Time:  O(t * log k) where t is the total time and k the number of task types
Space: O(k)
"""

import heapq
from collections import Counter, deque
from typing import List


def least_time_to_finish(tasks: List[str], cooldown: int) -> int:
    if not tasks:
        return 0
    if cooldown < 0:
        raise ValueError("cooldown must be non-negative")

    max_heap = [-count for count in Counter(tasks).values()]
    heapq.heapify(max_heap)

    cooling: deque = deque()  # pairs of (remaining_count, time_it_becomes_ready)
    time = 0

    while max_heap or cooling:
        time += 1

        if max_heap:
            remaining = heapq.heappop(max_heap) + 1  # counts are negative
            if remaining != 0:
                cooling.append((remaining, time + cooldown))

        if cooling and cooling[0][1] == time:
            ready_count, _ = cooling.popleft()
            heapq.heappush(max_heap, ready_count)

    return time


if __name__ == "__main__":
    print(least_time_to_finish(["A", "A", "A", "B", "B", "B"], 2))  # expected output: 8
    print(least_time_to_finish(["A", "A", "A", "B", "B", "B"], 0))  # expected output: 6
    print(least_time_to_finish(["A", "B", "C", "D", "A", "B"], 2))  # expected output: 6
    print(least_time_to_finish([], 3))                              # expected output: 0
