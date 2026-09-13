"""
Implement Stack Using Queues
--------------------------------
Design a last-in-first-out (LIFO) stack using only the standard
operations of a first-in-first-out (FIFO) queue. Support push, pop,
top, and empty, using queue operations exclusively for the underlying
storage.

Time:  O(n) per push, O(1) for pop/top/empty
Space: O(n)
"""

from collections import deque


class MyStack:
    def __init__(self) -> None:
        self._queue: deque = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)
        for _ in range(len(self._queue) - 1):
            self._queue.append(self._queue.popleft())

    def pop(self) -> int:
        return self._queue.popleft()

    def top(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return len(self._queue) == 0


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    print(stack.top())  # expected output: 2
    print(stack.pop())  # expected output: 2
    print(stack.empty())  # expected output: False
