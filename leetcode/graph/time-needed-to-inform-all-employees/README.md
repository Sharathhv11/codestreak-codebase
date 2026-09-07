# Time Needed To Inform All Employees

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Graph
- **Language:** python3
- **Runtime:** 221 ms
- **Memory:** 83.6 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution models the employee hierarchy as a graph and uses Depth First Search (DFS) to traverse it. The DFS explores all paths from the head to inform employees, calculating the maximum time taken to reach any leaf employee (those who manage no one), which represents the total time to inform everyone.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
