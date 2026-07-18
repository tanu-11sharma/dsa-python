"""
Min Stack
----------------------------------------------------------------
Design a stack that supports push, pop, top, and retrieving the
current minimum element, all in O(1) time. An auxiliary stack
tracks the running minimum alongside the main data stack.

Time:  O(1) for push, pop, top, and get_min
Space: O(n)
"""

from typing import List


class MinStack:
    def __init__(self) -> None:
        self._stack: List[int] = []
        self._min_stack: List[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        current_min = val if not self._min_stack else min(val, self._min_stack[-1])
        self._min_stack.append(current_min)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    ms.push(1)
    print(ms.get_min())
    # expected output: 1

    ms.pop()
    print(ms.get_min())
    # expected output: 2

    print(ms.top())
    # expected output: 2
