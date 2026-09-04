# Simplify Path

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 8 ms
- **Memory:** 12.5 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a stack to process the path components. It iterates through the path, pushing directory names onto the stack and popping for '..' or ignoring '.' . The final path is constructed by joining the stack elements with '/'.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
