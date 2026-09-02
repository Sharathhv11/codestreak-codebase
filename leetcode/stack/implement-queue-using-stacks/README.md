# Implement Queue Using Stacks

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 0 ms
- **Memory:** 12.5 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** [object Object]
- **Space Complexity:** O(N)

## Explanation
The solution implements a queue using a single stack. The push operation is costly as it involves transferring all existing elements to a temporary stack and back to maintain the FIFO order, resulting in O(N) time complexity. Pop and peek operations are efficient O(1) because the front of the queue is always at the top of the stack.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
