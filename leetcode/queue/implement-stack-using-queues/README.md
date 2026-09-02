# Implement Stack Using Queues

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Queue
- **Language:** java
- **Runtime:** 0 ms
- **Memory:** 41.6 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution simulates a stack using a single queue. The push operation involves adding the new element and then rotating the queue by moving all existing elements to the back, ensuring the new element is at the front. Pop and top operations then become simple queue remove and peek respectively. This approach leads to O(N) time complexity for push due to the rotations, and O(N) space complexity for storing elements in the queue.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
