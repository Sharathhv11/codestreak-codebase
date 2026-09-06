# Binary Tree Zigzag Level Order Traversal

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** BFS
- **Language:** java
- **Runtime:** 1 ms
- **Memory:** 42.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a Breadth-First Search (BFS) approach with a deque to perform level order traversal. The deque stores nodes for the current level, and based on the direction flag, nodes are added to the front or back and removed from the front or back to achieve the zigzag pattern. The space complexity is O(N) to store the queue and the result list, and the time complexity is O(N) as each node is visited and processed once.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
