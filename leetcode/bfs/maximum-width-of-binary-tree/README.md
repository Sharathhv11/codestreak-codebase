# Maximum Width Of Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** python3
- **Runtime:** 4 ms
- **Memory:** 20.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses Breadth-First Search (BFS) to traverse the tree level by level. Each node is assigned an index, doubling for the left child and adding one for the right child, to calculate the width of each level. The maximum width found across all levels is then returned.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
