# Tree Node

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 452 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a self-join to identify the type of each node. It categorizes nodes as 'Root', 'Inner', or 'Leaf' based on their parent ID and whether any node has them as a parent. The complexity is O(N) due to the scan of the table and potential intermediate storage for the join, and O(N) space for storing the results and intermediate join data.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
