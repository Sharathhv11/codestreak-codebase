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
The solution uses backtracking to explore all possible ways to partition the input string into four valid IP address segments. At each step, it tries to form a segment and recursively calls itself with the remaining string. The time and space complexity are constant because the maximum length of an IP address string is limited (3*4=12), and the recursion depth is also fixed at 4.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
