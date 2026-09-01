# Queue Using Array

## Problem Information
- **Platform:** GeeksforGeeks
- **Concept / Pattern:** Queue
- **Language:** python3
- **Runtime:** 0.03s
- **Memory:** 1120/1120 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** [object Object]
- **Space Complexity:** O(N)

## Explanation
The solution implements a queue using a Python list. Enqueue, isEmpty, isFull, getFront, and getRear operations are efficient O(1) time. However, the dequeue operation, which uses `list.remove(list[0])`, is O(N) because removing the first element requires shifting all subsequent elements.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
