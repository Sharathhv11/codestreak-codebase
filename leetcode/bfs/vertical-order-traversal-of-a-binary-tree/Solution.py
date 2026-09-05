# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if( not root ):
            return []


        queue = [(root,0)]
        d = dict()

        while( len(queue) ):
            n = len(queue)
            ld = dict()

            for i in range(n):

                node,index = queue[i]

                ld[index] = ld.get(index,[])
                ld[index].append(node.val)

                if( node.left ):
                    queue.append((node.left,index-1))
                if( node.right ):
                    queue.append((node.right,index+1))
            queue = queue[n:]

            for key in ld.keys():
                values = sorted(ld[key])
                
                d[key] = d.get(key,[])
                d[key].extend(values)


        return [ d[i] for i in sorted(d.keys())]


        
            