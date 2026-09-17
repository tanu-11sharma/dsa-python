"""
Move Zeroes
-----------
Given an integer array, move all 0s to the end while keeping the
relative order of the non-zero elements unchanged. Do it in place,
in a single pass, using constant extra space via two pointers.

Time:  O(n)
Space: O(1)
"""


def move_zeroes(nums: list[int]) -> list[int]:
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # expected output: [1, 3, 12, 0, 0]
    print(move_zeroes([0, 0, 1]))  # expected output: [1, 0, 0]
    print(move_zeroes([1, 2, 3]))  # expected output: [1, 2, 3]
    print(move_zeroes([0, 0, 0]))  # expected output: [0, 0, 0]
