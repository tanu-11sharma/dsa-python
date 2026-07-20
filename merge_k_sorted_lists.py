"""
Merge K Sorted Linked Lists
------------------------------
Given an array of k singly linked lists, each sorted in non-decreasing
order, merge them all into a single sorted linked list and return its
head. Use a min-heap keyed on node value to repeatedly pull the
smallest head across all lists.

Time:  O(N log k), where N is the total number of nodes and k the number of lists
Space: O(k) for the heap
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            # tie-break on list index so ListNode objects are never compared
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


def _build(values: list) -> Optional[ListNode]:
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head


def _to_list(node: Optional[ListNode]) -> list:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    lists = [_build([1, 4, 5]), _build([1, 3, 4]), _build([2, 6])]
    print(_to_list(merge_k_sorted_lists(lists)))
    # expected output: [1, 1, 2, 3, 4, 4, 5, 6]

    print(_to_list(merge_k_sorted_lists([])))
    # expected output: []

    print(_to_list(merge_k_sorted_lists([None])))
    # expected output: []

    print(_to_list(merge_k_sorted_lists([_build([7])])))
    # expected output: [7]
