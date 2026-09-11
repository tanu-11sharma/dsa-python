"""
Middle of a Linked List
------------------------
Given the head of a singly linked list, return its middle node. When the
list has an even number of nodes, return the second of the two middle
nodes. Solved with the classic fast/slow pointer technique in one pass.

Time:  O(n)
Space: O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def build_list(values: List[int]) -> Optional[ListNode]:
    head = tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    print(to_list(middle_node(build_list([1, 2, 3, 4, 5]))))  # expected output: [3, 4, 5]
    print(to_list(middle_node(build_list([1, 2, 3, 4, 5, 6]))))  # expected output: [4, 5, 6]
    print(to_list(middle_node(build_list([1]))))  # expected output: [1]
    print(to_list(middle_node(build_list([1, 2]))))  # expected output: [2]
