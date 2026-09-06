# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if( not root ):
            return []

        queue = [root]
        result = []

        direction = True # 0 - right to left  , 1 - left to right 

        while( queue ):
            n = len(queue)
            res = []
           
            for i in range(n):
                node = queue[i]
                res.append(node.val)

                if( node.left ):
                    queue.append(node.left)
                if( node.right ):
                    queue.append(node.right)
                    
            result.append(res if direction else res[::-1]) 
            direction = not  direction
            queue = queue[n:]

        return result 
            
        