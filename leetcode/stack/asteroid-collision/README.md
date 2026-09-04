# Asteroid Collision

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Stack
- **Language:** python
- **Runtime:** 10 ms
- **Memory:** 13.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a stack to simulate the collisions. Incoming asteroids are pushed onto the stack unless they are negative and collide with a positive asteroid at the top of the stack. Collisions are resolved by popping the positive asteroid if it's smaller or equal, or by discarding the negative asteroid if it's smaller. If a negative asteroid survives all potential collisions, it's added to the stack. The time and space complexity are both O(N) as each asteroid is pushed and popped at most once.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
