/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(root,0));
        int width = 1;
        
        while( !queue.isEmpty() ){
            int n = queue.size();
            int starting = 0;
            int ending = 0;
            int startingIndex = queue.peek().index;

            for( int i=0; i<n; i++ ){
                Pair p = queue.remove();
                int currentIndex = p.index - startingIndex;

                if( i == 0 )
                    starting = p.index;
                if( i == n-1 )
                    ending = p.index;

                if( p.node.left != null ){
                    queue.add(new Pair(p.node.left,2*currentIndex+1));
                }
                if( p.node.right != null ){
                    queue.add(new Pair(p.node.right,2*currentIndex+2));
                }
            }

            width = Math.max(width,ending-starting+1);
        }

        return width;
    }
}

class Pair{
    TreeNode node;
    int index;
    public Pair(TreeNode node,int index){
        this.node = node;
        this.index = index;
    }
}