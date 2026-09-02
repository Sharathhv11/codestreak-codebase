class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        sup = []

        while( not self.empty() ):
            sup.append(self.pop())

        self.stack.append(x)
        
        while( len(sup) ):
            self.stack.append(sup.pop())
        
        

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """

        return not len(self.stack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()