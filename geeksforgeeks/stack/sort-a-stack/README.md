# HI PEOPLEclass Solution {  public:  void ans(stack<int>&st,int x){      if(st.empty()||st.top()<=x){          st.push(x);          return;      }      int temp=st.top();      st.pop();      ans(st,x);      st.push(temp);  }    void sortStack(stack<int> &st) {        if(st.empty()){            return;        }        int x=st.top();        st.pop();        sortStack(st);        ans(st,x);    }};

## Problem Information
- **Platform:** GeeksforGeeks
- **Concept / Pattern:** Stack
- **Language:** python3
- **Runtime:** 0.19s
- **Memory:** 1115/1115 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N^2)
- **Space Complexity:** O(N)

## Explanation
The solution uses recursion to sort a stack. The `helper` function recursively calls itself to process the rest of the stack, then it inserts the current element into its correct sorted position using a temporary stack. This process, akin to insertion sort, results in O(N^2) time complexity due to nested operations within the recursion. The space complexity is O(N) due to the recursion depth and the temporary helper stack.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
