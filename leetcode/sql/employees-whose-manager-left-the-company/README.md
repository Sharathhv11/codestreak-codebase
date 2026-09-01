# Employees Whose Manager Left The Company

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 410 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N^2)
- **Space Complexity:** O(N)

## Explanation
The solution uses a subquery to identify manager IDs that exist in the Employees table but do not have a corresponding employee entry (i.e., the manager has left). It then filters employees whose salary is less than 30000 and whose manager ID is in this list of departed managers. The time complexity is O(N^2) due to the nested subquery potentially iterating over the table multiple times.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
