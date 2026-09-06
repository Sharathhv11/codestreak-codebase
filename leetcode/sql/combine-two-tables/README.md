# Combine Two Tables

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 407 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N + M)
- **Space Complexity:** O(N)

## Explanation
The solution uses a SQL LEFT JOIN to combine records from the Person and Address tables. It selects first name, last name, city, and state, ensuring all persons are included even if they don't have a corresponding address. The time complexity is proportional to the total number of rows in both tables (N for Person, M for Address), and space complexity is determined by the size of the output and intermediate structures, typically proportional to the number of rows in the 'left' table (Person).

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
