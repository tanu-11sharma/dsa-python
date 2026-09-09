"""
IP Routing Table via Longest Prefix Match Trie
-----------------------------------
Model a simplified router's forwarding table. Each route is a binary
prefix (a string of '0'/'1' bits) mapped to an outgoing interface name.
Given a full binary address, find the outgoing interface for the
longest matching stored prefix (the most specific route wins), the way
IP routers perform longest-prefix-match lookups.

Time:  O(L) to insert or look up a route, where L is the bit length
Space: O(N * L) for N stored prefixes of length up to L
"""

from typing import Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.interface: Optional[str] = None


class RoutingTable:
    def __init__(self):
        self.root = TrieNode()

    def add_route(self, prefix: str, interface: str) -> None:
        node = self.root
        for bit in prefix:
            node = node.children.setdefault(bit, TrieNode())
        node.interface = interface

    def lookup(self, address: str) -> Optional[str]:
        node = self.root
        best_match = node.interface
        for bit in address:
            if bit not in node.children:
                break
            node = node.children[bit]
            if node.interface is not None:
                best_match = node.interface
        return best_match


if __name__ == "__main__":
    table = RoutingTable()
    table.add_route("10", "if0-default-ish")
    table.add_route("1010", "if1-more-specific")
    table.add_route("101011", "if2-most-specific")

    print(table.lookup("101011"))  # expected output: if2-most-specific
    print(table.lookup("101010"))  # expected output: if1-more-specific
    print(table.lookup("1011"))  # expected output: if0-default-ish
    print(table.lookup("0101"))  # expected output: None
