class Node:
    def __init__(self,val,minVal):
        self.value = val
        self.minVal = minVal

class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """

        if( not len(self.stack) ): #stack is empty
            self.stack.append(Node(value,value))
            return

        #what is value is not smaller
        node = self.stack[-1]
        if( node.minVal <= value ):
            self.stack.append(Node(value,node.minVal))
        #what is value smaller till now 
        else:
            self.stack.append(Node(value,value))

             
        

    def pop(self):
        """
        :rtype: None
        """
        if( len(self.stack) ):
            self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if( len(self.stack) ):
            return self.stack[-1].value
        

    def getMin(self):
        """
        :rtype: int
        """
        if( len(self.stack) ):
            return self.stack[-1].minVal
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()