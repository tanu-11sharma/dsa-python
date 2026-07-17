"""
Valid Parentheses
------------------
Given a string containing just the characters '(', ')', '{', '}', '[' and
']', determine if the input string is valid. A string is valid if brackets
are closed by the same type and in the correct order.

Time:  O(n)
Space: O(n)
"""

def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
        # ignore any other characters
    return not stack

if __name__ == "__main__":
    print(is_valid("()[]{}"))   # True
    print(is_valid("(]"))       # False
    print(is_valid("([)]"))     # False
    print(is_valid("{[]}"))     # True
