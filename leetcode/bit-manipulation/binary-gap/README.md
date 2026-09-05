# Binary Gap

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** Bit Manipulation
- **Language:** java
- **Runtime:** 0 ms
- **Memory:** 42.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(log N)
- **Space Complexity:** O(1)

## Explanation
The solution iterates through the binary representation of the number by repeatedly right-shifting and checking the least significant bit. It finds the distance between consecutive set bits by counting the zeros between them, effectively using bitwise operations for efficiency. The time complexity is logarithmic because the number of bits in N determines the number of iterations.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
