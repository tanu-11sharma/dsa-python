"""
Majority Element (Boyer-Moore Voting)
-------------------------------------
Given a list of integers that is guaranteed to contain one value occupying more
than half of the positions, identify that value. Solve it in a single pass using
constant extra memory by pairing off differing elements: a value holding a strict
majority always survives such cancellation.

Time:  O(n)
Space: O(1)
"""

from typing import List, Optional


def majority_element(nums: List[int]) -> Optional[int]:
    candidate: Optional[int] = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


def majority_element_verified(nums: List[int]) -> Optional[int]:
    """Same idea, but confirms the candidate really is a majority (else None)."""
    candidate = majority_element(nums)
    if candidate is None:
        return None
    return candidate if nums.count(candidate) * 2 > len(nums) else None


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    # expected output: 3

    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    # expected output: 2

    print(majority_element_verified([1, 2, 3, 4]))
    # expected output: None

    print(majority_element_verified([7, 7, 7, 1]))
    # expected output: 7
