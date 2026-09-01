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
The solution uses a hash table (dictionary in Python) to store numbers encountered so far and their indices. For each number, it calculates the complement needed to reach the target and checks if the complement is already in the hash table. This allows for an average O(N) time complexity as lookups and insertions in a hash table are O(1) on average. The space complexity is O(N) due to the storage required for the hash table.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
