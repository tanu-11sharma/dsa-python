"""
Capacity to Ship Packages Within D Days
------------------------------------------
Packages, given as a list of weights in shipping order, must be loaded onto
a conveyor belt ship over exactly `days` days. Each day you load consecutive
packages without exceeding the ship's weight capacity for that day, and you
can't reorder or split a single package. Find the minimum ship capacity
that still gets everything shipped within `days` days, using binary search
over the range of possible capacities.

Time:  O(n log(sum(weights) - max(weights)))
Space: O(1)
"""


def ship_within_days(weights: list[int], days: int) -> int:
    def days_needed(capacity: int) -> int:
        trips = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                trips += 1
                current_load = 0
            current_load += w
        return trips

    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # expected output: 15
    print(ship_within_days([3, 2, 2, 4, 1, 4], 3))  # expected output: 6
    print(ship_within_days([1, 2, 3, 1, 1], 4))  # expected output: 3
