"""
Course Schedule (Topological Sort)
--------------------------------------
You are given num_courses courses labeled 0 to num_courses - 1 and a list
of prerequisite pairs [a, b] meaning course b must be completed before
course a. Determine whether it is possible to finish all courses (i.e.
the prerequisite graph has no cycle), and if so return one valid order to
take them in.

Time:  O(V + E)
Space: O(V + E)
"""

from collections import deque, defaultdict
from typing import List, Optional


def find_course_order(num_courses: int, prerequisites: List[List[int]]) -> Optional[List[int]]:
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(c for c in range(num_courses) if in_degree[c] == 0)
    order: List[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_courses else None


if __name__ == "__main__":
    print(find_course_order(2, [[1, 0]]))  # expected output: [0, 1]
    print(find_course_order(2, [[1, 0], [0, 1]]))  # expected output: None
    print(find_course_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # expected output: [0, 1, 2, 3]
    print(find_course_order(1, []))  # expected output: [0]
