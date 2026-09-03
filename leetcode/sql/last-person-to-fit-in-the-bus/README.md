# Last Person To Fit In The Bus

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 1066 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N log N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a window function to calculate the cumulative sum of weights ordered by turn. It then filters for rows where the cumulative weight does not exceed 1000, orders these by cumulative weight in descending order, and selects the top person. The time complexity is dominated by the window function's sorting, and space complexity is due to the intermediate result of the window function.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
