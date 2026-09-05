# Vertical Order Traversal Of A Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** python3
- **Runtime:** 0 ms
- **Memory:** 19.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N log N)
- **Space Complexity:** O(N)

## Explanation
The solution uses Breadth-First Search (BFS) to traverse the tree level by level. It stores nodes at the same horizontal distance (column) together and sorts them by their vertical level if they share the same column. The sorting within each column contributes to the N log N time complexity, while the queue and dictionaries store at most N nodes, leading to O(N) space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
