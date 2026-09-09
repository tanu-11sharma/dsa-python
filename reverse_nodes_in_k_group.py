"""
Reverse Nodes in k-Group
-----------------------------------
Given the head of a singly linked list, reverse the nodes of the list
k at a time and return the new head. If the number of nodes remaining
at the end is fewer than k, leave that final group untouched.

Time:  O(n), each node is visited a constant number of times
Space: O(1) extra (in-place pointer rewiring, excluding the input/output list)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def build_list(values: list) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def has_k_nodes(node: Optional[ListNode], k: int) -> bool:
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    return count == k


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not has_k_nodes(head, k):
        return head

    prev, curr = None, head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # `head` is now the tail of this reversed group; its `next` should
    # point to the head of the (recursively reversed) remaining list.
    head.next = reverse_k_group(curr, k)
    return prev


if __name__ == "__main__":
    a = build_list([1, 2, 3, 4, 5])
    print(to_list(reverse_k_group(a, 2)))  # expected output: [2, 1, 4, 3, 5]

    b = build_list([1, 2, 3, 4, 5])
    print(to_list(reverse_k_group(b, 3)))  # expected output: [3, 2, 1, 4, 5]

    c = build_list([1, 2, 3])
    print(to_list(reverse_k_group(c, 1)))  # expected output: [1, 2, 3]

    d = build_list([])
    print(to_list(reverse_k_group(d, 4)))  # expected output: []
