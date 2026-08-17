"""
Generate Balanced Parentheses
-----------------------------
Given a positive integer n, produce every string made of n opening and n
closing round brackets that is correctly balanced. A string is balanced when
every closing bracket matches an earlier, still unmatched opening bracket.

Time:  O(4^n / sqrt(n))  -- proportional to the number of results produced
Space: O(n) recursion depth, excluding the returned list
"""

from typing import List


def generate_parentheses(n: int) -> List[str]:
    """Return every balanced bracket string built from n pairs."""
    if n <= 0:
        return [""]

    results: List[str] = []
    buffer: List[str] = []

    def build(open_used: int, close_used: int) -> None:
        if len(buffer) == 2 * n:
            results.append("".join(buffer))
            return
        if open_used < n:
            buffer.append("(")
            build(open_used + 1, close_used)
            buffer.pop()
        if close_used < open_used:
            buffer.append(")")
            build(open_used, close_used + 1)
            buffer.pop()

    build(0, 0)
    return results


if __name__ == "__main__":
    print(generate_parentheses(1))
    # expected output: ['()']

    print(generate_parentheses(2))
    # expected output: ['(())', '()()']

    print(generate_parentheses(3))
    # expected output: ['((()))', '(()())', '(())()', '()(())', '()()()']

    print(len(generate_parentheses(4)))
    # expected output: 14
