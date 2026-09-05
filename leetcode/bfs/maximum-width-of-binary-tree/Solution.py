# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if( not root ):
            return 0

        queue = [(root,0)]
        maxLen = 0

        while queue:

            n = len(queue)

            start = queue[0][1]
            end = queue[n-1][1]

            maxLen = max(maxLen,end-start+1) 

            for i in range(n):
                node,index = queue[i]

                if( node.left ):
                    queue.append((node.left, 2*index+1 ))
                if( node.right ):
                    queue.append((node.right, 2*index+2 ))

            queue =  queue[n:]
        return maxLen