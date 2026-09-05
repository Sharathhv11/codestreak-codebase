# Cousins In Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** python3
- **Runtime:** 0 ms
- **Memory:** 19.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses Breadth-First Search (BFS) to traverse the tree level by level. It keeps track of the parent of each node. Cousins are identified if both target nodes are found at the same level and have different parents. The time complexity is O(N) as each node is visited once, and the space complexity is O(N) in the worst case for the queue, which can store all nodes at the widest level.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
