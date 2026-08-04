"""
Sliding Window Maximum (Monotonic Deque)
----------------------------------------
Given a list of integers and a window width k, slide a window of that width
from the left end to the right end and report the largest value inside the
window at every position. A monotonic decreasing deque of indices keeps the
current maximum at the front, so each element is pushed and popped once.

Time:  O(n)
Space: O(k)
"""

from collections import deque
from typing import List


def max_in_each_window(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums:
        return []
    if k > len(nums):
        return []

    window: deque = deque()  # holds indices, values strictly decreasing
    result: List[int] = []

    for i, value in enumerate(nums):
        # Drop indices that have slid out of the window on the left.
        if window and window[0] <= i - k:
            window.popleft()

        # Any smaller value behind the new one can never be a maximum again.
        while window and nums[window[-1]] <= value:
            window.pop()

        window.append(i)

        if i >= k - 1:
            result.append(nums[window[0]])

    return result


if __name__ == "__main__":
    print(max_in_each_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
    # expected output: [3, 3, 5, 5, 6, 7]

    print(max_in_each_window([9, 8, 7, 6], 2))
    # expected output: [9, 8, 7]

    print(max_in_each_window([4], 1))
    # expected output: [4]

    print(max_in_each_window([2, 5], 5))
    # expected output: []
