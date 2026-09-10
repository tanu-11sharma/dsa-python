"""
Sort Array By Parity
----------------------
Given an integer array, rearrange it in place so that every even number
comes before every odd number. The relative order within the evens or
within the odds does not need to be preserved. Solve it with two pointers
that swap elements toward the correct half in a single pass.

Time:  O(n), each element is visited and swapped at most once.
Space: O(1), the rearrangement happens in place.
"""

from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums


if __name__ == "__main__":
    result = sort_array_by_parity([3, 1, 2, 4])
    print(all(n % 2 == 0 for n in result[:2]) and all(n % 2 == 1 for n in result[2:]))
    # expected output: True

    print(sort_array_by_parity([0]))
    # expected output: [0]

    result2 = sort_array_by_parity([1, 3, 5, 2, 4, 6])
    print(sorted(result2[:3]), sorted(result2[3:]))
    # expected output: [2, 4, 6] [1, 3, 5]

    print(sort_array_by_parity([2, 4, 6]))
    # expected output: [2, 4, 6]
