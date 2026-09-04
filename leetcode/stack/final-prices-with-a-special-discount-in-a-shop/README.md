# Final Prices With A Special Discount In A Shop

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 7 ms
- **Memory:** 12.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a monotonic stack to efficiently find the next smaller element for each price. The stack stores pairs of (price, index). For each new price, it pops elements from the stack that are greater than or equal to the current price, applying the discount. Finally, it pushes the current price and its index onto the stack. This results in a single pass, achieving O(N) time and O(N) space for the stack and result array.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
