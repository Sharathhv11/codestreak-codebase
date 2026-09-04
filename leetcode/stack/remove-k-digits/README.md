# Remove K Digits

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** java
- **Runtime:** 26 ms
- **Memory:** 45.7 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a stack to greedily build the smallest possible number by removing digits. It iterates through the input string, pushing digits onto the stack while maintaining the non-decreasing order, popping larger preceding digits if k removals are available. Any remaining k removals are handled by popping from the end of the stack, and leading zeros are removed before returning the result.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
