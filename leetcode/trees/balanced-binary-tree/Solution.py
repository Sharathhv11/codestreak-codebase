# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        stop = False

        def dfs(root):
            nonlocal stop
            if( stop ):
                return 0

            if( not root ):
                return 0

            lftDepth = dfs(root.left)
            rytDepth = dfs(root.right)

            if( abs(lftDepth - rytDepth) > 1 ):
                stop = True
                return 0

            return max(lftDepth,rytDepth)+1

        dfs(root)
        return not stop 

            