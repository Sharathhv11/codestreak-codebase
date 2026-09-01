# Count Salary Categories

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 1586 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses SQL queries to categorize accounts based on salary ranges. It employs the UNION operator to combine the results of three separate SELECT statements, each counting accounts within a specific income bracket. The time complexity is O(N) because each query scans the Accounts table once, and the space complexity is O(1) as it only stores a few counter variables.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
