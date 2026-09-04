# Final Prices With A Special Discount In A Shop

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 11 ms
- **Memory:** 12.6 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a monotonic decreasing stack to find the next smaller element for each price. For each price, it pops elements from the stack that are greater than or equal to the current price, applies the discount, and pushes the current price onto the stack. This ensures each element is pushed and popped at most once, resulting in O(N) time and space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
