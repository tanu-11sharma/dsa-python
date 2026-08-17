"""
Encode and Decode a List of Strings
-----------------------------------
Design a pair of functions that pack a list of arbitrary strings into one
string and later recover the original list from it. The strings may contain
any characters at all, including digits, punctuation, and the empty string,
so no single character can be reserved as a plain separator.

Time:  O(N) for encode and for decode, N = total characters
Space: O(N) for the packed string or the rebuilt list
"""

from typing import List


def encode(strings: List[str]) -> str:
    """Pack the list using a length-prefixed framing scheme."""
    parts: List[str] = []
    for s in strings:
        parts.append(str(len(s)))
        parts.append("#")
        parts.append(s)
    return "".join(parts)


def decode(encoded: str) -> List[str]:
    """Rebuild the list that was packed by encode."""
    result: List[str] = []
    i = 0
    while i < len(encoded):
        hash_pos = encoded.index("#", i)
        length = int(encoded[i:hash_pos])
        start = hash_pos + 1
        result.append(encoded[start:start + length])
        i = start + length
    return result


if __name__ == "__main__":
    print(encode(["hi", "there"]))
    # expected output: 2#hi5#there

    print(decode("2#hi5#there"))
    # expected output: ['hi', 'there']

    print(decode(encode(["", "3#x", "12"])))
    # expected output: ['', '3#x', '12']

    print(decode(encode([])))
    # expected output: []
