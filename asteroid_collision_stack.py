"""
Asteroid Collision
------------------
A row of asteroids all travel along the same line. Each entry gives an
asteroid's size, and its sign gives its direction: positive moves right,
negative moves left. A collision happens only when a right-mover is
immediately followed by a left-mover; the smaller asteroid is destroyed,
and two of equal size destroy each other. Return the row once no further
collisions are possible.

Time:  O(n)
Space: O(n)
"""

from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    survivors: List[int] = []

    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and survivors and survivors[-1] > 0:
            if survivors[-1] < -asteroid:
                survivors.pop()
            elif survivors[-1] == -asteroid:
                survivors.pop()
                alive = False
            else:
                alive = False
        if alive:
            survivors.append(asteroid)

    return survivors


if __name__ == "__main__":
    print(asteroid_collision([5, 10, -5]))     # expected output: [5, 10]
    print(asteroid_collision([8, -8]))         # expected output: []
    print(asteroid_collision([10, 2, -5]))     # expected output: [10]
    print(asteroid_collision([-2, -1, 1, 2]))  # expected output: [-2, -1, 1, 2]
