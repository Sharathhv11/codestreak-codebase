# Binary Tree Right Side View

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** python
- **Runtime:** 1 ms
- **Memory:** 12.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(W)

## Explanation
The solution uses Breadth-First Search (BFS) to traverse the tree level by level. For each level, it records the value of the rightmost node encountered, which is effectively the last node processed at that level. The space complexity is O(W) where W is the maximum width of the tree, due to the queue storing nodes at each level.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
