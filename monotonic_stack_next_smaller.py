"""
Next Smaller Element (Monotonic Stack)
---------------------------------------
Given an array of integers, find, for every index, the index of the closest
element to its right that is strictly smaller than it. If no such element
exists, use -1 for that position. Solve it with a monotonically increasing
stack of indices so every element is pushed and popped at most once.

Time:  O(n)
Space: O(n)
"""


def next_smaller_indices(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n
    stack: list[int] = []  # indices whose values increase bottom to top

    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            result[stack.pop()] = i
        stack.append(i)

    return result


if __name__ == "__main__":
    print(next_smaller_indices([4, 2, 1, 5, 3]))  # expected output: [1, 2, -1, 4, -1]
    print(next_smaller_indices([1, 2, 3, 4]))  # expected output: [-1, -1, -1, -1]
    print(next_smaller_indices([9, 8, 7]))  # expected output: [1, 2, -1]
