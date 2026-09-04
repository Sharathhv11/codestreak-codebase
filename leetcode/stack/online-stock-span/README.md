# Online Stock Span

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 88 ms
- **Memory:** 17 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a monotonic stack to efficiently calculate the stock span. Each element in the stack stores a price and its corresponding span. When a new price arrives, we pop elements from the stack that are less than or equal to the current price, summing their spans to find the current span. This approach ensures that each element is pushed and popped at most once, leading to amortized O(1) time complexity per call.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
