"""
Basic Calculator
-----------------
Evaluate a mathematical expression given as a string containing non-negative
integers, '+', '-', parentheses, and spaces. Multiplication and division are
not part of the grammar. The expression is guaranteed to be well-formed.

Time:  O(n)
Space: O(n)
"""


def calculate(expression: str) -> int:
    stack = []
    result = 0
    number = 0
    sign = 1

    for ch in expression:
        if ch.isdigit():
            number = number * 10 + int(ch)
        elif ch in "+-":
            result += sign * number
            number = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * number
            number = 0
            result *= stack.pop()  # sign that preceded this parenthesis
            result += stack.pop()  # result accumulated before parenthesis

    result += sign * number
    return result


if __name__ == "__main__":
    print(calculate("1 + 1"))  # expected output: 2
    print(calculate(" 2-1 + 2 "))  # expected output: 3
    print(calculate("(1+(4+5+2)-3)+(6+8)"))  # expected output: 23
    print(calculate("2-(5-6)"))  # expected output: 3
