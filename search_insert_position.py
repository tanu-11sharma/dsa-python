"""
Search Insert Position
------------------------
Given a sorted array of distinct integers and a target value, return
the index of the target if it is present. Otherwise return the index
where it would be inserted to keep the array in sorted order. Solve
it with binary search rather than a linear scan.

Time:  O(log n)
Space: O(1)
"""


def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 5))  # expected output: 2
    print(search_insert([1, 3, 5, 6], 2))  # expected output: 1
    print(search_insert([1, 3, 5, 6], 7))  # expected output: 4
    print(search_insert([1, 3, 5, 6], 0))  # expected output: 0
