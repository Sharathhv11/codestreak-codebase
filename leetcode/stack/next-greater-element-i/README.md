# Next Greater Element I

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 9 ms
- **Memory:** 12.6 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(M)
- **Space Complexity:** O(N)

## Explanation
The solution uses a stack to find the next greater element for each number in nums2. It iterates through nums2, maintaining a decreasing monotonic stack. When a larger element is encountered, it pops smaller elements from the stack and updates their next greater element in the result. The lookup set and hash map for nums1 elements ensure efficient processing. The time complexity is O(M) as each element in nums2 is pushed and popped at most once. The space complexity is O(N) for the stack and lookup structures.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
