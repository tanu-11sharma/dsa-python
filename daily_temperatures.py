"""
Daily Temperatures
----------------------
Given a list of daily temperatures, return a list where each entry is the
number of days you must wait after that day until a strictly warmer
temperature occurs. If no future day is warmer, put 0 for that day.

Time:  O(n)
Space: O(n), for the stack of pending day indices
"""

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack: List[int] = []  # indices of days still waiting for a warmer day

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer


if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # expected output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))  # expected output: [1, 1, 1, 0]
    print(daily_temperatures([30, 60, 90]))  # expected output: [1, 1, 0]
