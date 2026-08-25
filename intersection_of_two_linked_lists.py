"""
Intersection of Two Linked Lists
---------------------------------
Two singly linked lists may merge into a shared tail at some node and
continue identically from there on. Given the heads of both lists, return
the node at which they intersect, or None if they never meet. Solve with
two pointers that each walk their own list and then switch to the other
list's head, guaranteeing they cover equal total distance and meet exactly
at the intersection (or both reach None together).

Time:  O(n + m)
Space: O(1)
"""

from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def get_intersection_node(head_a: ListNode | None, head_b: ListNode | None) -> ListNode | None:
    if not head_a or not head_b:
        return None

    pa, pb = head_a, head_b
    while pa is not pb:
        pa = pa.next if pa else head_b
        pb = pb.next if pb else head_a

    return pa


if __name__ == "__main__":
    # Shared tail: 8 -> 4 -> 5
    shared = ListNode(8, ListNode(4, ListNode(5)))
    list_a = ListNode(4, ListNode(1, shared))
    list_b = ListNode(5, ListNode(6, ListNode(1, shared)))
    result = get_intersection_node(list_a, list_b)
    print(result.val if result else None)  # expected output: 8

    list_c = ListNode(1, ListNode(2))
    list_d = ListNode(3, ListNode(4))
    print(get_intersection_node(list_c, list_d))  # expected output: None

    single = ListNode(7)
    print(get_intersection_node(single, single).val)  # expected output: 7
