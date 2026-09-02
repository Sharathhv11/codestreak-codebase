# Implement Stack Using Queues

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Queue
- **Language:** python
- **Runtime:** 2 ms
- **Memory:** 12.5 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** [object Object]
- **Space Complexity:** O(N)

## Explanation
The solution implements a stack using a single queue. The push operation involves appending the new element and then rotating the queue by moving all existing elements to the back, ensuring the newest element is always at the front. Pop and top operations then become efficient O(1) operations on the queue's front.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
