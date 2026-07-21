"""
Remove Nth Node From End of List
---------------------------------
Given the head of a singly linked list, remove the n-th node counted from
the end of the list and return the head of the resulting list. Solved in
a single pass using a two-pointer gap technique.

Time:  O(L) where L is the length of the list
Space: O(1)
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def from_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2)))  # expected output: [1, 2, 3, 5]
    print(to_list(remove_nth_from_end(from_list([1]), 1)))  # expected output: []
    print(to_list(remove_nth_from_end(from_list([1, 2]), 1)))  # expected output: [1]
    print(to_list(remove_nth_from_end(from_list([1, 2, 3]), 3)))  # expected output: [2, 3]
