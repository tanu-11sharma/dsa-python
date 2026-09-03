"""
Find All Missing Numbers
--------------------------
Given an array of n integers where every value lies between 1 and n
inclusive, some numbers appear twice while others never appear at
all. Return every value in the range [1, n] that is missing from
the array.

Time:  O(n)
Space: O(1) extra (the output list is not counted)
"""


def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i, v in enumerate(nums) if v > 0]


if __name__ == "__main__":
    print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))  # expected output: [5, 6]
    print(find_disappeared_numbers([1, 1]))  # expected output: [2]
    print(find_disappeared_numbers([1, 2, 3, 4, 5]))  # expected output: []
