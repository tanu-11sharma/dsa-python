"""
Fruit Into Baskets
------------------
A row of fruit trees is given as a list where each value is the fruit type
growing on that tree. You carry exactly two baskets, and each basket can
hold only one type of fruit (in unlimited quantity). Starting at any tree,
walk to the right picking exactly one fruit per tree, and stop the moment a
third distinct fruit type would need to go in a basket. Return the maximum
number of fruits that can be collected this way.

Time:  O(n)
Space: O(1) (the basket dict holds at most 3 keys at any time)
"""


def total_fruit(trees: list[int]) -> int:
    basket: dict[int, int] = {}
    left = 0
    best = 0

    for right, fruit in enumerate(trees):
        basket[fruit] = basket.get(fruit, 0) + 1

        while len(basket) > 2:
            left_fruit = trees[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]
            left += 1

        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    print(total_fruit([1, 2, 1]))  # expected output: 3
    print(total_fruit([0, 1, 2, 2]))  # expected output: 3
    print(total_fruit([1, 2, 3, 2, 2]))  # expected output: 4
    print(total_fruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # expected output: 5
