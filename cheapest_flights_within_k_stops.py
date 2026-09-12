"""
Cheapest Flights Within K Stops
---------------------------------
There are n cities connected by directed flights, each with a cost. Given
a source, a destination, and a maximum number of stops k, find the cheapest
price to travel from source to destination using at most k stops. Return
-1 if no such route exists.

Time:  O(k * E), using a Bellman-Ford-style relaxation bounded by k rounds
Space: O(n) for the distance arrays
"""

from __future__ import annotations

from typing import List


def find_cheapest_price(
    n: int, flights: List[List[int]], src: int, dst: int, k: int
) -> int:
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0

    # Relax edges at most k + 1 times (k stops means k+1 hops). Using a
    # snapshot of the previous round prevents using more than one edge
    # update per city within the same round.
    for _ in range(k + 1):
        updated = dist[:]
        for u, v, cost in flights:
            if dist[u] != INF and dist[u] + cost < updated[v]:
                updated[v] = dist[u] + cost
        dist = updated

    return -1 if dist[dst] == INF else dist[dst]


if __name__ == "__main__":
    flights1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(find_cheapest_price(3, flights1, 0, 2, 1))
    # expected output: 200

    flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    print(find_cheapest_price(3, flights2, 0, 2, 0))
    # expected output: 500

    flights3 = [[0, 1, 100]]
    print(find_cheapest_price(2, flights3, 0, 1, 5))
    # expected output: 100

    flights4 = [[0, 1, 100]]
    print(find_cheapest_price(3, flights4, 0, 2, 5))
    # expected output: -1
