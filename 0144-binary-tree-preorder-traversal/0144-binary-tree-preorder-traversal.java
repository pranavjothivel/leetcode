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
    public List<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> preorder = new ArrayList<>();
        preOrderHelper(root, preorder);
        return preorder;
    }
    private static void preOrderHelper(TreeNode node, List<Integer> lst) {
        if (node == null) {
            return;
        }
        lst.add(node.val);
        preOrderHelper(node.left, lst);
        preOrderHelper(node.right, lst);
    }
}