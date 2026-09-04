# Min Stack

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python3
- **Runtime:** 101 ms
- **Memory:** 31.1 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(1)
- **Space Complexity:** O(N)

## Explanation
The solution uses two stacks: one to store the elements and another to store the minimum element seen so far up to that point. Both push and pop operations take O(1) time by appending/popping from both stacks. getMin retrieves the minimum from the minStack in O(1) time. Space complexity is O(N) due to the storage of elements in two stacks.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
