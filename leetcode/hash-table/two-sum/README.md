# Two Sum

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Hash Table
- **Language:** python
- **Runtime:** 1 ms
- **Memory:** 13.1 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a hash table (dictionary) to store numbers encountered so far and their indices. For each number, it calculates the complement needed to reach the target and checks if the complement exists in the hash table. This allows for an average O(1) lookup time per element, resulting in an overall O(N) time complexity. The space complexity is O(N) due to storing elements in the hash table.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
