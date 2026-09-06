# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parentHash = dict()


        pPointer = None
        pDepth = -1

        qPointer = None
        qDepth = -1

        found  = 0

        def dfs(root,depth,parent):
            nonlocal found, pPointer, pDepth, qPointer, qDepth
            if( found == 2 ):
                return

            if( not root ):
                return 

            if( root == p ):
                pPointer = root
                pDepth = depth 
                found+=1

            if( root ==  q ):
                qPointer = root
                qDepth = depth 
                found += 1

            parentHash[root] = parent

            dfs(root.left,depth+1,root)
            dfs(root.right,depth+1,root)


        dfs(root,0,None)


        if( pDepth == qDepth ):
            while( pPointer != qPointer ):
                pPointer = parentHash[pPointer]
                qPointer = parentHash[qPointer]
        elif( pDepth < qDepth ):
            while( qDepth > pDepth ):
                qPointer = parentHash[qPointer]
                qDepth -= 1

            while( pPointer != qPointer ):
                pPointer = parentHash[pPointer]
                qPointer = parentHash[qPointer]
        else:
            while( qDepth < pDepth ):
                pPointer = parentHash[pPointer]
                pDepth -= 1

            while( pPointer != qPointer ):
                pPointer = parentHash[pPointer]
                qPointer = parentHash[qPointer]

        return qPointer


            
