# Maximum Matching Of Players With Trainers

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Greedy
- **Language:** java
- **Runtime:** 30 ms
- **Memory:** 90.8 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N log N)
- **Space Complexity:** O(log N)

## Explanation
The solution sorts both players and trainers arrays and then uses a two-pointer approach to greedily match players with trainers. By iterating from the largest player and trainer downwards, it ensures that the largest possible player is matched with the largest possible trainer they can be trained by, maximizing the overall count.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
