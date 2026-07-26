"""
Network Delay Time
-----------------------------------
A signal is sent from a source node through a directed, weighted network
of n nodes described by a list of (source, target, travel_time) edges.
Determine the minimum time for the signal to reach every node in the
network, using Dijkstra's algorithm with a min-heap. Return -1 if some
node is unreachable.

Time:  O(E log V)
Space: O(V + E)
"""

import heapq
from collections import defaultdict
from typing import List


def network_delay_time(times: List[List[int]], n: int, source: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    best = {}
    heap = [(0, source)]

    while heap:
        dist, node = heapq.heappop(heap)
        if node in best:
            continue
        best[node] = dist

        for neighbor, weight in graph[node]:
            if neighbor not in best:
                heapq.heappush(heap, (dist + weight, neighbor))

    if len(best) != n:
        return -1
    return max(best.values())


if __name__ == "__main__":
    print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # expected output: 2
    print(network_delay_time([[1, 2, 1]], 2, 1))  # expected output: 1
    print(network_delay_time([[1, 2, 1]], 2, 2))  # expected output: -1
