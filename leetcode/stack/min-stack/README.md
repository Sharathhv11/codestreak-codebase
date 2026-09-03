# Min Stack

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 260 ms
- **Memory:** 29.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(1)
- **Space Complexity:** O(N)

## Explanation
The solution uses a custom stack where each node stores both its value and the minimum value encountered so far up to that point. This allows for O(1) time complexity for push, pop, top, and getMin operations. The space complexity is O(N) because, in the worst case, we store N nodes, each potentially containing a new minimum.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
