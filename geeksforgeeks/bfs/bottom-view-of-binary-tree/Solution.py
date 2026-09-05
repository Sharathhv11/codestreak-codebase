'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
    
        if( root is None ):
            return []
    
        queue = [(root,0)]
        memo = dict()
    
        while( len(queue) ):
            n = len(queue)
            for i in range(n):
                node,index = queue[i]
                if( node is None ):
                    continue
                queue.append((node.left,index-1))
                queue.append((node.right,index+1))
                memo[index] = node.data
            queue = queue[n:]
    
        return [memo[i] for i in sorted(list(memo.keys()))]