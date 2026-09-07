"""
Remove All Adjacent Duplicates in String
-------------------------------------------
Given a string, repeatedly remove pairs of adjacent, identical characters
until no such pair remains. Return the resulting string.

Time:  O(n)
Space: O(n)
"""


def remove_duplicates(s: str) -> str:
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


if __name__ == "__main__":
    print(remove_duplicates("abbaca"))  # expected output: ca
    print(remove_duplicates("azxxzy"))  # expected output: ay
    print(remove_duplicates("aaaaaaaa"))  # expected output: (empty string)
    print(remove_duplicates("abcd"))  # expected output: abcd
