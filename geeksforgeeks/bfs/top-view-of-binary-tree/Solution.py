'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        if( not root ):
            return []
            
        queue = [(root,0)]
        d = dict()
        
        while( len(queue) ):
            n = len(queue) #dynamic length 
            
            for i in range(n):
                node,index = queue[i]
                
                if( index not in d ):
                    d[index] = node.data
                
                if( node.left is not  None ):
                    queue.append((node.left,index-1))
                if( node.right is not None ):
                    queue.append((node.right,index+1))
            queue = queue[n::]
                
        return [ d[i] for i in sorted(list(d.keys()))]
                
            
        