# Valid Parentheses

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 10 ms
- **Memory:** 12.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a stack data structure to keep track of opening brackets. When a closing bracket is encountered, it checks if the stack is empty or if the top of the stack is the corresponding opening bracket. If a mismatch occurs or the stack is empty for a closing bracket, it's invalid. Finally, if the stack is empty after processing the string, all brackets were validly matched.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
