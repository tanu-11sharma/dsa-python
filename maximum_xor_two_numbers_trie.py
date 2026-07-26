"""
Maximum XOR of Two Numbers in an Array
-----------------------------------------
Given an array of non-negative integers, find the largest possible value
of a[i] XOR a[j] for any pair of elements. Insert every number's bit
pattern (most significant bit first) into a binary trie, then for each
number greedily walk the trie choosing the opposite bit at every level
to maximize the running XOR.

Time:  O(n * b), where b is the number of bits per number (32 here)
Space: O(n * b)
"""

from typing import List


class _BitTrieNode:
    def __init__(self):
        self.children = [None, None]


class BitTrie:
    def __init__(self, bit_length: int = 32):
        self.root = _BitTrieNode()
        self.bit_length = bit_length

    def insert(self, num: int) -> None:
        node = self.root
        for i in range(self.bit_length - 1, -1, -1):
            bit = (num >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = _BitTrieNode()
            node = node.children[bit]

    def max_xor_with(self, num: int) -> int:
        node = self.root
        result = 0
        for i in range(self.bit_length - 1, -1, -1):
            bit = (num >> i) & 1
            desired = 1 - bit
            if node.children[desired] is not None:
                result |= (1 << i)
                node = node.children[desired]
            else:
                node = node.children[bit]
        return result


def find_maximum_xor(nums: List[int]) -> int:
    if len(nums) < 2:
        return 0

    bit_length = max(nums).bit_length()
    trie = BitTrie(bit_length=max(bit_length, 1))
    for num in nums:
        trie.insert(num)

    best = 0
    for num in nums:
        best = max(best, trie.max_xor_with(num))
    return best


if __name__ == "__main__":
    print(find_maximum_xor([3, 10, 5, 25, 2, 8]))  # expected output: 28
    print(find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]))  # expected output: 127
    print(find_maximum_xor([0, 0]))  # expected output: 0
    print(find_maximum_xor([1]))  # expected output: 0
