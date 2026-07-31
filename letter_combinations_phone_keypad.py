"""
Letter Combinations From A Phone Keypad
---------------------------------------
On an old telephone keypad each digit from 2 to 9 maps to a group of letters.
Given a string of such digits, return every letter string that could have been
typed, in the order produced by scanning the digits left to right.
Backtracking builds one candidate character at a time and undoes the last
choice before trying the next letter for that digit.

Time:  O(4^n * n) where n is the number of digits
Space: O(n) for the recursion stack, excluding the output list
"""

from typing import Dict, List

KEYPAD: Dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    for digit in digits:
        if digit not in KEYPAD:
            raise ValueError("digits may only contain the characters 2-9")

    results: List[str] = []
    current: List[str] = []

    def backtrack(position: int) -> None:
        if position == len(digits):
            results.append("".join(current))
            return

        for letter in KEYPAD[digits[position]]:
            current.append(letter)
            backtrack(position + 1)
            current.pop()

    backtrack(0)
    return results


if __name__ == "__main__":
    print(letter_combinations("23"))
    # expected output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    print(letter_combinations("9"))   # expected output: ['w', 'x', 'y', 'z']
    print(letter_combinations(""))    # expected output: []
    print(len(letter_combinations("789")))  # expected output: 36
