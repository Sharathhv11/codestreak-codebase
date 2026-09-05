# Maximum Width Of Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** java
- **Runtime:** 1 ms
- **Memory:** 43.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(W)

## Explanation
The solution uses Breadth-First Search (BFS) to traverse the tree level by level. Each node is assigned an index based on its position in a complete binary tree (left child 2*parent+1, right child 2*parent+2), adjusting for potential large values by subtracting the first node's index of each level. The maximum width is tracked as the difference between the last and first node's index at each level.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
