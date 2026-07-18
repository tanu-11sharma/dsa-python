"""
Group Anagrams
----------------------------------------------------------------
Given a list of strings, group the words that are anagrams of
each other into their own lists. Return the groups in any order;
within a group, words may appear in any order.

Time:  O(n * k log k), where n = number of strings, k = max string length
Space: O(n * k)
"""

from collections import defaultdict
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # expected output: groups like [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (order may vary)

    print(group_anagrams([""]))
    # expected output: [['']]

    print(group_anagrams(["a"]))
    # expected output: [['a']]
