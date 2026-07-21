"""
Evaluate Reverse Polish Notation
---------------------------------
Given a list of tokens representing an arithmetic expression in postfix
(reverse Polish) notation, compute its value. Valid tokens are integers
and the operators +, -, *, / (integer division truncating toward zero).

Time:  O(n)
Space: O(n)
"""

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    stack: List[int] = []
    ops = {"+", "-", "*", "/"}
    for tok in tokens:
        if tok in ops:
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(tok))
    return stack[-1]


if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))  # expected output: 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))  # expected output: 6
    print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # expected output: 22
    print(eval_rpn(["-7", "2", "/"]))  # expected output: -3
