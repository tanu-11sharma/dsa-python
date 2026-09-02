"""
Isomorphic Strings
-------------------
Given two strings s and t, determine whether the characters in s can be
consistently remapped to the characters in t such that replacing every
occurrence of a character in s with its mapped character produces t,
with no two characters mapping to the same target character.

Time:  O(n)
Space: O(k) where k is the size of the character set
"""


def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for cs, ct in zip(s, t):
        if cs in s_to_t and s_to_t[cs] != ct:
            return False
        if ct in t_to_s and t_to_s[ct] != cs:
            return False
        s_to_t[cs] = ct
        t_to_s[ct] = cs
    return True


if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))  # expected output: True
    print(is_isomorphic("foo", "bar"))  # expected output: False
    print(is_isomorphic("paper", "title"))  # expected output: True
    print(is_isomorphic("badc", "baba"))  # expected output: False
