"""
Remove K Digits to Form the Smallest Number
---------------------------------------------
Given a non-negative integer represented as a string of digits and an
integer k, remove exactly k digits so that the remaining digits, kept
in their original order, form the smallest possible number. A
monotonic increasing stack greedily discards a digit whenever a
smaller digit arrives right after it and removals remain.

Time:  O(n)
Space: O(n)
"""


def remove_k_digits(num: str, k: int) -> str:
    stack = []
    remaining = k

    for digit in num:
        while stack and remaining > 0 and stack[-1] > digit:
            stack.pop()
            remaining -= 1
        stack.append(digit)

    if remaining > 0:
        stack = stack[:-remaining]

    result = "".join(stack).lstrip("0")
    return result if result else "0"


if __name__ == "__main__":
    print(remove_k_digits("1432219", 3))  # expected output: 1219
    print(remove_k_digits("10200", 1))  # expected output: 200
    print(remove_k_digits("10", 2))  # expected output: 0
