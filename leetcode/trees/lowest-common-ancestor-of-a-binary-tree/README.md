# Lowest Common Ancestor Of A Binary Tree

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Trees
- **Language:** python3
- **Runtime:** 153 ms
- **Memory:** 64.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution performs a Depth First Search (DFS) to build a parent map and find the depths of nodes p and q. After finding both nodes and their depths, it moves the deeper node up towards the root until both nodes are at the same depth. Then, it moves both pointers up simultaneously until they meet at the Lowest Common Ancestor (LCA). The time complexity is O(N) due to the DFS traversal, and the space complexity is O(N) for storing the parent hash map and recursion stack.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
