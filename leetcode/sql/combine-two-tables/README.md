# Combine Two Tables

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 407 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N+M)
- **Space Complexity:** O(1)

## Explanation
The solution uses a LEFT JOIN to combine the Person and Address tables based on the personId. This retrieves all records from the Person table and matching records from the Address table, filling in NULLs for addresses that don't exist. The time complexity is proportional to the sum of the sizes of the two tables, and the space complexity is constant as no significant auxiliary data structures are created.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
