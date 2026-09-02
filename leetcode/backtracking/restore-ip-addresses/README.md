# Restore Ip Addresses

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Backtracking
- **Language:** java
- **Runtime:** 2 ms
- **Memory:** 42.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Explanation
The solution uses backtracking to explore all possible valid partitions of the input string into four IP address segments. For each segment, it checks if it's a valid IP part (1-3 digits, value <= 255, no leading zeros except for '0' itself). The time and space complexity are constant because the maximum length of an IP address string is fixed (12 characters), limiting the search space.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
