"""
Valid Triangle Count
----------------------
Given an array of non-negative integers representing stick lengths,
count how many triples of sticks can be assembled into a triangle
with positive area, i.e. the sum of the two shorter sides must
exceed the length of the longest side.

Time:  O(n^2)
Space: O(1) extra (beyond the sort)
"""


def triangle_number(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    count = 0
    for k in range(n - 1, 1, -1):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                count += j - i
                j -= 1
            else:
                i += 1
    return count


if __name__ == "__main__":
    print(triangle_number([2, 2, 3, 4]))  # expected output: 3
    print(triangle_number([4, 2, 3, 4]))  # expected output: 4
    print(triangle_number([1, 1, 1]))  # expected output: 1
