"""
Decode String With Stack
--------------------------
An encoded string uses the form count[segment], where segment repeats count
times and may itself contain further encodings, for example "3[a2[c]]".
Expand the encoding into its full plain-text form. Use a stack to remember
the partial result and repeat count outstanding at each nesting level.

Time:  O(n), where n is the length of the decoded output
Space: O(n)
"""

from typing import List, Tuple


def decode_string(encoded: str) -> str:
    stack: List[Tuple[str, int]] = []
    current = ""
    count = 0
    for ch in encoded:
        if ch.isdigit():
            count = count * 10 + int(ch)
        elif ch == "[":
            stack.append((current, count))
            current, count = "", 0
        elif ch == "]":
            prefix, repeat = stack.pop()
            current = prefix + current * repeat
        else:
            current += ch
    return current


if __name__ == "__main__":
    print(decode_string("3[a]2[bc]"))  # expected output: aaabcbc
    print(decode_string("3[a2[c]]"))  # expected output: accaccacc
    print(decode_string("2[ab]cd"))  # expected output: ababcd
    print(decode_string("10[z]"))  # expected output: zzzzzzzzzz
