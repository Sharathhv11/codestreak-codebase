# Managers With At Least 5 Direct Reports

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 359 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses a self-join on the Employee table to link employees to their managers. It then groups the results by manager and uses a HAVING clause to filter for managers with 5 or more direct reports. The time complexity is O(N) because each row is scanned once for the join and aggregation, and space complexity is O(1) as only a few counters are used during aggregation.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
