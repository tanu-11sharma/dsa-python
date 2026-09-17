"""
Min-Max Stack Design
---------------------
Design a stack that supports push, pop, top, and retrieving both the
current minimum and maximum element, all in O(1) time. Maintain two
auxiliary stacks alongside the main one to track running minimums
and maximums as elements are pushed and popped.

Time:  O(1) per operation
Space: O(n)
"""


class MinMaxStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self._min_stack: list[int] = []
        self._max_stack: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        prev_min = self._min_stack[-1] if self._min_stack else val
        prev_max = self._max_stack[-1] if self._max_stack else val
        self._min_stack.append(min(val, prev_min))
        self._max_stack.append(max(val, prev_max))

    def pop(self) -> int:
        self._min_stack.pop()
        self._max_stack.pop()
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]

    def get_max(self) -> int:
        return self._max_stack[-1]


if __name__ == "__main__":
    s = MinMaxStack()
    for v in [5, 1, 8, 2]:
        s.push(v)
    print(s.get_min(), s.get_max())  # expected output: 1 8
    s.pop()
    print(s.get_min(), s.get_max())  # expected output: 1 8
    s.pop()
    print(s.get_min(), s.get_max())  # expected output: 1 5
    print(s.top())  # expected output: 1
