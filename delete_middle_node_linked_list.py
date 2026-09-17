"""
Delete the Middle Node of a Linked List
-----------------------------------------
Given the head of a singly linked list, delete its middle node and
return the head of the modified list. When the list has an even
number of nodes, treat the second of the two middle nodes as "the"
middle. Locate it in a single pass with the slow/fast pointer
technique.

Time:  O(n)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return None

    slow_prev = None
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow_prev = slow
        slow = slow.next
        fast = fast.next.next

    slow_prev.next = slow.next
    return head


def to_list(head: Optional[ListNode]) -> list[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def from_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(delete_middle(from_list([1, 3, 4, 7, 1, 2, 6]))))  # expected output: [1, 3, 4, 1, 2, 6]
    print(to_list(delete_middle(from_list([1, 2, 3, 4]))))  # expected output: [1, 2, 4]
    print(to_list(delete_middle(from_list([2, 1]))))  # expected output: [2]
    print(to_list(delete_middle(from_list([1]))))  # expected output: []
