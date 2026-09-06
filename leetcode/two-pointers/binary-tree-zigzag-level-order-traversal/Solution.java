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
class Solution{
    public List<List<Integer>> zigzagLevelOrder(TreeNode root){
        List<List<Integer>> result = new ArrayList<>();
        if( root == null ) return result;

        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.addFirst(root);
        boolean direction = true;

        while( !queue.isEmpty() ){
            int n = queue.size();
            List<Integer> levelNodes = new ArrayList<>();
            for( int i=0; i<n; i++ ){
                TreeNode node = null;
                if(direction){
                    node = queue.removeFirst();
                    if( node.left != null) queue.addLast(node.left);
                    if( node.right != null) queue.addLast(node.right);
                }else{
                    node = queue.removeLast();
                    if( node.right != null) queue.addFirst(node.right);
                    if( node.left != null) queue.addFirst(node.left);
                }
                levelNodes.add(node.val);
    
            }
            result.add(levelNodes);
            direction = !direction;
        }

        return result;
    }
}