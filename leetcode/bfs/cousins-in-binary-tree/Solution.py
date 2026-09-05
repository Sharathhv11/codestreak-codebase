# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = [(root,None)]

        while( queue ):
            n = len(queue)

            foundX = False
            parentX = -1

            foundY = False
            parentY = -1

            for i in range(n):
                node,parent = queue[i]

                if( node.val == x ):
                    foundX = True
                    parentX = parent

                if( node.val == y ):
                    foundY = True
                    parentY = parent 

                if( node.left ):
                    queue.append((node.left,node))
                if( node.right ):
                    queue.append((node.right,node))

            if(  (foundX and not foundY) or (not foundX and foundY)  ):
                #means the x and y are not in the same depth 
                return False

            if( foundX and foundY ):
                # both found on same level 
                return parentX != parentY #they are cousins

            queue = queue[n:]
        return False


                 