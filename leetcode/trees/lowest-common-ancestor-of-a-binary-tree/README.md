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
The solution uses a Depth First Search (DFS) to build a parent hash map and find the depths of nodes p and q. It then iteratively moves the deeper node's pointer up to match the depth of the shallower node. Finally, it moves both pointers up simultaneously until they meet at the Lowest Common Ancestor. The time and space complexity are both O(N) due to the DFS traversal and storing parent pointers in the hash map.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
