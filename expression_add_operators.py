"""
Expression Add Operators
-------------------------
Given a string made up only of digits and a target integer, insert any
combination of the binary operators +, -, and * between the digits (without
reordering them) so that the resulting expression evaluates to the target.
Return every expression that works. Leading zeros in a multi-digit operand
are not allowed (e.g. "05" is invalid unless the operand is exactly "0").

Time:  O(4^n) in the worst case, since at each of the n-1 gaps between
       digits we choose one of three operators or to extend the current
       operand, and every candidate expression is evaluated in O(n).
Space: O(n) for the recursion stack and the current expression being built.
"""

from typing import List


def add_operators(digits: str, target: int) -> List[str]:
    results: List[str] = []
    n = len(digits)

    def backtrack(index: int, expr: str, value: int, last_operand: int) -> None:
        if index == n:
            if value == target:
                results.append(expr)
            return

        for end in range(index + 1, n + 1):
            operand_str = digits[index:end]
            if len(operand_str) > 1 and operand_str[0] == "0":
                break  # skip operands with leading zeros
            operand = int(operand_str)

            if index == 0:
                backtrack(end, operand_str, operand, operand)
            else:
                backtrack(end, expr + "+" + operand_str, value + operand, operand)
                backtrack(end, expr + "-" + operand_str, value - operand, -operand)
                backtrack(
                    end,
                    expr + "*" + operand_str,
                    value - last_operand + last_operand * operand,
                    last_operand * operand,
                )

    backtrack(0, "", 0, 0)
    return results


if __name__ == "__main__":
    print(sorted(add_operators("123", 6)))
    # expected output: ['1*2*3', '1+2+3']

    print(sorted(add_operators("232", 8)))
    # expected output: ['2*3+2', '2+3*2']

    print(add_operators("105", 5))
    # expected output: ['1*0+5', '10-5']

    print(add_operators("00", 0))
    # expected output: ['0+0', '0-0', '0*0']
