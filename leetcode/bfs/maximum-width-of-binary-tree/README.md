# Maximum Width Of Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** python3
- **Runtime:** 2 ms
- **Memory:** 20 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution performs a Breadth-First Search (BFS) on the binary tree, assigning a unique index to each node as if it were a complete binary tree. In each level traversal, it calculates the width by subtracting the minimum index from the maximum index of nodes present in that level. The space complexity is O(N) due to the queue storing nodes, and time complexity is O(N) as each node is visited and processed once.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
