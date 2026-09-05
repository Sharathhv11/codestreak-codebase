# Top View of Binary Tree

## Problem Information
- **Platform:** GeeksforGeeks
- **Concept / Pattern:** BFS
- **Language:** python3
- **Runtime:** 0.17s
- **Memory:** 1111/1111 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution performs a Breadth-First Search (BFS) on the binary tree, using a queue to process nodes level by level. A dictionary stores the first encountered node's data for each horizontal distance, ensuring the top-most node at that distance is recorded. The time complexity is O(N) as each node is visited once, and space complexity is O(N) in the worst case for the queue and dictionary.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
