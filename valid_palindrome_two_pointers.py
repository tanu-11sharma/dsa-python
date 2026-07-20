"""
Valid Palindrome (Alphanumeric Only)
--------------------------------------
Given a string, determine whether it reads the same forwards and
backwards once all non-alphanumeric characters are removed and the
letters are compared case-insensitively. Solve with two pointers
moving inward from both ends without allocating a cleaned copy.

Time:  O(n)
Space: O(1)
"""


def is_valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_valid_palindrome("A man, a plan, a canal: Panama"))
    # expected output: True
    print(is_valid_palindrome("race a car"))
    # expected output: False
    print(is_valid_palindrome(" "))
    # expected output: True
