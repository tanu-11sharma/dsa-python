"""
Implement a Queue Using Two Stacks
----------------------------------
Build a first-in-first-out queue whose only storage is two last-in-first-out
stacks (Python lists restricted to append/pop from the end). Support push,
pop, peek and empty. Elements are moved from the inbox stack to the outbox
stack only when the outbox runs dry, which makes each element move at most
twice.

Time:  O(1) amortised per operation
Space: O(n)
"""

from typing import List, Optional


class QueueWithStacks:
    def __init__(self) -> None:
        self._inbox: List[int] = []   # newest elements land here
        self._outbox: List[int] = []  # reversed order, oldest on top

    def push(self, value: int) -> None:
        self._inbox.append(value)

    def _shift_if_needed(self) -> None:
        if not self._outbox:
            while self._inbox:
                self._outbox.append(self._inbox.pop())

    def pop(self) -> Optional[int]:
        """Remove and return the oldest element, or None if the queue is empty."""
        self._shift_if_needed()
        return self._outbox.pop() if self._outbox else None

    def peek(self) -> Optional[int]:
        self._shift_if_needed()
        return self._outbox[-1] if self._outbox else None

    def empty(self) -> bool:
        return not self._inbox and not self._outbox

    def __len__(self) -> int:
        return len(self._inbox) + len(self._outbox)


if __name__ == "__main__":
    q = QueueWithStacks()
    for n in (1, 2, 3):
        q.push(n)
    print(q.peek(), q.pop(), len(q))
    # expected output: 1 1 2

    q.push(4)
    print(q.pop(), q.pop(), q.pop())
    # expected output: 2 3 4

    print(q.empty(), q.pop())
    # expected output: True None
