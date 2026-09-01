# Exchange Seats

## Problem Information
- **Platform:** LeetCode
- **Concept / Pattern:** SQL
- **Language:** mysql
- **Runtime:** 386 ms
- **Memory:** 0B
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Explanation
The solution uses a self-join on the Seat table to swap adjacent students. It handles odd and even IDs separately in the join condition and uses a UNION ALL to append the last student if the total count is odd, ensuring all students are included in the result. The complexities are O(N) for both time and space due to table scans and potential intermediate result set sizes.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
