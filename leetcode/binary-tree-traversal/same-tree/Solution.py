# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we do BFS and detect tree is not same through vertical index 
        if( not p and not q ):
            return True
        if( (not p and q) or (p and not q)):return False
        queue1 = [(p,0)]
        queue2 = [(q,0)]

        while( queue1 and queue2 ):
            n = len(queue1)
            m = len(queue2)

            i = 0
            j  = 0
            x = min(n,m)

            while( i < x and j < x ):
                node1,inx1 = queue1[i]
                node2,inx2 = queue2[j]

                if( node1.val != node2.val or inx1 != inx2 ):
                    return False

                if( node1.left ):queue1.append((node1.left,inx1-1))
                if( node2.left ):queue2.append((node2.left,inx2-1))

                if( node1.right ):queue1.append((node1.right,inx1+1))
                if( node2.right ):queue2.append((node2.right,inx2+1))

                i+=1
                j+=1

            queue1 =  queue1[n:]
            queue2 =  queue2[m:]

        return  True if (len(queue1) == 0 and len(queue2) == 0 ) else False 