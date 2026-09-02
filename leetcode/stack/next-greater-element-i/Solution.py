class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = Stack()

        lookUp = set(nums1)

        n = len(nums1)
        m = len(nums2)

        indexHash = dict() 
        for i in range(n):
            indexHash[nums1[i]] = i

        result = [-1] * n

        for i in range(m):

            num = nums2[i] 

            if( (stack.isEmpty()  or stack.peek() >= num) and num in lookUp ):
                stack.push(num)
            else:
                while( stack.peek() < num ):
                    popValue = stack.pop()
                    result[indexHash[popValue]] = num

                if( num in lookUp ):
                    stack.push(num)

        return result 


            
