"""
Maximum Average Subarray
-------------------------
Given an array of integers and an integer k, find a contiguous
subarray of length k with the maximum average value and return that
average. Use a fixed-size sliding window so the running sum is
updated incrementally instead of recomputed for every window.

Time:  O(n)
Space: O(1)
"""


def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


if __name__ == "__main__":
    print(find_max_average([1, 12, -5, -6, 50, 3], 4))  # expected output: 12.75
    print(find_max_average([5], 1))  # expected output: 5.0
    print(find_max_average([0, 4, 0, 3, 2], 1))  # expected output: 4.0
    print(find_max_average([-1, -2, -3, -4], 2))  # expected output: -1.5
