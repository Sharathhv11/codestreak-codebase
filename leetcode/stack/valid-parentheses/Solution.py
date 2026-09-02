class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    def top(self):
        if self.empty():
            return None
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        n = len(s)
        i = 0
        while i < n:
            char = s[i]
            if( char in (")","}","]")):
                if( stack.empty() ): return False
                top = stack.top()
                if( 
                (char == ")" and  top == "(") or
                (char == "}" and  top == "{") or
                (char == "]" and  top == "[")
                  ):
                    stack.pop()
                else:
                    break
            else:
                stack.push(char)
            i+=1

        return stack.empty()

            

        