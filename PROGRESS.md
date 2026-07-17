# Progress Tracker

This file is the source of truth for the daily DSA automation. Update it every time new problems are committed.

## Plan

- Target: 450 problems total
- Pace: 5 new problems/day, every day
- Duration: 90 days
- Started: 2026-07-18 (Day 1, seeded with 10 problems)
- Stats: **10 / 450 solved** · Day 1 / 90

## Topic rotation queue

Cycle through this list in order, 5 topics per day (wrap back to the top when the list is exhausted). Skip a topic for the day if it was already used earlier that day. Prefer variety over repeating the same topic two days running.

1. Arrays & Hashing
2. Two Pointers
3. Sliding Window
4. Stacks & Queues
5. Linked Lists
6. Binary Search
7. Trees (traversals, BST)
8. Tries
9. Heaps / Priority Queues
10. Backtracking
11. Graphs (BFS/DFS, topological sort)
12. Union-Find / Disjoint Set
13. Dynamic Programming (1D)
14. Dynamic Programming (2D / grid)
15. Greedy
16. Intervals
17. Math & Geometry
18. Bit Manipulation
19. Sorting & Searching
20. Design (data structure implementation, e.g. caches, iterators)

## Rules for each daily run

- Read the current file list in the repo root to avoid duplicate filenames/problems.
- Each new problem is its own `.py` file, `snake_case` name describing the problem (e.g. `kth_largest_element.py`).
- Every file has: a top docstring (problem statement in 2-4 lines + Time/Space complexity), a clean solution, and a `if __name__ == "__main__":` block with at least 2-3 example calls and expected output as comments.
- Write original problems/solutions inspired by classic algorithmic patterns for the day's topics — do not copy proprietary problem statements verbatim from LeetCode or other platforms.
- Commit each file individually with a short, natural commit message (e.g. "Add kth_largest_element solution using a min-heap").
- After committing all 5 files for the day, update this PROGRESS.md: bump the solved count, bump the day count, and append a row to the Daily Log below. Commit that update too.
- If solved count reaches 450, write "COMPLETE" at the top of the Plan section and stop generating new problems on future runs.

## Daily Log

| Day | Date | Topics | Files added | Running total |
|---|---|---|---|---|
| 1 | 2026-07-18 | Arrays/Hashing, Linked Lists, Binary Search, Stacks, Intervals, Graphs, Sorting, Design, Sliding Window, DP | two_sum, reverse_linked_list, binary_search, valid_parentheses, merge_intervals, graph_bfs_dfs, quicksort, lru_cache, sliding_window, dynamic_programming | 10 |
